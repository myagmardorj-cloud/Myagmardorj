# scripts/ — Analysis Scripts

All analysis code for the BK-type prime correlation study.

## Quick Start

```bash
# Full pipeline — one command
python scripts/run_all.py zeros3.txt

# Core analysis only
python scripts/analyze.py zeros3.txt
```

---

## Script Reference

| Script | Purpose | Output |
|--------|---------|--------|
| `analyze.py` | Core BK amplitude test — computes A(p), B(p), Pearson r | r value, p-value, scatter plot |
| `run_all.py` | Full pipeline: analysis + all controls | Summary report |
| `generate_checksums.py` | SHA-256 hashes for data integrity | `data_v1/CHECKSUMS.sha256` |
| `utils.py` | Shared utilities (load zeros, spacing covariance, BK predictor) | — |
| `01_power_spectrum.py` | Power spectrum of zero spacings | Spectrum plot |
| `02_prime_excess.py` | Prime-indexed excess detection | Excess plot |
| `03_BK_amplitude_test.py` | BK law correlation test | r, scatter, ratio R(p) |
| `04_null_tests.py` | Basic null comparisons | Comparison plots |

---

## Execution Order

```
analyze.py              ← start here (main result)
    ↓
run_all.py              ← full pipeline including controls
    ↓
generate_checksums.py   ← after downloading zero files
```

---

## Key Parameters

| Parameter | Value | File |
|-----------|-------|------|
| Primes used | 2 3 5 7 11 13 17 19 23 29 31 37 | `data_v1/primes/primes_v1.txt` |
| Normalization | `τ_p = log(p) / log(T/2π)` | `analyze.py`, `utils.py` |
| Zero datasets | zeros2, zeros3, zeros4 | Odlyzko tables |

**Critical:** high-T normalization `log(p)/log(T/2π)` is required.
Using `log(p)/2π` gives r ≈ 0.4–0.6. See `docs/LIMITATIONS.md §1`.

---

## Expected Output (zeros3.txt)

```
Pearson r  = 0.9992
Naive p    = 2.64e-15   ← uncorrected, see LIMITATIONS.md
R(p) mean  ≈ 16.5
Status:    CONSISTENT WITH BK-TYPE SCALING
```

These are computational observations.
Not a confirmed result. Not a proof of RH.
