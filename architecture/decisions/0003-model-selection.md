# ADR-0003 — One model per role: the strong one where you judge, the cheap one where you execute

**Status:** accepted

---

## Context

The pipeline uses several language models. The natural temptation — to contain cost — is
to use **one cheap model everywhere**. But the roles are not equal: some **extract and
judge** (accuracy matters), others do **mechanical work** (run a script, report an
output). Assigning the same model to all of them wastes money where it is not needed and
gets it wrong where it is.

## Hypothesis (what we believed before)

That a **mid-tier** model could handle extraction too, cutting cost without losing
quality; and that for mechanical tasks the **cheapest** model would always be enough.

## Experiment (what we measured)

> **Real data**, from prior use of the pipeline that preceded this project, rewritten in
> generic form. In the reference implementation the models are of the Claude family (see
> the README, *Status & implementation*). **Small sample → directional evidence, not a
> benchmark** (that is M4). Stated caveat: the baseline was collected partly under a
> different gate regime ⇒ it is **not a fully controlled A/B**.

**What counts as a substantial error.** Errors are counted **by class**, and *substantial*
is a precise one: a **substantially wrong transcription** — a symbol, subscript, exponent,
operator, sign, unit or numeric value that, taken as written, would make a downstream
calculation give a different result. The test is operational: **if a script consuming the
note would produce a different number, the error is substantial.** Counted **separately**,
and not included in the figures below: **false source typos** (accusing the source of an
error it does not print), **silent corrections** and altered verbatim, wrong **page or
figure attributions**, and reporting slips. They are separate classes because they fail in
different ways and are prevented by different safeguards — not because they matter less.

- **Extraction with the strong model (Opus) — baseline:** **≈ 0.163 substantial errors
  per note** (8 substantial errors across 49 notes, 3 articles).
- **Extraction with a mid-tier model (Sonnet), one article:** **≈ 0.50 substantial errors
  per note** (~3× worse). On top of that, the **base gate failed to catch 2 serious
  errors**, and a **fabricated source typo** slipped through (caught only by the full
  gate).
- **Back to the strong model, next article:** **≈ 0.00**.
- **On a purely mechanical role** (run a script and report the output verbatim), the
  **cheapest model (Haiku) failed twice** — it *interpreted* instead of *executing* — and
  was moved up a tier.

## Decision

1. **Strong model where you extract and where you judge at the full level** (extraction,
   verification from the image).
2. **Mid-tier model where you re-read without emitting a verdict** (base gate) and where
   the task is a repeatable craft.
3. **Not “the cheapest everywhere”:** even a mechanical task needs a model that knows how
   *not* to interpret — a rule drawn from **two observed failures**, not from a
   measurement.
4. Each role’s model is **fixed in its own card**, independent of the model the session
   runs on.

**Assignment in the reference implementation (Claude):** extraction = Opus · full-level
verification = Opus · base-level re-transcription = Sonnet (no verdict) · mechanical
pre-gate operator = Sonnet (raised from Haiku).

## Consequences

- **What it solves:** cost spent where it pays off (judgment), saved where it is not
  needed (base reading, mechanical work).
- **What it is NOT:** a benchmark. The numbers are **directional** and must be reconfirmed
  under controlled conditions (M4).
- **What it does NOT solve:** it does not eliminate errors; it moves them onto the right
  model for each role. The safety net remains the two-level gate plus the adjudicator
  (ADR-0001).
- **When to revisit:** the ADR fixes the **criterion** (“the strong one where you judge”),
  not the model *names*. If a future cheap model matched the strong one on extraction, the
  assignment changes without touching the criterion.
