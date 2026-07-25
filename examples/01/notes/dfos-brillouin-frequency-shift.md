---
title: "Brillouin frequency shift — strain and temperature relation (DFOS)"
source_doi: "10.1016/j.jrmge.2024.01.008"
source_title: "Distributed fiber optic sensors for tunnel monitoring: A state-of-the-art review"
source_authors: "Zhang, X. et al."
source_year: 2024
source_license: "CC-BY-4.0"
locator: "§2.1, Eq. (1)"
page_pdf: 2
page_printed: 3842
page_note: "final published version (23 pages); in the earlier corrected proof §2.1 sits on PDF page 3 — locate by §2.1, not by page"
status: verified
verified_by:
  - channel: text-layer
    outcome: discrepant
  - channel: image-400dpi
    outcome: authoritative
  - channel: source-internal-arithmetic
    outcome: confirming
tags: [dfos, brillouin, fiber-optic, strain, temperature]
---

# Brillouin frequency shift — strain and temperature relation

The Brillouin frequency shift (BFS) in an optical fiber varies linearly with the strain and
the temperature applied to the fiber, measured against a reference state:

$$\nu(T, \varepsilon) = C_\varepsilon (\varepsilon - \varepsilon_0) + C_T (T - T_0) + \nu_0(T_0, \varepsilon_0)$$

## Symbols

| Symbol | Meaning |
|---|---|
| `ν(T, ε)` | BFS at temperature `T` and strain `ε` |
| `C_ε` | strain sensitivity coefficient |
| `C_T` | temperature sensitivity coefficient |
| `ν₀(T₀, ε₀)` | baseline BFS at reference temperature `T₀` and reference strain `ε₀` |

## Conditions of use

- The relation is **relative to a reference state**. A BFS reading is meaningless without the
  baseline `ν₀` and the `(T₀, ε₀)` it was taken at.
- Strain and temperature are **coupled** in a single measured quantity: one BFS reading
  cannot separate them. Decoupling requires a second, independent measurement — typically a
  strain-free fiber run for temperature compensation.
- `C_ε` and `C_T` are properties of the specific fiber and interrogator; they are calibrated,
  not assumed.

## Verification record

- **Text layer** — *discrepant.* Extraction produced
  `nðT; εÞ ¼ Cε ðε  ε0 Þ þ CT ðT  T0 Þ þ n0 ðT0 ; ε0 Þ`. Beyond the obvious font-encoding
  noise (`ð` `Þ` `¼` `þ`), **both subtraction operators were absent** and `ν` was rendered as
  a Latin `n`.
- **Image at 400 dpi** — *authoritative.* Both minus signs and the Greek `ν` are unambiguous
  in the print.
- **Source-internal arithmetic** — *confirming, independently.* The article defines `ν₀` as
  the baseline at `(T₀, ε₀)`. Setting `T = T₀` and `ε = ε₀` must therefore yield `ν = ν₀`,
  which requires the first two terms to vanish at the reference point — possible only if they
  are differences. A product or a sum would contradict the article's own definition of `ν₀`.
- **Dimensional check** — every term is a frequency, so `C_ε` is Hz per unit strain and `C_T`
  is Hz per degree, matching the definitions given in the text.

*Walkthrough: [../README.md](../README.md). Source used under
[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
