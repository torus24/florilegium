# 01 — The typo that was not there

*Journal entry. It recounts a real episode and what changed in the method because of it.
The data comes from prior use of the pipeline that preceded this project, reported in
generic form.*

---

## The wrong suspicion

The question everything started from was: **is the pipeline transcribing formulas
correctly?**

It was the wrong question. Not because it was useless, but because it took the direction of
the error for granted. We were looking for badly transcribed formulas. What was actually
happening was something else, and more insidious: the pipeline transcribed the formula one
way, **found no match against the source, and concluded that the source was wrong.**

In the notes produced, this left an unmistakable trace: a line marked **"source typo"**,
with an operational prescription attached — *the paper prints it this way, but it is wrong:
use this other form instead*. A note like that is not a passive error. It is an error
**that gives instructions**.

## Four out of five

When we went back and re-checked those lines one by one, rendering the page as an **image**
and re-reading the disputed line at high resolution, the result was this: out of **five**
accusations against the source, **four were false**. The source printed exactly what it was
supposed to print. It was the pipeline that had misread — and had then built a usage rule
on top of it.

The starkest case was not even an imprecise reading: it was a **fabricated** accusation. The
verification charged an equation with an error involving **symbols never printed in that
formula**. It had not misread: it had produced a verdict because it had been asked for one.
*(That is where [ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.md)
comes from.)*

## The fourth case — the one that decided everything

We had found the first three because **someone had a doubt**. An equation looked odd, we
went and checked, the false accusation surfaced. A process that works, but that depends
entirely on the doubt arriving.

The fourth arrived another way. We were working on a note for a completely different reason
— unblocking an item left pending — and in doing so we passed over an equation **nobody had
questioned**. No suspicion, no flag, no apparent anomaly. Under high-resolution rendering,
the glyph printed by the source differed from the one transcribed in the note, and on that
non-existent difference the note had founded yet another "source typo" line.

The final tally for that note: it carried **four** “source typo” lines, and the **real**
source typos were **two**. These are two different tallies and **they do not add up**: the
five accusations re-checked one by one are spread over three different papers — two of
which carried more than one — while these four all sit on the same note, and the two
tallies overlap. Read them as two views of the same material, not as two independent
counts.

This is the point that changed the method, and it matters more than the number. If the
fourth case surfaced **by accident**, while we were looking at something else, then the
question is no longer *how many did we find*. It is: **how many are left where nobody will
ever look?**

The data says the doubt does not arrive.

## What changed

The previous rule was reasonable and wrong: *high-resolution rendering happens when there is
a doubt.* It was cheap precisely because it triggered rarely — but it triggered rarely for
the worst reason, namely that a silent error, by definition, generates no doubts.

The new rule is blunt and it works: **every line that accuses the source requires the
disputed line to be rendered as an image at ≥400 dpi before it can be signed off.** At any
gate level. No exceptions, no suspicion required, no discretion.

This is not a micro-optimization: it is a reversal of the burden of proof. Before, the
pipeline could accuse the source **and** get away with it. Now, to accuse the source, it
must **prove it through a channel different from the one that produced the accusation.**

## Why this is the founding entry

Everything else in the project descends from here.

- That a verdict is not enough, and must be weighed rather than believed →
  [ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.md).
- That verification must be **third-party** — whoever judges is not whoever extracted →
  [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.md).
- That a chain of separate roles is worth more than a single good prompt →
  [ADR-0004](../architecture/decisions/0004-chain-vs-single-prompt.md).
- That the extra cost is **intrinsic to quality**, not waste to be optimized away →
  [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.md).

And above all: a knowledge base that is wrong **in silence** is worse than one that does not
exist. Someone without the base goes and reads the paper. Someone with a wrong base trusts
it.

---

**Decision born here:** [ADR-0001 — OCR text is not reliable for formulas](../architecture/decisions/0001-formula-verification-from-image.md)
