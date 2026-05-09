# Known Failures and Negative Results

**Status:** Active investigation  
**Last updated:** May 2026  
**Version:** v1.0.0-experimental

---

## Critical: Independent Replication Failure

### Attempt 1 — zeros_ht.txt (Odlyzko 10¹² block)

**Date:** May 2026  
**File:** Odlyzko "Zeros number 10¹²+1 through 10¹²+10⁴" [text]  
**N:** 10,000 zeros | T ≈ 267,653,396,932

**Result:**
```
Pearson r = 0.5113
Naive p   = 8.93e-02
```

**Expected (original claim):** r ≈ 0.9992

**Status:** ❌ Not reproduced

**Analysis:**  
Independent replication on the Odlyzko 10¹² zero block produced 
r = 0.51, not r = 0.9992 as originally reported. Both raw and 
high-T unfolded normalizations were tested. Neither reproduced 
the original result.

**Implications:**  
This failure is consistent with the selection bias warning stated 
in LIMITATIONS.md: the high-T normalization was selected after 
observing weak low-T results. The original r = 0.9992 may reflect 
normalization tuning rather than a genuine signal.

**Next steps:**
1. Locate and re-run the exact original code version that produced r = 0.9992
2. Identify which normalization and dataset block was used originally
3. Test whether r = 0.9992 was specific to one particular parameter choice
4. Update paper/main.tex to reflect this replication failure

---

## Previously Documented Negative Results

### Low-T normalization (τ_p = log p / 2π)
- **Result:** r ≈ 0.4–0.6
- **Interpretation:** Normalization physically incorrect at high T

### Shuffled zero ordering
- **Result:** r ≈ 0.0 ± 0.2
- **Interpretation:** Signal depends on zero ordering

### GUE surrogate spectra
- **Result:** r ≈ 0.0 ± 0.2
- **Interpretation:** Signal exceeds pure GUE baseline

### Composite-lag indices (non-primes)
- **Result:** r ≈ 0
- **Interpretation:** Effect appears prime-specific

### N < 500 zeros
- **Result:** r fluctuates widely
- **Interpretation:** Minimum N ≈ 1000 for stability

---

## Statement

These failures do not invalidate the computational observation —  
they are essential scientific context. A result that cannot be  
independently reproduced should not be treated as established.

**This project makes no claim of proof of the Riemann Hypothesis.**  
All results are exploratory computational observations requiring  
further investigation.

