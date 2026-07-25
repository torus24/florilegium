# Example 01 — a formula the text layer silently broke

This is the worked example for **M1**. There is no engine yet (that is M2), so everything
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

## Channel 1 — the text layer

```bash
pdftotext -f 2 -l 2 paper.pdf - | sed -n '/relationship can be expressed/,+4p'
```

What comes out:

```
nðT; εÞ ¼ Cε ðε  ε0 Þ þ CT ðT  T0 Þ þ n0 ðT0 ; ε0 Þ
```

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
  benchmark. The benchmarks arrive with M4, and until then this repository quotes no numbers
  it cannot reproduce.
- the pipeline running. There is no engine here yet (M2), and no role prompts (M3): this
  example is deliberately doable by hand, which is also the honest way to check that the
  method does not depend on any particular model.

---

## Attribution

The equation and the symbol definitions discussed above are from Zhang, X. et al. (2024),
*Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review*, Journal
of Rock Mechanics and Geotechnical Engineering,
[doi:10.1016/j.jrmge.2024.01.008](https://doi.org/10.1016/j.jrmge.2024.01.008), used under
[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
