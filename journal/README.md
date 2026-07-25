# Journal — field notes

An ADR records a **decision**: context, hypothesis, measurement, consequence. A journal
entry records the **episode that forced it** — what went wrong, how it was found, and often
how close it came to never being found at all.

| # | Entry | What happened | Decision it fed |
|---|---|---|---|
| 01 | [The typo that was not there](01-the-typo-that-was-not-there.md) | Four accusations against the source out of five were false — and the fourth surfaced by accident, with nobody suspecting anything | [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.md) |
| 02 | [The silent corrector](02-the-silent-corrector.md) | Three undeclared “corrections” to a source: fidelity is not correctness | [ADR-0002](../architecture/decisions/0002-verdict-as-source-of-error.md) |
| 03 | [The third channel](03-the-third-channel.md) | Two channels agreed on the same error — and a channel declared dead proved decisive three times out of three | [ADR-0001](../architecture/decisions/0001-formula-verification-from-image.md) · [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.md) |
| 04 | [When the chain stops itself](04-when-the-chain-stops-itself.md) | The ceiling is a shutdown, not a quota: no unit left half-done | [ADR-0005](../architecture/decisions/0005-cost-is-intrinsic-to-quality.md) |
| 05 | [The anchored reading](05-the-anchored-reading.md) | The expected string, pasted into the re-reader’s own instructions | [ADR-0006](../architecture/decisions/0006-reader-must-not-know-the-expected-answer.md) |

These are written after the fact and kept honest, including where the method was wrong
first and right later. The data comes from use of the pipeline that preceded this project,
reported in generic form.

---

*See also: [architecture/overview](../architecture/overview.md) for how these rules ended up
in the design.*
