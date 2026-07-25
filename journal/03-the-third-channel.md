# 03 — The third channel

*Journal entry. The data comes from prior use of the pipeline that preceded this project,
reported in generic form.*

*A note on wording: in this entry “third channel” means the **third route of verification**
beyond the two original readings — normally the re-reading of the text layer, with the
source's own arithmetic preferred wherever it exists. In the architecture the channels are
instead enumerated by **source** (layer, image, arithmetic):
[quality-gates §3](../architecture/quality-gates.md).*

---

## Two readings are not enough

The architecture starts with two channels: whoever **extracts** reads the text, whoever
**verifies** re-reads the image. Two independent readings, one per source. It looked
sufficient, and for a while it really did seem so.

Then came two episodes that say the same thing from opposite directions.

## Episode one — when both channels get it wrong together

On one correction, the image re-transcriber and the note gave the **same wrong answer**.
That is not a lucky break for the pipeline: it is the case that destroys the idea that two
channels are enough. If they agree, the gate passes. No discrepancy, no doubt, no flag —
and the error is certified.

The right verdict came from the **third channel**: re-reading the text layer, which fails in
a **structurally different** way from the other two. The image can fail on the **glyph** (one
symbol resembles another). The text layer fails on **extraction** (it drops a character,
inverts an order). These are faults that do not overlap: and that is exactly why the third
channel pays for itself.

The operational corollary is blunt: **raising the DPI does not fix a glyph error.** If the
problem is that two symbols resemble each other, looking at them more closely does not help
— you need to look at them **from somewhere else**.

## Episode two — when a channel is declared dead

The opposite case, and the one that produced the strictest rule.

On a paper with a mangled text layer, the third channel was declared **"unavailable
wholesale"** across every page carrying formulas. A reasonable decision: the page was
corrupted on the symbols, insisting seemed pointless.

At the next verification, on the same material, that channel proved **decisive on three
lines out of three**.

The reason is that "page corrupted on the symbols" does not mean "page useless". The
corruption hits the **symbols**; what survives is the plain text, the equation numbers and —
above all — **the source's internal arithmetic**. Throwing away the whole page to save time
means throwing away what was still good.

Hence the prohibition, written the way a prohibition ought to be written: **declaring the
text layer unavailable wholesale is forbidden.** Unavailability is **always per single
line**, always justified in the report, never an a-priori exclusion of a channel. The third
channel is **always attempted** — even on a page already given up for lost.

## The source's arithmetic is not a fallback

This deserves spelling out, because it is counterintuitive and easy to get backwards.

When the source publishes a **number the formula must reproduce** — a value in a table, a
worked example, a numerical result — then **redoing that computation** counts as a third
channel. And it is not a second-choice surrogate: it is the channel **to be preferred**.

The reason is that a computation that checks out is evidence of a different nature from a
reading. Two readings can agree in error, as we saw. Arithmetic that closes agrees with
nobody: **either it works out or it does not**, and it does not care what the other two read.

In the same spirit, whoever extracts cross-checks every formula against its **twins in the
same source** — the same quantity in another equation, a known physical limiting case — and
checks that the two sides **balance** dimensionally before even writing the note. These are
channels internal to the document, free, and systematically underrated.

## And when nobody has a doubt

There was one last hole, and it sat in the word *conditional*.

The third reading, originally, triggered **when someone had a doubt**: a gate with a
discrepancy, a contested verdict, a visible anomaly. Then came a case where the base gate
had said "no discrepancy" — so no doubt had arisen, so the third reading had not triggered —
and underneath sat two errors of the gravest class.

A reading conditional on doubt **does not trigger precisely in the cases where it would be
needed**, because a silent error generates no doubts. It is the same mechanism as entry
[01](01-the-typo-that-was-not-there.md), under another name.

Today the rule is unconditional: on every formula note, the third channel is **always
executed**, even when the gate found nothing. Especially when the gate found nothing.

## What to take away

- Two channels that agree **are not a confirmation**: they may be the same error twice.
- A channel is worth something in proportion to **how differently it fails** from the
  others, not to how accurate it is on its own.
- No channel is **absolute truth** — not even the high-resolution image, strongest safeguard
  though it is.
- A check that fires **only when there is a doubt** is a check that misses exactly the class
  of errors it exists for.

---

**Related decisions:** [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.md) · [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.md)
