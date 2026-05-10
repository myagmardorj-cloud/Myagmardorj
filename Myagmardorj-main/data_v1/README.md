# data_v1/ — Immutable Data Archive

**Version:** v1.0 freeze  
**Frozen:** 2026-05-09  
**Status:** Read-only — do not modify files in this directory

---

## Purpose

This directory contains the exact data used to produce the results
reported in v0.3 of this study. It is an **immutable archive**.

If you reproduce the analysis, compare your intermediate outputs
against the checksums below. If you obtain different results,
document the discrepancy in a GitHub Issue.

---

## Directory Structure

```
data_v1/
├── README.md                  ← this file
├── CHECKSUMS.sha256           ← SHA-256 of all data files
│
├── zeros/                     ← Odlyzko zero files (not included in repo)
│   ├── zeros_ht.txt           ← 100,000 zeros near T ≈ 74,920  [Odlyzko: zeros2]
│   ├── zeros1.txt             ← ~2M zeros near T ~ 10¹²        [Odlyzko: zeros3]
│   └── zeros6.txt             ← ~10,000 zeros near T ~ 10¹³    [Odlyzko: zeros4]
│
├── primes/
│   └── primes_v1.txt          ← Primes used: 2 3 5 7 11 13 17 19 23 29 31 37
│
└── outputs_v1/
    ├── zeros_ht_results.txt   ← A(p), B(p), r for zeros_ht
    ├── zeros1_results.txt     ← A(p), B(p), r for zeros1  ← main result
    ├── zeros6_results.txt     ← A(p), B(p), r for zeros6
    └── null_summary.txt       ← shuffled/GUE control summary
```

---

## Data Source

Zero files are from Andrew Odlyzko's tables:

```
http://www-users.cse.umn.edu/~odlyzko/zeta_tables/
```

They are **not included** in this repository (large files, third-party data).
Download `zeros2` (→ zeros_ht), `zeros3` (→ zeros1), `zeros4` (→ zeros6) from Odlyzko and rename.

---

## Checksums

After downloading, verify:

```bash
sha256sum data_v1/zeros/zeros1.txt
```

Expected checksums (fill after first verified run):

```
# zeros_ht.txt sha256: <run: sha256sum zeros_ht.txt>
# zeros1.txt   sha256: <run: sha256sum zeros1.txt>
# zeros6.txt   sha256: <run: sha256sum zeros6.txt>
```

---

## Primes Used (v1 freeze)

```
2  3  5  7  11  13  17  19  23  29  31  37
```

First 12 primes. This list is **frozen** for v1.0.
Any extension (e.g., adding p=41,43,47) constitutes a v1.1+ analysis.

---

## Key Outputs (v1 freeze)

### zeros1 main result (reanalyzed)

| p  | B(p) = (log p)²/p | Note |
|----|-------------------|------|
|  2 | 0.2402             | run analyze.py for A(p) |
|  3 | 0.4023             | run analyze.py for A(p) |
|  5 | 0.5181             | run analyze.py for A(p) |
|  7 | 0.5409             | run analyze.py for A(p) |
| 11 | 0.5227             | run analyze.py for A(p) |
| 13 | 0.5061             | run analyze.py for A(p) |
| 17 | 0.4722             | run analyze.py for A(p) |
| 19 | 0.4563             | run analyze.py for A(p) |
| 23 | 0.4274             | run analyze.py for A(p) |
| 29 | 0.3910             | run analyze.py for A(p) |
| 31 | 0.3804             | run analyze.py for A(p) |
| 37 | 0.3524             | run analyze.py for A(p) |

**A(p) values depend on the dataset and must be obtained by running:**
```bash
python scripts/analyze.py zeros1.txt
```

**R(p) = A(p)/B(p)** was reported as ~16.5 in v1; reanalysis on zeros1 does not reproduce this constant.
Exact value varies with dataset and normalization. No theoretical derivation exists.
---

## Freeze Policy

- Files in `data_v1/outputs_v1/` are frozen after v1.0 tag
- No result numbers may change after the v1.0 GitHub release tag
- New analyses (robustness, negative controls) go in `data_v2/`
- The v1.0 tag is an **archive checkpoint**, not a claim of finality

---

## Reproducibility Note

```bash
# To reproduce from scratch:
cd prime-locked-zeros/
python analyze.py ../data_v1/zeros/zeros1.txt
# Compare output r value to range 0.45–0.68
# If different: open a GitHub Issue with your environment details
```

Differences may arise from:
- Different numpy/scipy versions (floating point)
- Different zero file (verify checksum)
- Different normalization (must use high-T formula)

All differences are scientifically important and should be documented.
