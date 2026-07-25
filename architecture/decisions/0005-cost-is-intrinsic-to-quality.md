# ADR-0005 — The token cost is largely intrinsic to quality (a rejected optimization)

**Status:** accepted *(documents a **rejected** optimization proposal)*

---

## Context

The chain uses more tokens than a one-shot extraction, and that invites optimizations. A
concrete proposal: move the “rationale/record” part (the *why* of the rules, episodes,
deprecated rules) into **on-demand** files, to lighten the large upfront read that precedes
each batch of work.

## Hypothesis (what we believed)

That lightening that upfront read would cut a **significant share** of the cost.

## Experiment (the analysis that rejected it)

> **Real data**, from prior use of the pipeline that preceded this project, in generic,
> directional form.

- **Moves little.** Most of the “rationale” is actually **operational** (*which
  verification channel catches which error* is a “how”, not a “why”) and must stay. The
  real cut is **~10%**, not the hoped ~50%.
- **Targets the wrong cost.** What saturates work on a dense document is not the upfront
  read: it is the **per-note verification cost**, which **scales with the number of notes**
  and which the proposal does not touch. Lightening the upfront read bought **less than one
  extra note**.
- **No real simplification.** The moved material would still need a guard (it contains
  deprecated rules in imperative form) → just one more file.

## Decision

Optimization **rejected**. The token cost is **largely intrinsic to quality**: it comes
from **redundant multi-channel verification**, which is the value, not the waste. We do not
fight the trade-off the project is named after. The only change kept was one that
**increases reliability at higher cost** (a verification channel always attempted), not one
that saves.

## Consequences

- **What it says:** the pipeline operates **near its quality/cost frontier**; work spanning
  multiple sessions is **expected**, not inefficiency.
- **What it reinforces:** *knowledge quality over token efficiency*, with a concrete case.
- **Reusable lesson:** before optimizing, measure **which** cost dominates — often it is not
  the obvious one (here: per-note verification, not the upfront read).
- **When to revisit:** if the dominant cost changed (e.g. per-item verification became much
  cheaper), the analysis would need redoing.
