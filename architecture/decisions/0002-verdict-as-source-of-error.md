# ADR-0002 — The mandatory verdict is itself a source of error

**Status:** accepted

---

## Context

In a quality gate it seems natural — and rigorous — to ask the verifying role for a
**clear-cut verdict** on every item: pass / fail, correct / typo. The intuition is “no
middle ground, decide.”

But forcing a **definitive verdict on EVERY item** has a non-obvious side effect: faced
with **ambiguous or insufficient** evidence, the role produces a verdict **anyway** —
because it was asked to. That verdict does not measure reality: it measures the
**pressure to decide**. That is how false confidence is manufactured.

This ADR is tightly linked to
[ADR-0001](0001-formula-verification-from-image.md): there, the mandatory “source typo”
verdict produced unfounded accusations; here we draw the general principle from it.

## Hypothesis (what we believed before)

That a **mandatory, binary** verdict made the gates stricter and more reliable — that
“forcing a decision” was the same as “deciding better.”

## Experiment (what we observed)

> **Real data**, from prior use of the pipeline that preceded this project, in generic
> form. Small sample → *directional* evidence, not a benchmark (that is M4).

Forcing the verifying role to emit a “source typo” verdict on contested formulas produced
a **high rate of unfounded accusations** (see
[ADR-0001](0001-formula-verification-from-image.md): **4 out of 5** were false alarms).
One case shows it starkly: the verification **fabricated** a typo, accusing an equation of
an error that used **symbols never printed** in that formula — a verdict produced by the
*pressure to decide*, not by the evidence. On ambiguous cases the mandatory verdict
skewed, **in every case observed**, toward the **stronger** decision (accuse the source)
rather than toward “I don’t know, more is needed.”

## Decision

1. **The verdict is evidence to be weighed, not absolute truth.** “The role expressed a
   judgment” and “the judgment is true” are two distinct things: the first does not imply
   the second.
2. **An outcome of “cannot determine → escalation” is allowed — and sometimes required —**
   instead of forcing a pass/fail on insufficient evidence.
3. **A high-impact verdict** (e.g. “the source is wrong”) **is not signable without
   stronger independent proof** — the high-resolution rendering of ADR-0001.
4. The gate is designed to **reward honest doubt**, not punish it: an escalation is not a
   failure of the role, it is the correct behaviour.

## Consequences

- **What it solves:** fewer false positives; ambiguities become **escalations** instead
  of wrong signed-off decisions.
- **What it costs:** it requires an **explicit escalation path** (process cost) and a gate
  level to catch it.
- **What it does NOT solve:** false negatives. A role can still *miss* a real error; for
  that the **two gate levels plus the adjudicator** (ADR-0001) remain — dropping the
  mandatory verdict is not enough on its own.
- **When to revisit:** if a way is found to **reliably calibrate the confidence** of a
  verdict, part of the escalation could be automated (this ADR would then become
  `superseded` or be refined).
