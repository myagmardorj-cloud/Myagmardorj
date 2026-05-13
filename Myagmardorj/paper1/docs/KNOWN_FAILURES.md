# Known Failures and Negative Results

**Status:** Active investigation  
**Last updated:** May 2026  
**Version:** v1.0.0-experimental

---

## Summary

| File | N | T | r | Bootstrap mean r | Verdict |
|------|---|---|---|-----------------|---------|
| zeros_ht.txt | 10,000 | ~10¹² | 0.5113 | 0.09 ± 0.30 | UNSTABLE |
| zeros1.txt | 100,000 | ~40K | 0.6847 | 0.36 ± 0.26 | UNSTABLE |
| zeros6.txt | 2,001,052 | ~600K | 0.4509 | 0.68 ± 0.09 | MODERATE |

**Key finding:** r is not universal. It varies by dataset, scale, and normalization.  
**Original r = 0.6847 (zeros1) (earlier result — not stable across datasets) has not been reproduced on any tested file.**

---

## Canonical Wording

Preliminary computational correlations were observed, but robustness across
datasets and scales remains unresolved.

Монгол: Урьдчилсан тооцооллын корреляцийн хандлага ажиглагдсан боловч
өгөгдлийн багц болон масштаб хоорондын тогтвортой байдал одоогоор
тодорхойгүй байна.

---

## 1. Replication Failure — zeros_ht.txt

**File:** zeros_ht.txt (Odlyzko 10¹² block, N=10,000)  
**Result:** r = 0.5113 (not r = 0.6847 (zeros1) (earlier result — not stable across datasets))  
**Bootstrap:** Mean r = 0.09 ± 0.30, 95% CI [-0.49, 0.65] → UNSTABLE  
**Status:** ❌ Original result not reproduced

---

## 2. Bootstrap Results — All Files

### zeros_ht.txt (N=10,000)
- Full r = 0.5113
- Bootstrap: 0.09 ± 0.30 → **UNSTABLE**
- r < 0: 39% of subsets

### zeros1.txt (N=100,000)
- Full r = 0.6847
- Bootstrap: 0.36 ± 0.26 → **UNSTABLE**
- r < 0: 9.9% of subsets

### zeros6.txt (N=2,001,052)
- Full r = 0.4509
- Bootstrap: 0.68 ± 0.09 → **MODERATE**
- r < 0: 0% of subsets
- r > 0.5: 97% of subsets

**Interpretation:** Signal stability increases with N. At N=2M, signal
is consistently positive but not strong (r~0.68, not r~0.9992).

---

## 3. C Constant — Scale Dependent

| File | C (A/B mean ratio) |
|------|-------------------|
| zeros1.txt | 3.37 |
| zeros6.txt | 3.11 |
| zeros_ht.txt | -2.56 |

C ≈ 3 is consistent across low-T datasets.  
C = -2.56 on high-T block suggests sign instability.  
**No universal constant can be claimed.**

---

## 4. Independent Replication

- Andrew Odlyzko: Form letter decline (high volume of requests)
- Steven Clark (MSE): r = 0.6847 (zeros1) (earlier result — not stable across datasets) confirmed on unknown dataset — awaiting dataset identification
- Facebook requests: All AI-generated responses (r = sin(1) = 0.8414...)

---

## 5. Open Questions

1. Which dataset produces r = 0.6847 (zeros1) (earlier result — not stable across datasets)? (Steven Clark's file unknown)
2. Why does r decrease as N increases?
3. Is C ≈ 3 theoretically meaningful?
4. What is the effect of normalization choice on r?

---

## Statement

This project makes no claim of proof of the Riemann Hypothesis.
All results are exploratory computational observations.
Robustness across datasets and scales remains unresolved.
