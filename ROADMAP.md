# Roadmap

🇮🇹 *Questa pagina è disponibile anche in [italiano](ROADMAP.it.md).*

florilegium documents a method the author **actually uses**, in another project. It is not
developed as a product: there are no development commitments here, no dates, and no
promised v1.0. One rule holds — **what ships is what was already written in order to
work**, not what would have to be built for the sake of the repository.

The milestones below therefore describe *states*, not a work plan.

---

## M1 — The Story  ·  *shipped — this repository*

A repository that **explains** the project.

- README (the problem, why it is different, the architecture).
- `architecture/` — overview, roles, quality gates, with a diagram.
- Architecture Decision Records (ADRs) — the strong decisions, with numbers where available.
- A few `journal/` entries.
- **One** worked example in `examples/` with an open-licensed input.
- `LICENSE`, `ROADMAP.md`, `CONTRIBUTING.md`.
- **A script that runs the example** — `scripts/compare_readings.py`: it renders the page
  as an image, re-transcribes the formula from it, compares the two readings, prints the
  differences. A demonstration of **one** gate, not the engine.

**State reached:** a stranger, reading only the README + architecture + one ADR,
understands the *problem*, the *originality*, and *why this author designed it that way*.
The example is reproducible by hand, and the script reproduces on its own the discrepancies
the example documents.

## M2 — The Chain  ·  *when it has been cleaned up*

The chain that already runs, published **as it is**: generalized and stripped of the
private domain it comes from, not rewritten for an imaginary audience.

- The real role cards (director / librarian / pre-gate operator / re-transcriber /
  verifier), generalized.
- The gate protocol and its operational configuration: escalation triggers, the channels
  required per note type, the quarantine policy.
- The deterministic core — whatever must never be a model's opinion: a minimum rendering
  resolution enforced by the program, structural comparison, the mechanical pre-gate, the
  signature trail. A few hundred lines, not a framework.
- How to install it and what it takes to run it.

**State reached:** anyone with the same environment — an agentic host that runs sub-agents
with isolated context, `poppler-utils`, a multimodal model — runs it. The limit is stated
plainly: **this is not a package installable everywhere, and it does not promise to
become one.**

## M4 — The Evidence  ·  *no date*

The numbers that show the value is the *process*, not the model. With one constraint this
repository cannot work around: **the sources the chain actually works on are
copyrighted, and will never be committed here.**

- **Aggregate measurements** collected on the author's real corpus: how many formulas the
  text layer corrupts, how many the chain catches, how many false alarms — with the
  measurement methodology described and the sources *not* published. This is
  **directional** evidence, not reproducible by third parties, and the repository says so
  every time.
- **If** and **when** part of the material is openly licensed: a *conformance fixture* — a
  few pages, known corruptions, an expected outcome — that anyone can re-run. It is the
  only genuinely reproducible benchmark this project can produce.

**State reached:** every published number states how it was collected and what it does
**not** prove.

---

## What this roadmap does not promise

To be fair to the reader: there will be no package installable on any system, no continuous
integration, no multi-provider support verified across hosts, and no controlled benchmarks
comparing models. Not because those have no value, but because they are product work, and
this repository is not a product. If they ever arrive, it will be because the author needed
them for his own work — not because they were promised.

---

## Versioning

Versions follow [SemVer](https://semver.org). The project stays in **0.x**: each milestone
gets its own minor tag — `v0.1.0` for M1, `v0.2.0` for M2 — and **no v1.0 is planned**.
Every tag is a GitHub Release, and [`CHANGELOG.md`](CHANGELOG.md) records what changed.

---

*Milestones describe states, not dates. Decisions that turn out wrong are revised in the
open — ADRs can be marked `superseded`.*
