# 02 — The silent corrector

*Journal entry. The data comes from prior use of the pipeline that preceded this project,
reported in generic form.*

---

## A defect that does not look like one

Entry [01](01-the-typo-that-was-not-there.md) tells of the pipeline accusing the source of
errors that do not exist. This one tells the opposite defect — and the worse one.

Here the pipeline **accuses nobody**. It reads a formula printed with an error, understands
that there is an error, **corrects it**, and writes the right form into the note. Without
saying so.

The result is a **correct** note. And that is precisely the problem.

## Why it is the worst case

A wrong note, sooner or later, jars. A unit that does not work out, an order of magnitude
out of place, a symbol that does not belong: something catches the eye, and you go check.

A **silently corrected** note never jars. It is mathematically impeccable, dimensionally
consistent, plausible at every point. No re-reading of the text unmasks it, because **there
is nothing wrong to see**. The only way to notice is to compare it against **what the source
actually prints** — and that comparison you either make by protocol, or you never make at
all.

The damage is not in the note. It is in the fact that the note **is no longer the source**.
Whoever uses it will believe they are citing the paper, and will be citing an interpretation
someone made of it on their own, in a step of which no trace remains.

## The tally

On a **single paper**, the gate caught **three** silent corrections. Three points where the
note carried the *correct* form instead of the *printed* one, with not a line to flag it:
two equations **silently normalized** — the printed form replaced by the “clean” one — and a
percentage rewritten in its sensible reading, because the printed one did not square with
the figures in the same paper.

On another paper, two transcription errors caught at the gate — with one detail worth
keeping: neither was caught by reading the image. They were caught by the **text layer
together with the source's internal arithmetic**. And on one of the two, the full-level
verifier had **confirmed the note**, because it was looking at the note while judging.
*(That story is entry [05](05-the-anchored-reading.md).)*

## The distinction that solved it

The formulation that unlocked everything is a single line, and it sits in the role card of
whoever extracts:

> **Fidelity ≠ correctness.**

Verbatim transcription guarantees that the note is **faithful to the print**. It does not
guarantee that the printed formula is **right**. They are two different properties, and a
pipeline that conflates them loses both.

Hence the rule. When whoever extracts notices that the source is wrong, they **do not have
permission to correct**. They have the obligation to do three things at once:

1. **transcribe verbatim what is printed** — the note stays faithful;
2. **declare the suspicion**, with the expected consistent form beside it;
3. **mark its nature**: the usage line states explicitly *this contradicts the source, and
   here is why*.

That way the correction does not disappear: it **becomes visible, traceable and arguable**.
Whoever reads the note sees what the paper says, what was concluded from it, and who
concluded what.

## The general principle

There is a lesson here that reaches well beyond formulas, and it is the reason this entry
exists.

A gate that asks **"is it right?"** cannot catch the silent corrector: the answer, in that
case, is honestly *yes*. The only gate that catches it is the one that asks **"where does it
come from?"** — that is, the one that treats a verdict as a question of **provenance**, not
of truth.

The useful question is not *is this formula correct*. It is: **is this line what the source
prints, or what someone thought the source meant to say?**

---

**Decision born here:** [ADR-0002 — The mandatory verdict is itself a source of error](../architecture/decisions/0002-verdict-as-source-of-error.md)
