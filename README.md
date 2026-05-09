# Computational Investigation of Prime-Dependent Structures
in Unfolded Zeta Zero Statistics

**Status:** Exploratory experimental mathematics — not a confirmed result  
**DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20077673.svg)](https://zenodo.org/records/20077673)  
**Website:** [research.nexcore.ltd](https://research.nexcore.ltd)  
**License:** MIT  
**Version:** v0.3 · May 2026

---

## 1. Motivation

The Riemann zeta function encodes deep information about prime number distribution. Bogomolny & Keating (1996) predicted that GUE statistics of zeta zeros should receive prime-dependent corrections. This project investigates whether such corrections are numerically detectable in high-height zero blocks.

---

## 2. Background

- **Montgomery (1973):** Pair correlation of Riemann zeros follows GUE statistics
- **Bogomolny–Keating (1996):** Predicted prime-indexed amplitude corrections of the form A(p) ~ C(log p)²/p
- **This work:** Numerical study of whether such corrections appear in spacing covariance statistics

---

## 3. Mathematical Definitions

**Spacing covariance at lag h:**
```
C(h) = (1/N-h) Σ (δₙ - δ̄)(δₙ₊ₕ - δ̄)
```
where δₙ = γₙ₊₁ - γₙ are consecutive zero spacings.

**BK predictor:**
```
B(p) = (log p)² / p
```

**High-T unfolded normalization (critical):**
```
τ_p = log(p) / log(T / 2π)
```
Using log(p)/2π instead gives no signal (r ≈ 0.4–0.6).

---

## 4. Numerical Method

1. Load zero heights γₙ from Odlyzko tables
2. Compute spacings δₙ = γₙ₊₁ - γₙ and center them
3. For each prime p: compute covariance C(p) = mean(δₙ · δₙ₊ₚ)
4. Compute Pearson correlation between {C(p)} and {B(p)} across 12 primes
5. Run null controls (shuffled zeros, GUE surrogates)

---

## 5. Data Source

Odlyzko zero tables (University of Minnesota):
- **zeros2:** 100,000 zeros near T ≈ 74,920
- **zeros3:** ~10,000 zeros near T ~ 10¹²
- **zeros4:** ~10,000 zeros near T ~ 10¹³

Download: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

---

## 6. Results

Observed alignment with the first 12 expected prime-associated peaks
under the current normalization scheme (r values are naive estimates):

| Dataset | Height | Pearson r | p-value |
|---------|--------|-----------|---------|
| zeros2 | ~74,920 | 0.9783 | 3.82×10⁻¹⁸⁶ |
| zeros3 | ~10¹² | 0.9992 | 2.64×10⁻¹⁵ |
| zeros4 | ~10¹³ | 0.9421 | 5.0×10⁻⁶ |

Empirical agreement with BK-type amplitude scaling observed after normalization and residual extraction. The ratio R(p) = C(p)/B(p) ≈ 16.5 is approximately constant across primes (zeros3).

**Observed empirical agreement with BK-type amplitude scaling.**

> **Note on p-values:** The reported p-values assume independence of spacing covariances
> across prime lags. Autocorrelation in zero spacings, multiple testing (12 primes tested),
> and fitted normalization parameters reduce the effective degrees of freedom.
> Bootstrap confidence intervals and a formal null ensemble definition are needed
> before these p-values can be interpreted rigorously.

---

## 7. Controls / Null Models

| Control | Result | Interpretation |
|---------|--------|----------------|
| Shuffled zeros | r ≈ 0 | Signal is in ordering, not marginal distribution |
| Non-prime lags | mean ≈ 0 | Effect is prime-specific |
| Cross-dataset | r ≥ 0.94 (3 datasets) | Not height-specific artifact |

**Still needed:**
- GUE surrogate test (random matrix eigenvalues)
- Bootstrap confidence intervals
- Fake prime spectrum (composite numbers only)
- Scaling law with N

---

## 8. Limitations

- High correlation (r ≈ 0.9992 (naive estimate, see RESULTS.md)) alone is insufficient — normalization artifacts, overfitting (12 data points), window bias, hidden dependence, and finite-size effects have not been fully ruled out
- C ≈ 16.5 has no theoretical derivation
- Independent peer replication has not been done
- This is **not** a confirmed theorem
- This is **not** a proof of the Riemann Hypothesis

---

## 9. Future Work

| Priority | Task |
|----------|------|
| High | GUE surrogate + bootstrap significance tests |
| High | Scaling law: how does r behave as N → ∞? |
| High | Independent replication by another researcher |
| Medium | Derive C ≈ 16.5 from explicit formula |
| Medium | Submit to Experimental Mathematics journal |
| Low | Test on zeros at T ~ 10²¹ |

---

## 10. References

- E. B. Bogomolny & J. P. Keating (1996). Random matrix theory and the Riemann zeros. *Nonlinearity*
- H. L. Montgomery (1973). The pair correlation of zeros of the zeta function. *Proc. Sympos. Pure Math.* 24
- A. M. Odlyzko (1992). The 10²⁰-th zero of the Riemann zeta function
- G. A. Hiary & A. M. Odlyzko (2012). arXiv:1105.4312

---

## Reproducibility

```bash
# Clone the repository
git clone https://github.com/myagmardorj-cloud/Myagmardorj
cd Myagmardorj

# Install dependencies
pip install -r zeta-zero-prime-frequency-analysis/requirements.txt

# Run main analysis
cd prime-locked-zeros
python analyze.py
# Expected output: r value, p-value, scatter plot

# Run null controls
cd ../zeta-zero-prime-frequency-analysis/controls
python run_all.py
# Expected output: shuffled r ≈ 0, GUE baseline comparison

# Run BK amplitude test
cd ../code
python 03_BK_amplitude_test.py
# Expected output: CONSISTENT WITH BK-TYPE SCALING (if r ≥ 0.8)
```

All results should be reproducible given the same Odlyzko zero files.  
See `data/README.md` for data download instructions.

---

## Citation

```bibtex
@misc{namnansuren2026prime,
  author    = {Namnansuren, Myagmardorj},
  title     = {Prime-Indexed Excess in High Riemann Zero Spacing Statistics},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673},
  url       = {https://zenodo.org/records/20077673}
}
```

---

*Myagmardorj Namnansuren · Nexcore LTD · Ulaanbaatar, Mongolia · 2026*

> "Interesting experimental mathematics result — not a confirmed theorem, but not mere fantasy either."
