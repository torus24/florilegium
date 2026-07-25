# Contributing to florilegium

Thanks for your interest. florilegium is, first, a **published methodology** — so the most
valuable contributions right now are ideas, critiques of the method, and reproductions,
not just code.

## Where the project is

See the [Roadmap](ROADMAP.md). Today the repository is at **M1 — the Story**: README,
architecture and decision records. The runnable engine, the generalized prompts and the
benchmarks arrive in later milestones.

## How to propose a change

1. Open an **issue** first to discuss anything non-trivial — especially changes to the
   method or the architecture.
2. For text and docs, small focused pull requests are easiest to review.
3. Explain the *why*, not only the *what*. This project values reasoning: a change to a
   decision should read like a short argument.

## Conventions

- **Bilingual docs.** English is the canonical version; the Italian mirror carries the
  `.it.md` suffix (e.g. `README.md` ↔ `README.it.md`). If you change one, note the other
  so they can be kept in sync.
- **Decisions go in ADRs.** A significant design choice is recorded in
  `architecture/decisions/` using the existing template: *Context · Hypothesis ·
  Experiment · Decision · Consequences*. An ADR can be `superseded` — that is normal.
- **Claims must be honest.** Numbers are labelled as directional evidence or as
  benchmarks; the two are not the same. Controlled benchmarks land in M4.

## Two hard rules

- **No source PDFs.** Source documents (papers, standards, books) are copyright and must
  never be committed. Examples use **only openly licensed** material (e.g. arXiv CC-BY, or
  a synthetic PDF).
- **No secrets or personal data.** No keys, tokens, absolute personal paths, or private
  configuration.

## License

By contributing you agree that your contributions are licensed under the project’s terms:
**[Apache-2.0](LICENSE)** for code, and **CC-BY-4.0** for documentation.
