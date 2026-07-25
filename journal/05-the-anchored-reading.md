# 05 — The anchored reading

🇮🇹 *Questa pagina è disponibile anche in [italiano](05-the-anchored-reading.it.md).*

*Journal entry. The data comes from prior use of the pipeline that preceded this project,
reported in generic form.*

---

## An optimization that looked obvious

The prompt that sends a role to re-read a formula has to tell it **where to look**: which
page, which equation, which line. So far, necessary.

At some point it also came to include **what to expect**. Not out of carelessness: out of
efficiency. Pasting the string taken from the note into the prompt looked like a clear
improvement — the reader knows exactly what to compare, wastes no time, the verdict is
targeted, fewer tokens are spent.

The reasoning is sound. The conclusion is wrong, for a reason you only see after you have
paid for it.

## The episode

The case surfaced on a pair of near-synonymous technical terms — two expressions so alike
that, read in haste, they get swapped without anyone noticing. The note carried one of them.
Into the prompt of **the re-transcriber — the base-level gate** — had been pasted **the one
from the note**.

The re-transcriber confirmed it, returning it as the verbatim of the printed text.

The print carried the other.

It had not misread the page: **it had not really needed to read it**. It had been handed the
answer along with the question, and it did what anyone would do — it verified that the
answer was consistent with itself.

The same mechanism reappeared elsewhere, on an acronym error: the note reported one
experimental scenario in place of another, and the full-level verifier — the one that looks
at the high-resolution image, the strongest safeguard in the pipeline — **confirmed the
note**. What caught the error was the text layer and the source's internal arithmetic. The
most expensive channel, neutralized by the way the question had been put to it.

## Why this is a structural defect and not an oversight

The independence of verification was already a principle of the project: whoever judges the
formula **does not see the first reading and has no stake in it**. It is written down, and it
is the heart of
[ADR-0001](../architecture/decisions/0001-formula-verification-from-image.md).

And it was already applied — at one point. Whoever adjudicates redoes the dimensional
analysis **by hand, before opening the verdict** of whoever verified, explicitly so as not to
be conditioned by it. The word *anti-anchoring* already appeared in the operating
instructions.

The hole was elsewhere, and this is the part that makes the episode instructive. The rule
protected the adjudicator from the verifier's verdict. **Nobody protected the verifier from
the note.** Independence had been guaranteed at the last link and taken for granted at the
second-to-last — where a single line of prompt can annul it.

And annul it it did, **leaving no trace**. An anchored reading does not produce a visible
error: it produces a **confirmation**. In the log it is indistinguishable from a successful
check. The pipeline goes on showing green gates while one of its channels has, in effect,
stopped being a channel.

## The rule that came out of it

The formulation is simple, and harder to comply with than it sounds:

> **The target is indicated by position and quantity. Never by value.**

*"Equation 12 on page 7, the coefficient on the left-hand side"* — legitimate. *"Equation 12
should read X"* — forbidden, in any form, paraphrased included, "useful context" included.

If there is a suspicion to communicate, you communicate **the disputed point**, not the
expected conclusion: *"there is a doubt on this line, re-read it"*, not *"this line should
read this"*. And whoever has re-read may then list the **differences**, once its own
transcription is closed — but judging those differences belongs to **a third actor**,
never to whoever re-read.

## A note of honesty

In the origin material this amendment **was made** — on one prompt only, and on the same day
the episode was put on record.

The ban on pasting the expected string entered the canonical prompt of the re-transcriber,
the base-level gate, with the rationale written beside the rule. It stayed in force: later
sessions cite it in their reports as current procedure.

On the full-level verifier — the one that looks at the high-resolution image — it was never
written. Its prompt still receives "the equations and values declared for this note", plus a
free-text line for suspicions: two doors through which the expected answer comes back in.

Two days later it came back in. The acronym error recounted above is **subsequent** to the
correction of the other prompt: the rule was already there, and it protected nothing,
because it was written on the wrong link.

It is worth saying instead of hiding it. A rule applied to a single link of a chain is not an
applied rule: it is a belief that you are protected. Here the decision is taken in full — it
is [ADR-0006](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.md).

## The principle, outside this project

It holds for any chain in which one component checks another, with or without language
models in the middle.

**A verifier that knows what it should find is not a verifier.** It is a second reader of the
same answer — at the cost of an independent check and with the value of none.

And the mistake is all the easier to make the more careful the system is: it is born of the
reasonable desire to be precise, not to waste anyone's time, to give context. The context you
give to whoever verifies is **exactly what stops being verified**.

---

**Decision born here:** [ADR-0006 — Whoever re-reads the source must not know the expected answer](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.md)
