#!/usr/bin/env python3
"""florilegium — the First Loop (M1.5).

A minimal demonstration of ONE gate, rebuilt so that anyone can run it.

Read that sentence literally. This script is not the chain that produced the
numbers in architecture/decisions/ — that chain runs as agent sessions inside
Claude Code, and it is what M2 publishes. This is a small, separate program
that reproduces, end to end, the discrepancy examples/01 walks through by
hand. It is a demonstrator, not the engine.

It does four things, in this order:

  1. renders one PDF page as an image at >= 400 dpi;
  2. reads the same page from the PDF text layer;
  3. asks a multimodal model to transcribe the target from the *image only* —
     without ever being shown the text-layer reading, and without being told
     what to expect (see architecture/decisions/0006);
  4. compares the two readings and prints the differences.

It stops there, on purpose. Listing differences is the base gate's job;
judging them belongs to the adjudicator, and the third channel is the
adjudicator's too. Neither is implemented here — see architecture/quality-gates.md.

No source PDF ships with this repository. Point --pdf at a file you downloaded
yourself; examples/01 uses an openly licensed paper.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

# The role prompt is deliberately minimal. What matters is what it does NOT
# contain: the text-layer reading, the expected answer, or any hint of what
# the formula "should" look like. The target is given by position and number.
TRANSCRIBE_PROMPT = """\
You are re-reading a page of a technical document from an image of that page.

Transcribe, verbatim, what is PRINTED at this target: {target}

Rules:
- Transcribe the print, not what you think it ought to say. If the printed
  form looks wrong to you, transcribe it as printed and say so separately.
- Use plain-text notation: ^ for superscripts, _ for subscripts, and the
  actual Unicode character for Greek letters.
- Reproduce every sign, subscript, superscript, coefficient and decimal
  separator exactly as printed.
- For any glyph you are not certain about, say so explicitly and list the
  alternatives you considered.
- Do not judge, do not correct, do not summarise. Transcribe and report doubts.

Reply with exactly this, and nothing else:

