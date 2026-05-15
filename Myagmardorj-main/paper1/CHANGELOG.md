# Changelog

All notable changes to this project are documented here.
This project follows [Semantic Versioning](https://semver.org/).

---

## [v0.3] — 2026-05-09

### Scientific framing update
- `"verification"` → `"comparison"` throughout
- `"BK confirmed"` → `"BK-type agreement observed"`
- Explicit distinction between computational evidence and mathematical proof
- Normalization-selection caveat added explicitly to LIMITATIONS.md:
  *"The normalization was selected after observing weak low-T behavior,
  which introduces possible selection bias — a known confound."*
- Null hypothesis (H₀) stated explicitly in LIMITATIONS.md and RELEASE_NOTES

### Added
- `CITATION.cff` — GitHub automatic citation support
- `requirements.txt` at repository root
- `controls/07_negative_controls.py` — composite indices, random phases, GUE eigenvalue tests
- `controls/08_robustness_tests.py` — zero range, prime cutoff, normalization variants, random subsets
- `CHANGELOG.md` — this file
- Footer version string (`v0.3 · May 2026`) on all HTML pages
- MIT `LICENSE` at repository root (with author name)
- README: Zenodo badge, numerical limitations table, independent replication checklist

### Changed
- `RESULTS.md`: replaced "The BK amplitude law has been proved" bullet with positive statement "supported by numerical observations in this dataset"
- `index.html`: "Fixing this gave r = 0.6847 (zeros1)" → "Using the corrected normalization produced r = 0.6847 (zeros1) in this dataset"
- `index.html`: "Permutation test confirms the signal is genuine" → "did not reproduce the observed pattern, suggesting the signal is not an obvious statistical artifact"
- `index.html` (MN): `тоон нотолгоо` → `тооцооллын ажиглалт` throughout
- `03_BK_amplitude_test.py`: `MAYBE CONFIRMED` → `CONSISTENT WITH BK-TYPE SCALING`
- `landscape.html`: `$1,000,000 🎯` → `Clay Millennium Prize ($1,000,000)`
- `paper/main.tex`: expanded to full draft (Background, Method, Results, Limitations, Future Work, Reproducibility)

---

## [v0.2] — 2026-05-07

### Added
- `verify.html` — interactive correlation analysis tool
- `landscape.html` — Clay Prize and open problems context
- `intro.html` — research introduction page
- `LIMITATIONS.md` — 10-item caveat list
- `KNOWN_FAILURES.md` — normalization failure analysis
- `REPRODUCIBILITY.md` — step-by-step replication guide
- `controls/` directory with 6 null tests (shuffled, GUE, scaling, window, blind, bootstrap)
- `prime-locked-zeros/analyze.py` — standalone reproducible analysis

### Changed
- `verify.html`: fixed `<script src>` tag containing inline code (Plotly would not load)
- `index.html`: removed `BK confirmed!` code comment
- `index.html`: removed `or-val good` (green bold) styling from r = 0.6847 (zeros1) result row
- `index.html`: `BK Amplitude Law — Numerical Evidence` → `BK Amplitude Law — Computational Observation`
- `index.html`: `Numerical evidence` → `Computational observations consistent with BK-type scaling`
- `verify.html`: `Published v1` → `Reference result`
- All files: `Persistent prime-indexed excess observed` → `Prime-indexed excess patterns observed`
- All files: `verification lab` → `correlation analysis tool`

---

## [v0.1] — 2026-05-06  *(initial release)*

### Added
- Initial GitHub repository
- `index.html` — main research site
- `README.md` — project overview with results table
- `ABSTRACT.md` — research summary
- `METHODS.md` — mathematical definitions
- `zeta-zero-prime-frequency-analysis/` — full analysis code
  - `code/01_power_spectrum.py` through `04_null_tests.py`
  - `controls/01_shuffled_control.py` through `06_bootstrap.py`
  - `paper/main.tex` — initial LaTeX draft
- `RESULTS.md` — numerical results with caveats
- Zenodo DOI: `10.5281/zenodo.20077673`

---

## Planned: [v1.0] — target after independent replication

### Goals for stable release
- [ ] Independent replication confirmed (different machine/researcher)
- [ ] Bootstrap confidence intervals computed and documented
- [ ] Negative controls (Test 7) run on all three datasets
- [ ] Robustness tests (Test 8) run and summarised
- [ ] paper/main.tex compiled and uploaded to arXiv or Zenodo
- [ ] All HTML pages pass W3C validation
- [ ] Version number frozen — no result changes after v1.0 tag

> **Note:** v1.0 will be a frozen archive. Results will not change
> after the tag is applied. Any further analysis continues in v1.1+.
