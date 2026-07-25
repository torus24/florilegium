# ADR-0006 — Whoever re-reads the source must not know the expected answer

**Status:** accepted

---

## Context

[ADR-0001](0001-formula-verification-from-image.md) establishes that verification is
**third-party**: the role that judges a formula does not see the first reading and has no
stake in it. It is the principle the whole chain rests on.

But "not seeing the note" is not a sufficient guarantee, because independence is not lost
only by showing the document: it is lost **with a fragment of the document inside the
prompt**. And the verification prompt necessarily has to say *where* to look. The boundary
between pointing at the target and suggesting the answer is thin, and that is exactly where
it breaks.

This ADR closes the exposed side of ADR-0001. The principle protected **the adjudicator**
from someone else's verdict — it was already practice to redo the computations by hand
*before* opening the verifier's verdict, avowedly so as not to be conditioned by it. No rule
protected **the verifier** from the note it was supposed to question.

There is a further reason why the scope cannot stop at those who issue verdicts. In the
originating chain the base-level gate **does not judge at all**: it is a role created by
*removing* the verdict from the second reading, after verdicts had proved wrong in both
directions — correlated confirmations on faulty notes, and accusations against sound ones
(the same finding as [ADR-0002](0002-verdict-as-source-of-error.md)). That role re-reads
from the image and lists the discrepancies; a third party judges them, with one more
channel at its disposal. **And it anchored anyway.** Taking away the power to judge did
not take away the anchoring, because anchoring does not strike the judgment: it strikes
**the reading**. Hence this ADR speaks of *whoever re-reads the source*, not of *whoever
verifies*.

## Hypothesis (what we believed)

That pasting the expected string — taken from the note — into the verification prompt made
the check **more precise and cheaper**: an unambiguous target, no time lost searching, a
focused verdict, fewer tokens.

## Experiment (what we observed)

> **Real data**, from prior use of the pipeline that preceded this project, in generic form.
> Small sample → *directional* evidence, not a benchmark (that is M4).

Two independent episodes, same mechanism.

1. On a pair of near-synonymous technical terms, the note's string was pasted into the
   prompt of the **re-transcriber — the base-level gate**, the role that re-reads from the
   image and issues no verdicts. It **returned that string as the verbatim of the printed
   text**; the print carried the other term. It had not misread the page: it had not needed
   to read it, because the answer had arrived together with the question. There was no
   consequence for the datum — the value held on two other channels — but the channel meant
   to check it had stopped checking.
2. On an acronym error (one experimental scenario reported in place of another), the
   **full-level** verifier — the one that renders the image at high resolution, the most
   expensive safeguard in the chain — **anchored to the note** and confirmed it. The error
   was caught by two other channels (text layer and the source's internal arithmetic).

The common trait, and what makes the defect serious: an anchored reading **does not produce
an error, it produces a confirmation**. In the logs it is indistinguishable from a successful
check, and the channel reads as active while it has stopped working. It holds at every gate
level: in the first episode the confirmation comes from a role that does not even have the
power to issue verdicts.

There is a second finding, and it is the one that dictates this ADR's scope. After the first
episode the rule **was written** — but only on the prompt that had generated it, the one for
the base-level gate. The full-level prompt was left as it was. The second episode happened
**two days later**, on that prompt. A correct rule, applied to a single link, moved nothing:
it produced the belief that we were protected.

## Decision

1. **The verification prompt does not contain the expected form.** In no form: not verbatim,
   not paraphrased, not as "useful context", not as an example.
2. **The target is indicated by POSITION and QUANTITY, never by value.** *"Equation 12, page
   7, the coefficient on the left-hand side"* is legitimate; *"equation 12 should read X"* is
   forbidden.
3. **A suspicion is communicated as a disputed point, not as an expected conclusion:**
   *"there is a doubt on this line, re-read it"*, never *"this line should read this"*.
4. **Transcribe first, compare afterwards — and whoever re-reads does not judge.** The
   re-reading is closed *before* the note is opened. Whoever has re-read may then list the
   **differences** — a difference between two readings is not an accusation — but judging
   those differences belongs to a third party, who has one more channel available. It is
   this point, not point 1, that covers the case where the note is handed over in full to
   whoever re-reads. And it must be said: the ordering, on its own, is an instruction, and
   is worth what instructions are worth (see *Consequences*); the structural safeguard is
   the **separation between whoever reads and whoever judges**.
5. **Whoever adjudicates redoes the computations before opening anyone else's verdict**
   (dimensional analysis and arithmetic): a rule already in place, confirmed here as part of
   the same family.
6. **The rule applies to EVERY prompt of EVERY role that re-reads the source, at every gate
   level** — whether or not that role is allowed to judge. It is
   not a remedy for the episode that generated it: it is a scope requirement. A verification
   prompt that does not carry it in writing is **non-compliant** even if nobody has pasted
   anything into it yet — the rule lives in the text of the prompt, not in the diligence of
   whoever fills it in.
7. **Free-text fields are the way back in, and must be governed first.** Entries such as
   *"values declared for this note"* or *"suspicions to be judged"* are points where the
   expected form comes back in without anyone having decided to let it. They must be bound to
   position and quantity in the text of the prompt itself, like everything else.
8. **Adoption is verified prompt by prompt.** The check is mechanical: open every
   verification prompt in force and look for the rule. As long as one prompt is uncovered,
   the decision is not applied, however well it is applied elsewhere.

## Consequences

- **What it solves:** it prevents the most insidious failure mode of gates — a channel that
  produces confirmations instead of checks, while staying green in the logs.
- **What it costs:** less targeted re-readings, hence more tokens and the occasional
  off-target verdict to relaunch. It is the same trade-off as
  [ADR-0005](0005-cost-is-intrinsic-to-quality.md): knowledge quality before token
  efficiency.
- **What it does NOT solve:** the anchoring of a role to **its own** previous reading (if it
  re-reads twice, the second is contaminated by the first) — that requires the separation
  into distinct roles of [ADR-0004](0004-chain-vs-single-prompt.md). And it does not solve
  false negatives: an unanchored verifier can still miss an error.
- **Why asking for distrust is not enough.** In the originating chain the safeguard already
  existed — as an **instruction**. The full-level prompt opens with *"do not trust the note
  or the extractor's report"*; the role's card prescribes transcribing **first** from the
  image and comparing **afterwards**, and ignoring the note's judgements until an autonomous
  conclusion has been reached. The anchoring happened anyway. An exhortation to distrust
  holds only while the information is not already in front of you: after that, asking not to
  use it is asking not to have read it. **The remedy is not to instruct distrust of the
  information: it is not to supply it.** This is why the decision is written as a constraint
  on the **text of the prompt** and not as a recommendation about conduct.
- **Residual risk to watch:** the rule is easy to break **in good faith**, because it is born
  of the legitimate desire to be precise and not to waste anyone's time. It must be verified
  on the **prompts**, not on intentions: the context you give to whoever verifies is exactly
  what stops being verified.
- **Residual risk, second kind — the partial fix:** a rule written on the link where the
  defect showed up, and not on the others, is more dangerous than no rule at all: it closes
  the case in the logs and leaves the defect in service. It is the second finding of the
  experiment above. Every time a rule of this family comes into force, the last step is not
  writing it — it is **enumerating the links and checking them all**.
- **When to revisit:** if it could be shown that a verification role **does not anchor** to
  information it is given — by measuring it, not assuming it — the constraint could be
  loosened for cases where the target is genuinely ambiguous.

## Related journal entry

[05 — The anchored reading](../../journal/05-the-anchored-reading.md)
