## Quick Reproduction


## Current Observed Correlations

| Dataset | N | r | Bootstrap | Verdict |
|---------|---|---|-----------|---------|
| zeros1 | 100K | 0.6847 | 0.36 ± 0.26 | UNSTABLE |
| zeros_ht | 10K | 0.5113 | 0.09 ± 0.30 | UNSTABLE |
| zeros6 | 2M | 0.4509 | 0.68 ± 0.09 | MODERATE |

Bootstrap analysis suggests only limited stability for zeros6.
Earlier higher correlations (r = 0.6847 (zeros1) (earlier result — not reproduced across tested datasets)) were not robust under independent replication.
C estimates near 3 in zeros1/zeros6, but not stable across all datasets.

```bash
git clone https://github.com/myagmardorj-cloud/Myagmardorj
cd Myagmardorj
pip install -r requirements.txt
python scripts/analyze.py zeros_ht.txt
```

**Note:** zeros_ht.txt must be downloaded separately from:
http://www-users.cse.umn.edu/~odlyzko/zeta_tables/
(Zeros number 10^12+1 through 10^12+10^4)

**Expected result:** r ≈ 0.51 (independent replication)
Original claimed r = 0.45–0.68 (dataset-dependent) has not been reproduced.

# Prime-Indexed Excess in Riemann Zero Spacing Covariance

