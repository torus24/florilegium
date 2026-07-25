# Roadmap

florilegium is released **in layers**. Each milestone has a publishable deliverable and a
**definition of done** (DoD): the next one does not start until the DoD is green. This is
deliberate — the value here is the method and the decisions, so the *story* ships before
the *code*.

---

## M1 — The Story  ·  *shipped — this repository*

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

## M1.5 — The First Loop  ·  *planned*

The smallest thing that runs: a short script that automates example 01 — render the
page as an image, re-transcribe the formulas from it, compare the two readings, print
the differences. No orchestrator, no gates, no configuration.

**DoD:** a user runs the script on example 01 and the loop reproduces, on its own, the
discrepancies the example documents by hand.

## M2 — The Engine & the Gates  ·  *planned*

Make the project runnable in its useful-but-hard-to-copy core. *(Former M2 and M3,
merged: an orchestrator without the role prompts is scaffolding, not a pipeline — they
ship together. M4 keeps its number.)*

- The orchestrator, batching and session management.
- The generalized role prompts (director / librarian / pre-gate operator /
  re-transcriber / verifier).
- The operational configuration of the gates: escalation triggers, the channels required
  per note type, the quarantine policy.
- `config/config.example.yaml`, installation and getting-started docs.

**DoD:** a Linux user runs the pipeline on an example PDF by following the
getting-started guide, and the gates produce a reproducible quality report.

## M4 — Benchmarks & v1.0  ·  *planned*

The data that shows the value is the *process*, not the model.

- `benchmark/`: single-prompt vs. chain; OCR robustness; cost/token;
  [note density](journal/04-when-the-chain-stops-itself.md) — with
  reproducible data.
- Tests (unit + functional + regression), CI.
- Tag **v1.0.0**, complete `CHANGELOG.md`.

**DoD:** the benchmarks are reproducible from the repository; CI is green; the README
points to the results.

---

## Versioning

Versions follow [SemVer](https://semver.org). While the engine is not there yet, the
project stays in **0.x**: each milestone gets its own minor tag — `v0.1.0` for M1,
`v0.2.0` for M1.5, and so on — and `v1.0.0` arrives with M4, together with the
benchmarks. Every tag is a GitHub Release, and [`CHANGELOG.md`](CHANGELOG.md) records
what changed.

---

*Milestones describe intent, not dates. Decisions that turn out wrong are revised in the
open — ADRs can be marked `superseded`.*
