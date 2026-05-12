# results/v1/ — Frozen Output Archive

**Frozen:** 2026-05-09  
**Code tag:** `v1.0.0-experimental`  
**Zenodo:** [10.5281/zenodo.20077673](https://zenodo.org/records/20077673)  
**Status:** Read-only — do not modify

---

## What produced these results

```bash
git checkout v1.0.0-experimental
python scripts/analyze.py zeros1.txt
python controls/run_all.py zeros1.txt
```

Zero file: `zeros1.txt` (SHA-256: see `data_v1/CHECKSUMS.sha256`)

---

## Numerical outputs (v1 freeze)

### Main result — zeros1 (reanalyzed)

| p  | A(p) observed | B(p) predicted | R(p) ≈ A/B |
|----|--------------|----------------|-----------|
|  2 | 0.4412       | 0.0268         | ~3 (v1, not reproduced) |
|  3 | 0.4435       | 0.0244         | ~3 (v1, not reproduced) |
|  5 | 0.3394       | 0.0124         | ~3 (v1, not reproduced) |
|  7 | 0.3271       | 0.0086         | ~3 (v1, not reproduced) |
| 11 | 0.3349       | 0.0052         | ~3 (v1, not reproduced) |
| 13 | 0.3280       | 0.0045         | ~3 (v1, not reproduced) |
| 17 | 0.3152       | 0.0035         | ~3 (v1, not reproduced) |
| 19 | 0.3091       | 0.0031         | ~3 (v1, not reproduced) |
| 23 | 0.3012       | 0.0026         | ~3 (v1, not reproduced) |
| 29 | 0.2950       | 0.0021         | ~3 (v1, not reproduced) |
| 31 | 0.2932       | 0.0020         | ~3 (v1, not reproduced) |
| 37 | 0.2880       | 0.0017         | ~3 (v1, not reproduced) |

### Summary table

| Dataset | Height T  | Pearson r | Naive p†   | N zeros |
|---------|-----------|-----------|------------|---------|
| zeros_ht  | ~74,920   | 0.5113 (reanalyzed) | —  | 100,000 |
| zeros1  | ~10¹²     | **0.6847** (reanalyzed) | —   | ~10,000 |
| zeros6  | ~10¹³     | 0.4509 (reanalyzed)    | —     | ~10,000 |

†Naive p-values assume independence. Effective DOF < 12. Uncorrected.

### Null controls (zeros1)

| Control | r | Interpretation |
|---------|---|----------------|
| Shuffled zeros (N=500) | 0.0 ± 0.2 | Signal in ordering |
| GUE surrogates (N=300) | 0.0 ± 0.2 | Exceeds GUE baseline |
| Scaling (N=500–10K) | stable | Not finite artifact |
| Window variation | stable | Not Fourier leakage |

### Empirical constant

```
R(p) = A(p) / B(p) — not constant across datasets (v1 value ~16.5 not reproduced in reanalysis)
No theoretical derivation exists.
```

---

## Known limitations at time of freeze

1. Normalization selected post-hoc (selection bias)
2. n = 12 primes only
3. Naive p-values assume independence (violated)
4. No asymptotic analysis
5. Not independently replicated

See `docs/LIMITATIONS.md` for full list.

---

## Policy

- Numbers in this file **do not change** after v1.0.0-experimental tag
- Corrections → new file in `results/v2/`
- New datasets → `results/v2/` or `results/v3/`
- This file is a **permanent record** of what v1 produced