PAGE HEADER: <the running header printed on the page, verbatim>
TRANSCRIPTION: <the target, verbatim>
UNCERTAIN GLYPHS: <one per line, or "none">
"""


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)
    except FileNotFoundError:
        sys.exit(f"error: {cmd[0]} not found. On Debian/Ubuntu: sudo apt install poppler-utils")
    except subprocess.CalledProcessError as e:
        sys.exit(f"error: {' '.join(cmd)} failed\n{e.stderr}")


def render_page(pdf: str, page: int, dpi: int, out_dir: str, crop: str | None) -> str:
    """Render one page to PNG. -singlefile gives a predictable filename."""
    prefix = os.path.join(out_dir, "page")
    cmd = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", "-singlefile"]
    if crop:
        try:
            x, y, w, h = (int(v) for v in crop.split(","))
        except ValueError:
            sys.exit("error: --crop wants four integers: X,Y,WIDTH,HEIGHT (pixels of the rendered page)")
        cmd += ["-x", str(x), "-y", str(y), "-W", str(w), "-H", str(h)]
    run(cmd + [pdf, prefix])
    return prefix + ".png"


def read_text_layer(pdf: str, page: int, grep: str | None, context: int) -> str:
    """Read the page from the text layer, narrowed to the target if asked.

    Narrowing matters: the signals compared below are counted per reading, and
    a whole page compared against a single formula is not a comparison at all.
    """
    page_text = run(["pdftotext", "-f", str(page), "-l", str(page), pdf, "-"]).stdout
    if not grep:
        return page_text
    lines = page_text.splitlines()
    hits = [i for i, line in enumerate(lines) if re.search(grep, line)]
    if not hits:
        return ""
    keep = sorted({j for i in hits for j in range(i, min(i + context + 1, len(lines)))})
    return "\n".join(lines[j] for j in keep)


def transcribe_api(png: str, prompt: str, model: str) -> str:
    """Alternative backend: one direct API call.

    Not the reference implementation, and not free: it needs an API key and
    bills per token. It exists to show that the method is not tied to one way
    of reaching a model — the same gate works through a plain API call.
    """
    try:
        import anthropic
    except ImportError:
        sys.exit("error: the api backend needs the SDK and a paid API key.\n"
                 "       pip install anthropic, or drop the flag to use the default\n"
                 "       cli backend (a local Claude Code install, no key needed).")
    with open(png, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode()
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": data}},
            {"type": "text", "text": prompt},
        ]}],
    )
    if response.stop_reason == "refusal":
        sys.exit("error: the model declined to answer this request.")
    return "".join(b.text for b in response.content if b.type == "text")


def transcribe_cli(png: str, prompt: str) -> str:
    """Default backend: a local Claude Code install.

    This is the reference implementation the README names, and it is how the
    origin chain invokes a model — a session, not an API call. It needs no API
    key and costs nothing beyond a subscription you already have. Being an
    agentic session, it is less deterministic than a single call.
    """
    if shutil.which("claude") is None:
        sys.exit("error: the cli backend needs Claude Code on PATH (https://claude.com/claude-code)")
    # Claude Code will not read a file outside its working directory, so the
    # render has to live under it — see the default for --out.
    full = f"Read the image at {os.path.abspath(png)} and do the following.\n\n{prompt}"
    return run(["claude", "-p", full]).stdout


def parse_reading(reply: str) -> str:
    """Pull the transcription out of the reply, and refuse anything that isn't one.

    A model that answers something other than a transcription — a refusal, a
    permission error, an apology — must not be fed into the comparison as if it
    were a reading of the page. That produces confident nonsense.
    """
    m = re.search(r"^TRANSCRIPTION:\s*(.+?)(?=^[A-Z][A-Z ]+:|\Z)", reply, re.M | re.S)
    if not m:
        sys.exit("error: the reply carries no TRANSCRIPTION line, so there is nothing to compare.\n"
                 "The model answered this instead:\n\n" + reply.strip())
    return m.group(1).strip()


# --- comparison -------------------------------------------------------------
# What follows compares *structural signals* that can be counted without
# knowing the right answer: how many minus signs each reading carries, which
# Greek letters, which digits. This is the point of the loop — an anchored
# comparison would defeat the whole method.

MINUS = "-‐‑‒–—−"  # hyphen and the dashes OCR likes to drop


def signals(text: str) -> dict:
    greek = sorted({c for c in text if "GREEK" in unicodedata.name(c, "")})
    return {
        "minus signs": sum(text.count(c) for c in MINUS),
        "greek letters": greek,
        "digits": sorted(set(re.findall(r"\d", text))),
        "parentheses": text.count("(") + text.count(")"),
    }


def compare(text_layer: str, image_reading: str) -> list[str]:
    a, b = signals(text_layer), signals(image_reading)
    return [f"{k}: text layer {a[k]!r} vs image {b[k]!r}" for k in a if a[k] != b[k]]


def main() -> None:
    p = argparse.ArgumentParser(description="florilegium — the First Loop")
    p.add_argument("--pdf", required=True, help="path to the PDF (never committed to this repo)")
    p.add_argument("--page", type=int, required=True, help="PDF page number (not the printed one)")
    p.add_argument("--target", required=True, help='what to transcribe, by position — e.g. "Eq. (1) in section 2.1"')
    p.add_argument("--dpi", type=int, default=400, help="render resolution, >= 400 (default: 400)")
    p.add_argument("--crop", help="X,Y,WIDTH,HEIGHT in pixels of the rendered page — see the note on resolution")
    p.add_argument("--grep", help="regex narrowing the text layer to the target — without it the two "
                                  "readings are not comparable (a whole page vs one formula)")
    p.add_argument("--context", type=int, default=4, help="lines to keep after each --grep match (default: 4)")
    p.add_argument("--backend", choices=["cli", "api"], default="cli",
                   help="cli: a local Claude Code install, no API key (default, and the "
                        "reference implementation). api: one direct API call — needs a paid key")
    p.add_argument("--model", default="claude-opus-5", help="api backend only (default: claude-opus-5)")
    p.add_argument("--out", help="where to keep the render (default: a scratch directory under the "
                                 "current one — the cli backend cannot read outside it)")
    args = p.parse_args()

    if args.dpi < 400:
        sys.exit("error: the method requires at least 400 dpi. A lower render is how false typo "
                 "accusations get made — see architecture/decisions/0001.")

    # Under the current directory, not /tmp: Claude Code refuses to read a file
    # outside its working directory, which silently breaks the cli backend.
    out_dir = args.out or tempfile.mkdtemp(prefix=".florilegium-run-", dir=os.getcwd())
    os.makedirs(out_dir, exist_ok=True)

    png = render_page(args.pdf, args.page, args.dpi, out_dir, args.crop)
    text_layer = read_text_layer(args.pdf, args.page, args.grep, args.context)
    prompt = TRANSCRIBE_PROMPT.format(target=args.target)

    print(f"[1/4] rendered  {png}")
    print(f"[2/4] text layer read from page {args.page}"
          + (f", narrowed by --grep {args.grep!r}" if args.grep else ""))
    if not args.grep:
        print("      warning: no --grep, so the whole page is compared against a single target."
              "\n      The differences below will be noise. Narrow it.")
    print(f"[3/4] re-reading the image ({args.backend} backend)...", flush=True)
    reply = (transcribe_api(png, prompt, args.model) if args.backend == "api"
             else transcribe_cli(png, prompt))
    image_reading = parse_reading(reply)

    print("\n--- reading 1: the PDF text layer -------------------------------")
    print(text_layer.strip() or "(empty — the text layer gave nothing for this page)")
    print("\n--- reading 2: the page image, read independently ---------------")
    print(reply.strip())

    print("\n--- differences -------------------------------------------------")
    diffs = compare(text_layer, image_reading)
    if diffs:
        for d in diffs:
            print(f"  * {d}")
    else:
        print("  no difference in the signals this script counts")
    print("\nThese are differences, not verdicts. Deciding which reading is right is\n"
          "the adjudicator's job, on a third channel — not this script's.")

    if args.out:
        with open(os.path.join(out_dir, "run.json"), "w") as f:
            json.dump({"pdf": os.path.basename(args.pdf), "page": args.page,
                       "target": args.target, "dpi": args.dpi, "backend": args.backend,
                       "text_layer": text_layer, "reply": reply, "image_reading": image_reading,
                       "differences": diffs}, f, indent=2)
            print(f"\nrun saved to {os.path.join(out_dir, 'run.json')}")


if __name__ == "__main__":
    main()
