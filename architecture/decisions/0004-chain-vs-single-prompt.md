# ADR-0004 — A multi-agent chain, not a single prompt

**Status:** accepted

---

## Context

Extracting verifiable knowledge from technical PDFs could be done with **a single prompt**
on a capable model: “read the PDF, write the notes.” It is the simplest and cheapest path
in tokens — and the default of most tools.

## Hypothesis (what we believed possible)

That a capable enough model, in a single prompt, could **extract and self-check** to a
sufficient level.

## Experiment / reasoning

A single prompt has **one reading** of the page and **no independent second source** to
contradict it. Two *structural* failures follow, measured in the other ADRs:

- it does not see **silent formula errors** — the second reading from the image is needed
  ([ADR-0001](0001-formula-verification-from-image.md));
- under the obligation to judge, it **fabricates verdicts** on ambiguous evidence
  ([ADR-0002](0002-verdict-as-source-of-error.md)).

Neither is fixed by making the prompt “smarter”: what is missing is the **second source**
and **third-party separation**, not intelligence.

## Decision

The pipeline is a **chain of single-responsibility roles**, where whoever verifies did not
produce what they verify and does not see its reasoning. Independent verification is not a
stylistic choice: it is what a single prompt, **by construction**, cannot do.

## Consequences

- **What it solves:** catches errors a single prompt structurally misses.
- **What it costs:** more tokens and passes — the stated trade-off, and that cost is
  largely **intrinsic to quality** ([ADR-0005](0005-cost-is-intrinsic-to-quality.md)).
- **What it does NOT solve:** it does not make each role infallible; the safety net remains
  the two-level gate plus the adjudicator.
- **When to revisit:** if a single model could produce a second reading that is
  **independent, from a different source, in one pass** — hard by construction: it would
  still be one reading.
