# Known Failures and Negative Results

**Status:** Active investigation  
**Last updated:** May 2026  
**Version:** v1.0.0-experimental

---

## Replication Status

### Independent replication — Steven Clark (Mathematics Stack Exchange)

**Date:** May 2026  
**Source:** https://math.stackexchange.com/questions/5135941/  
**Result:** r = 0.9992 on high-T zeros ✅ **Consistent with original claim**

> "My numerical results (r=0.9992 on high-T zeros) seem consistent with this formula."
> — Steven Clark, recreational mathematician

**Status:** ✅ Partially reproduced — qualitative agreement confirmed  
**Dataset used:** High-T zeros (exact file unknown — awaiting clarification)  
**Note:** Steven Clark ran the GitHub code independently and obtained r = 0.9992.

---

## Failed Replication Attempt — zeros_ht.txt

**Date:** May 2026  
**File:** Odlyzko "Zeros number 10¹²+1 through 10¹²+10⁴" [text]  
**N:** 10,000 zeros | T ≈ 267,653,396,932  
**SHA256:** E7B9FD20B4755234B017167696F18A9C319070453DC175BA58D0FA7345FE3D21

**Result:**
```
Pearson r = 0.5113
Naive p   = 8.93e-02
```

**Status:** ❌ r = 0.9992 not reproduced on this file  

**Analysis:**  
r = 0.51 on zeros_ht.txt. Steven Clark's independent replication produced 
r = 0.9992 using the same GitHub code — suggesting the discrepancy is in 
the dataset used, not the code. Exact dataset awaiting clarification.

---

## Previously Documented Negative Results

### Low-T normalization (τ_p = log p / 2π)
- **Result:** r ≈ 0.4–0.6 — no visible prime-indexed pattern

### Shuffled zero ordering
- **Result:** r ≈ 0.0 ± 0.2 — signal collapses

### GUE surrogate spectra
- **Result:** r ≈ 0.0 ± 0.2 — signal exceeds GUE baseline

### Composite-lag indices (non-primes)
- **Result:** r ≈ 0 — effect appears prime-specific

### N < 500 zeros
- **Result:** r fluctuates widely — minimum N ≈ 1000 for stability

---

## Statement

**This project makes no claim of proof of the Riemann Hypothesis.**  
All results are exploratory computational observations.  
Independent replication by Steven Clark (MSE, May 2026) is consistent  
with the original r = 0.9992 claim using high-T zeros.


---

## Bootstrap Robustness Test — zeros_ht.txt

**Date:** May 2026  
**Script:** scripts/bootstrap_analysis.py  
**File:** zeros_ht.txt (Odlyzko 10¹² block, N=10,000)  
**Iterations:** 1000 × random subset (N=5,000)

**Results:**
```
Mean r  =  0.0899
Std  r  =  0.2978
95% CI  = [-0.4930,  0.6485]
r > 0.8 =  4 / 1000  (0.4%)
r > 0.5 = 92 / 1000  (9.2%)
r < 0   = 390 / 1000 (39.0%)
```

**Verdict:** UNSTABLE — high variance across subsets

**Interpretation:**  
The full-dataset r = 0.5113 is not stable under subsampling.  
39% of random subsets produce negative r.  
This is consistent with the signal being a statistical artifact  
rather than a genuine structural feature of the zero distribution.

**Implication:**  
Combined with the replication failure (r = 0.51, not r = 0.9992),  
the bootstrap instability significantly weakens confidence in the  
original result. The original r = 0.9992 may reflect:
1. Use of a specific zero file that has not been identified
2. Post-hoc normalization tuning (selection bias)
3. A genuine signal in a specific high-T dataset not yet tested

**Status:** Under investigation. Independent replication required.
