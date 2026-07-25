# ADR-0001 — OCR text is not reliable for formulas → independent verification from the image

**Status:** accepted

---

## Context

A pipeline that extracts knowledge from technical PDFs relies on the **text layer** (OCR,
or text embedded in the PDF). On body text it works well. **On formulas it does not.**

The typical corruptions are **single-glyph**: a swapped subscript, a lost or doubled
exponent, an altered symbol — and they are **silent**: the output reads perfectly well,
so nobody checks. In an engineering context the damage does not stop at the note: these
formulas **feed calculation code**, so a silent error becomes a **wrong result
downstream**, produced by a script that never questions the number it was handed.

The problem has **two faces**, not one:
- **false negative** — a real transcription error that goes unseen;
- **false positive** — a text-only check that *accuses* the source of an error that is
  **not there**, and proposes a wrong “correction”.

## Hypothesis (what we believed before the experiment)

That a large model, reading the OCR text, could **flag suspect formulas on its own**; and
that **high-resolution rendering** of the image was needed only in doubtful cases, to be
triggered **“on demand”** whenever someone had an explicit doubt.

## Experiment (what we measured)

> **Real data**, from prior use of the pipeline that preceded this project, rewritten in
> generic form — no reference to the corpus. It is a **small sample**: read it as
> *directional* evidence that motivated the decision, not as a controlled benchmark
> (that is M4).

We went back over the **5 formulas** that the text check had flagged as a **“source typo”**
(i.e. the source is wrong, use the corrected version) — they had accumulated across
different papers and different runs, not in a single batch — and re-rendered each one: the
**contested line only**, at **high resolution (≥400 dpi)**, re-read **from the image**,
independently. Result:

- **4 out of 5 were false alarms:** the source was correct, the error was in the
  low-resolution OCR/rendering. The “correction” would have made things worse.
- **The 5th was a real source error,** confirmed the same way.

**Key finding:** the “doubt” that was supposed to trigger high-resolution rendering —
left to discretion — **never arrived**. Rendering “on demand” was, in practice,
rendering that never happened.

## Decision

1. **Formulas are not verified from the text, but from the image.** High-resolution
   rendering of the page/line → **independent re-transcription** from the image →
   **cross-check** against the text reading.
2. **Verification is third-party.** The role that judges the formula **does not see**
   the first reading and **has no stake** in it: a non-independent agent cannot wave its
   own mistake through as correct.
3. **High-resolution rendering of the contested line is mandatory, not “on demand”**, for
   every flagged formula, *before* it is signed off as verified.
4. **Two gate levels, plus an adjudicator:** *base* (independent re-transcription from the
   image, **with no verdict**) on every note carrying a formula or a point-of-use value;
   *full* (verification from the image at ≥400 dpi, **with** a verdict) **only where a
   verdict accuses the source**, or the note is a benchmark anchor — because a silent error
   produces no flag. A discrepancy found at the base level opens the **adjudication**, not
   the expensive gate.

## Consequences

- **What it solves:** catches silent formula errors a single prompt cannot see; and —
  just as important — **clears false alarms**, avoiding “fixing” sources that were
  already correct.
- **What it costs:** more tokens and more passes. This is the project’s stated trade-off —
  *knowledge quality over token efficiency*.
- **What it does NOT solve:** formulas where **not even the image** is legible (a page too
  degraded). There the system **flags**, it does not guess.
- **When to revisit:** if a future model could read formulas from the image **reliably in
  a single pass**, the two gate levels could merge (this ADR would then become
  `superseded`).