> **This repository presents exploratory computational experiments and does not claim a proof of the Riemann Hypothesis.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20077673.svg)](https://zenodo.org/records/20077673)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.3-green.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-computational%20observation-orange.svg)](docs/LIMITATIONS.md)

> **What this is:** A computational observation of prime-indexed structure in high Riemann zero statistics, empirically consistent with Bogomolny–Keating (1996) predictions.  
> **What this is NOT:** A proof of the Riemann Hypothesis. Not a confirmed theorem. Not peer-reviewed.  
> **Reproducibility:** `pip install -r requirements.txt && python scripts/analyze.py zeros1.txt`  
> **Limitations:** Normalization selection bias, n=12 data points, no asymptotic analysis. See [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md).

---

## Latest Update (v0.3 — May 2026)

Repository updated with more conservative scientific framing.

**Main changes:**
- `"verification"` → `"comparison"`
- `"BK confirmed"` → `"BK-type agreement observed"`
- Explicit distinction between computational evidence and proof
- Robustness and null-control structure expanded (8 tests)
- Normalization-selection caveat documented explicitly

**Important limitation:**
> The normalization procedure (`τ_p = log(p)/log(T/2π)`) was selected
> after observing weak low-T results. This introduces potential selection
> bias and should be treated as a known confound requiring independent replication.

**Reproduce:**
```bash
python scripts/run_all.py zeros1.txt
```

---



```
/
├── scripts/          ← analysis code (analyze.py, BK test, null tests)
├── controls/         ← 8 null and robustness tests
├── paper/            ← LaTeX draft + flagship figure generator
├── docs/             ← RESULTS, LIMITATIONS, METHODS, REPRODUCIBILITY
├── data_v1/          ← frozen prime list + zero file instructions
├── .github/          ← issue/discussion templates
├── *.html            ← research website (research.nexcore.ltd)
├── CHANGELOG.md
├── CITATION.cff
└── requirements.txt
```

---

## Quick Start

```bash
git clone https://github.com/myagmardorj-cloud/Myagmardorj
cd Myagmardorj
pip install -r requirements.txt

# Download zero data from Odlyzko:
# http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

python scripts/analyze.py zeros1.txt
# Expected: r = 0.6847 (zeros1) (earlier result — not reproduced across tested datasets), naive p = 2.64e-15 (uncorrected — see Limitations)
```

---

## Main Result

Pearson correlation between empirical spacing covariance A(p) and
BK predictor B(p) = (log p)²/p across 12 primes on three datasets:

| Dataset | Height T  | Pearson r | Naive p-value†  |
|---------|-----------|-----------|-----------------|
| zeros_ht  | ~74,920   | 0.5113    | —               |
| zeros1  | ~10¹²     | **0.6847**              | —               |
| zeros6  | ~10¹³     | 0.4509    | —               |

†Naive p-values assume independence. Effective DOF < 12 due to
autocorrelation. Not corrected for multiple testing. See
[`docs/LIMITATIONS.md`](docs/LIMITATIONS.md) for full caveat list.

Null controls (shuffled zeros, GUE surrogates, composite-lag indices)
produce r ≈ 0 — see `controls/07_negative_controls.py`.

---

## Key Limitations

1. **Normalization selection bias** — high-T formula chosen after low-T gave r ≈ 0.4
2. **Small n = 12** — Pearson r with 12 points is sensitive to outliers
3. **Autocorrelation** — consecutive covariances not independent; effective DOF < 12
4. **No asymptotic analysis** — r behavior as N → ∞ is unknown
5. **Not independently replicated** — results not yet reproduced on a separate machine

Full list: [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md)

---

## Controls

| # | Test | Result |
|---|------|--------|
| 01 | Shuffled zeros | r ≈ 0 — signal in ordering |
| 02 | GUE surrogates | r ≈ 0 — exceeds GUE baseline |
| 03 | Scaling law (N) | r stable — not obvious finite artifact |
| 04 | Window types | r stable — not Fourier leakage |
| 05 | Blind detection | Peaks cluster near primes |
| 06 | Bootstrap CI | Corrected intervals available |
| 07 | Negative controls | Composite lags, random phases → r ≈ 0 |
| 08 | Robustness | Zero range, prime cutoff, norm variants |

---

## Numerical Limitations Summary

| Issue | Detail |
|-------|--------|
| Selection bias | Normalization chosen after observing weak low-T result |
| Sample size | Only 12 prime lags (n=12) |
| Autocorrelation | Effective DOF < 12; naive p-values unreliable |
| Multiple testing | 12 lags, no Bonferroni correction |
| Finite window | Spectral leakage not fully excluded |
| Asymptotics | r behavior as N→∞ unknown |
| No derivation | Empirical constant C estimates near 3 in zeros1/zeros6, but not stable across all datasets. has no theoretical explanation |
| No independent replication | No independent reproduction yet |

---

## Independent Replication Checklist

```bash
# Run on your machine, compare outputs:
python scripts/analyze.py zeros1.txt
```

| Check | Expected | Notes |
|-------|----------|-------|
| r (zeros1) | 0.6847 | Bootstrap UNSTABLE; replication needed |
| Shuffled r | ≈ 0.0 ± 0.2 | Run controls/01 |
| GUE r | ≈ 0.0 ± 0.2 | Run controls/02 |
| Prime excess visible | Yes | 12/12 primes |

→ Replication attempt? Open a [Discussion](../../discussions).

---

## Paper

LaTeX draft: [`paper/main.tex`](paper/main.tex)  
Flagship figure: [`paper/generate_flagship_figure.py`](paper/generate_flagship_figure.py)  
arXiv draft: [`docs/ARXIV_DRAFT.md`](docs/ARXIV_DRAFT.md)

---

## GitHub Topics

<!-- Add these in Settings → Topics -->
`riemann-hypothesis` · `computational-number-theory` · `experimental-mathematics` · `prime-numbers` · `zeta-function` · `bogomolny-keating` · `pair-correlation` · `gue-statistics`

---

## Citation

```bibtex
@misc{namnansuren2026prime,
  author    = {Namnansuren, Myagmardorj},
  title     = {Prime-Indexed Excess in Riemann Zero Spacing Covariance},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673},
  url       = {https://zenodo.org/records/20077673}
}
```

---

## References

- E. B. Bogomolny & J. P. Keating (1996). *Nonlinearity* 8–9.
- H. L. Montgomery (1973). *Proc. Sympos. Pure Math.* 24.
- A. M. Odlyzko. Zero tables. http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

---

*Myagmardorj Namnansuren · Nexcore LTD · Ulaanbaatar, Mongolia · 2026*  
*Experimental numerical study — not a confirmed theorem, not a proof of RH*

## How to Cite

```bibtex
@software{myagmardorj2026,
  author    = {Myagmardorj Namnansuren},
  title     = {Prime-Indexed Excess in High Riemann Zero Spacing Covariance},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673},
  url       = {https://github.com/myagmardorj-cloud/Myagmardorj}
}
```

## Expected Runtime

```
python scripts/analyze.py zeros_ht.txt  →  ~10 seconds
python controls/run_all.py              →  ~3 minutes
```

## Dataset Checksums
zeros_ht.txt SHA256: E7B9FD20B4755234B017167696F18A9C319070453DC175BA58D0FA7345FE3D21
