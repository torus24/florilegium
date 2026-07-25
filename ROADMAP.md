# Roadmap

florilegium is released **in layers**. Each milestone has a publishable deliverable and a
**definition of done** (DoD): the next one does not start until the DoD is green. This is
deliberate — the value here is the method and the decisions, so the *story* ships before
the *code*.

---

## M1 — The Story  ·  *in progress*

A repository that **explains** the project, without runnable code yet.

- README (the problem, why it is different, the architecture).
- `architecture/` — overview, roles, quality gates, with a diagram.
- Architecture Decision Records (ADRs) — the strong decisions, with numbers where available.
- A few `journal/` entries.
- **One** worked example in `examples/` with an open-licensed input.
- `LICENSE`, `ROADMAP.md`, `CONTRIBUTING.md`.

**DoD:** a stranger, reading only the README + architecture + one ADR, understands the
*problem*, the *originality*, and *why this author designed it*. The example is
reproducible by hand.

## M2 — The Engine  ·  *planned*

Make the project runnable in its useful-but-hard-to-copy core.

- The orchestrator, batching and session management.
- `config/config.example.yaml`, installation and getting-started docs.

**DoD:** a Linux user runs the pipeline on an example PDF by following the getting-started
guide, without further help.

## M3 — The Gates  ·  *planned*

The methodologically original part, in runnable form. The *method* is already published at
M1 (see `architecture/` and the ADRs); what M3 adds is the machinery that executes it.

- The generalized role prompts (director / librarian / pre-gate operator /
  re-transcriber / verifier).
- The operational configuration of the gates: escalation triggers, the channels required
  per note type, the quarantine policy.

**DoD:** the gates run on the example and produce a reproducible quality report.

## M4 — Benchmarks & v1.0  ·  *planned*

The data that shows the value is the *process*, not the model.

- `benchmark/`: single-prompt vs. chain; OCR robustness; cost/token; note density — with
  reproducible data.
- Tests (unit + functional + regression), CI.
- Tag **v1.0.0**, complete `CHANGELOG.md`.

**DoD:** the benchmarks are reproducible from the repository; CI is green; the README
points to the results.

---

*Milestones describe intent, not dates. Decisions that turn out wrong are revised in the
open — ADRs can be marked `superseded`.*
