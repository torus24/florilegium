# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to
[Semantic Versioning](https://semver.org).

This file is kept in English only — see the bilingual policy in
[CONTRIBUTING](CONTRIBUTING.md).

## [0.1.0] — 2026-07-26 — M1, the Story

First public release. The repository publishes the **method**, not yet the engine.

### Added

- README (EN + IT): the problem, the hero feature, the architecture, the limitations and
  the roadmap.
- `architecture/`: overview, roles and quality gates, each with an Italian mirror.
- Six Architecture Decision Records (ADR-0001 … ADR-0006), EN + IT, all `accepted`.
- `journal/`: five entries recording the failures the decisions were paid for, EN + IT,
  with an index.
- `examples/01`: a worked example — a formula the text layer silently broke —
  reproducible by hand with `poppler-utils` on an openly licensed paper (CC-BY 4.0). No
  source PDF is committed.
- `scripts/compare_readings.py` — the smallest runnable demonstration of one
  gate. It renders the page, reads the text layer, re-transcribes the formula from the
  image alone and prints the differences between the two readings. It stops at the
  differences: it issues no verdict. Default backend is a local Claude Code install (no
  API key); an API backend is available as a declared alternative.
- `LICENSE` (Apache-2.0), `LICENSES/CC-BY-4.0.txt`, `CITATION.cff`, `ROADMAP` and
  `CONTRIBUTING` (both EN + IT).
- The `ROADMAP` describes **states, not commitments**: florilegium documents a method its
  author uses in another project, so what ships is what was already written in order to
  work. No v1.0 is planned, and the roadmap says in as many words what it does not
  promise.
