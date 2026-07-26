# Example 01 — a formula the text layer silently broke

🇮🇹 *Questa pagina è disponibile anche in [italiano](README.it.md).*

This is the worked example for **M1**. The chain is not published yet (that is M2), so everything
here is **reproducible by hand** with two commands from `poppler-utils` — no API key, no
model, no account. What the pipeline automates, you can do manually in five minutes and see
the same thing.

The point is not that the pipeline is clever. The point is that **the text layer loses an
operator without telling anyone**, and that a second reading from the image catches it.

---

## The source

| | |
|---|---|
| **Title** | Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review |
| **Authors** | Xuehui Zhang et al. |
| **Journal** | Journal of Rock Mechanics and Geotechnical Engineering (2024) |
| **DOI** | [10.1016/j.jrmge.2024.01.008](https://doi.org/10.1016/j.jrmge.2024.01.008) |
| **License** | **CC-BY 4.0** — printed on page 1 of the article and recorded in the Crossref metadata |

The PDF is **not committed to this repository** and never will be — see the note on sources
in the [README](../../README.md). Download it yourself from the DOI above; it is free.

> **A note on page numbers.** This example locates the target by **where it sits in the
> document structure — §2.1, Eq. (1)** — and treats the page number as a lookup aid, not as
> an identifier: the article first circulated as the publisher's *corrected proof*, whose
> header reads `xxx (xxxx) xxx` and whose pagination is **not** the final one. Addressing a
> target by structure rather than by a number that shifts between versions is the same
> discipline as
> [ADR-0006](../../architecture/decisions/0006-reader-must-not-know-the-expected-answer.md).

In the **final published version** (23 pages), §2.1 falls on **PDF page 2**, printed page
**3842**. The commands below use `-f 2 -l 2`; if your copy is the proof, §2.1 sits on PDF
page 3 and the flags need adjusting.

---

## Prerequisites

Any Unix-like system (Linux, macOS, WSL) and `poppler-utils` — the two commands used
below, `pdftotext` and `pdftoppm`, come from that package:

```bash
sudo apt install poppler-utils     # Debian/Ubuntu
brew install poppler               # macOS
```

This walkthrough was verified with **poppler 24.02.0**. Rendering can differ slightly
between poppler versions; the loss of the minus signs shown below, however, comes from the
**PDF**, not from the version.

Download the article from the DOI above and save it in this directory as **`paper.pdf`** —
that is the filename the commands expect.

---

## Channel 1 — the text layer

```bash
pdftotext -f 2 -l 2 paper.pdf - | grep -A 4 'relationship can be expressed'
```

What comes out:

```
nðT; εÞ ¼ Cε ðε  ε0 Þ þ CT ðT  T0 Þ þ n0 ðT0 ; ε0 Þ
```

**If the output is empty**, nothing is broken and you did nothing wrong: your copy is
probably the corrected proof, where §2.1 sits on PDF page **3** — rerun with `-f 3 -l 3`.
The command does not fail, it simply returns nothing.

Some of this damage is loud and harmless: `ð` for `(`, `Þ` for `)`, `¼` for `=`, `þ` for `+`
— a font-encoding mismatch that any reader spots instantly, and that a language model
repairs correctly without hesitation.

Two pieces of damage are neither loud nor harmless:

1. **`ν` became `n`.** The Brillouin frequency shift is a Greek nu. As a Latin `n` it reads
   like a count, or an index.
2. **Both minus signs are gone.** `ðε  ε0 Þ` is `ε`, two spaces, `ε0`. The subtraction
   operator did not become a wrong character — it **stopped existing**.

This is the failure mode the project is built around. Nothing here looks corrupted enough to
investigate: a reader repairing the obvious `ð`/`Þ`/`¼`/`þ` noise arrives at a formula that
is clean, plausible, dimensionally arguable — and wrong. `C_ε(ε ε₀)` invites reconstruction
as a product, or as a sum. Both would be silently, usably incorrect.

---

## Channel 2 — the image

Render the page at high resolution and read the equation from the picture, without looking
at what channel 1 produced:

```bash
pdftoppm -r 400 -f 2 -l 2 -png paper.pdf page
```

This writes **`page-02.png`** in the current directory — poppler pads the number to the
length of the document, and the published article has 23 pages. Open it with any image
viewer and look for Eq. (1), in §2.1.

The printed equation is:

> **ν(T, ε) = C_ε(ε − ε₀) + C_T(T − T₀) + ν₀(T₀, ε₀)**  (1)

Both minus signs are there and unambiguous at 400 dpi. So is the Greek `ν`.

**The cross-check:** two independent readings, two differences — a lost operator (twice) and
a swapped symbol. Neither was flagged by anything; the text-layer output carried no marker of
damage at those two points.

---

## Channel 3 — the source's own arithmetic

The two readings above disagree, and the image is the stronger evidence. But *stronger
evidence* is not the same as *proof*, and this is where the method does something a
two-channel pipeline cannot: it settles the question **without looking at either reading**.

The article defines its own symbols in the sentence right after the equation: `ν₀(T₀, ε₀)`
is the **baseline** BFS at the reference temperature `T₀` and reference strain `ε₀`.

Now impose that definition on the formula. Set `T = T₀` and `ε = ε₀` — the measurement *is*
the baseline. The equation must then reduce to `ν = ν₀`, by the source's own definition of
what `ν₀` means. That forces the first two terms to **vanish** at the reference point:

- with a **difference**, `C_ε(ε₀ − ε₀) = 0` and `C_T(T₀ − T₀) = 0` → `ν = ν₀` ✅
- with a **product**, `C_ε·ε₀·ε₀ ≠ 0` → the baseline is not the baseline ❌
- with a **sum**, `C_ε(ε₀ + ε₀) ≠ 0` → same ❌

The missing operator can only be a minus. This is the **third channel**: not a third reading,
but the document checking itself. It fails in a way the other two cannot — it does not care
what anybody read, only whether the result closes.

Dimensional consistency agrees: every term must be a frequency, so `C_ε` is Hz per unit
strain and `C_T` is Hz per degree — which is exactly what the article says they are.

---

## The resulting note

→ [`notes/dfos-brillouin-frequency-shift.md`](notes/dfos-brillouin-frequency-shift.md)

An atomic note: one formula, provenance in the frontmatter, and a record of **which channels
verified it and how**. That last part is the difference between a note you can use and a note
you have to re-check.

---

## What this example shows — and what it does not

**It shows:**

- a real, silent, single-operator loss in a text layer, on an openly licensed paper anyone
  can download;
- that a second reading from the image catches it;
- that a third, non-visual channel can settle it independently — see
  [journal/03](../../journal/03-the-third-channel.md).

**It does not show:**

- a measured error rate. This is **one formula in one paper**: a demonstration, not a
  benchmark. The measurements arrive with M4 — directional, since their sources are
  copyrighted — and every number this repository quotes is labelled for what it is:
  directional evidence from private runs (as in ADR-0003), never a reproducible benchmark.
- the pipeline running. Neither the role cards nor the gate protocol are here yet (both M2): this
  example is deliberately doable by hand, which is also the honest way to check that the
  method does not depend on any particular model.

---

## The same thing, automated

**What this is, precisely.** [`scripts/compare_readings.py`](../../scripts/compare_readings.py) is a
minimal demonstration of **one gate**, rebuilt as a standalone program so that anyone can run
it. It is **not** the chain that produced the numbers in the decision records: that chain runs
as agent sessions inside Claude Code, and publishing it — the role definitions, the skills,
the hooks — is what **M2** is for. Read this as a demonstrator, not as the chain.

Everything above is done by hand, and it should stay that way: it is what makes the claim
checkable without trusting us. The script is the same four steps with the model doing the
second reading instead of you.

```bash
python3 scripts/compare_readings.py \
  --pdf paper.pdf --page 2 \
  --target "the first displayed numbered equation, Eq. (1), in section 2.1" \
  --grep 'ðT; εÞ' --context 1
```

It renders the page at 400 dpi, reads the text layer, asks a multimodal model to transcribe
the target **from the image alone**, and prints the differences between the two readings. On
this paper it reports what you found by hand: two minus signs present in the image and absent
from the text layer, and a Greek `ν` the text layer turned into a Latin `n`.

**Two backends, and the default is deliberate.** By default it drives a local
[Claude Code](https://claude.com/claude-code) install: **no API key, nothing to pay** beyond a
subscription, and it is the reference implementation this repository names. It is an agentic
session rather than a single call, so it is less deterministic — that is the trade.
`--backend api` sends one direct API call instead, which needs `pip install anthropic` and a
**paid** `ANTHROPIC_API_KEY`; it is there to show the method is not tied to one way of
reaching a model, not because you need it.

**What it does not do.** It lists differences and stops. It does not decide which reading is
right, and it does not run the third channel — both belong to the adjudicator
([quality-gates](../../architecture/quality-gates.md)), which is M2. The prompt it sends is
never shown the text-layer reading and is never told what to expect, which is the rule
[ADR-0006](../../architecture/decisions/0006-reader-must-not-know-the-expected-answer.md)
exists to enforce.

**A limit worth knowing.** The render is 400 dpi, but a full page at that resolution is
larger than the model accepts and gets downscaled on the way in — for this equation that was
enough, but where a glyph is genuinely marginal, crop the target instead:
`--crop X,Y,WIDTH,HEIGHT`, in pixels of the rendered page. A crop keeps the real resolution.

---

## Attribution

The equation and the symbol definitions discussed above are from Zhang, X. et al. (2024),
*Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review*, Journal
of Rock Mechanics and Geotechnical Engineering,
[doi:10.1016/j.jrmge.2024.01.008](https://doi.org/10.1016/j.jrmge.2024.01.008), used under
[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
