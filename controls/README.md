# Control Tests — Null Hypothesis Testing

These scripts test whether the observed prime-indexed excess
in Riemann zero spacing statistics survives rigorous null controls.

## H₀ (Null hypothesis)
> The observed correlation r ≈ 0.9992 arises from normalization
> artifacts, finite-window effects, or hidden statistical bias —
> not from genuine prime-indexed structure in Riemann zero statistics.

---

## All Tests

| Script | Category | Test | Expected collapse? |
|--------|----------|------|-------------------|
| `01_shuffled_control.py` | Permutation | Shuffle zero ordering | ✓ Yes — r → 0 |
| `02_gue_simulation.py` | Surrogate | GUE eigenvalues | ✓ Yes — r → 0 |
| `03_scaling_law.py` | Stability | Vary N = 500…10,000 | ✗ No — r stays high |
| `04_window_effects.py` | Stability | Vary window type | ✗ No — r stays high |
| `05_blind_test.py` | Detection | Find peaks without prime label | Prime-specific |
| `06_bootstrap.py` | Statistics | Bootstrap confidence intervals | Corrected CI |
| `07_negative_controls.py` | **Negative** | Composite lags, random phases, fake zeros | ✓ Yes — r → 0 |
| `08_robustness_tests.py` | Robustness | N range, prime cutoff, 4 normalizations | Stable if genuine |

---

## Negative Controls (Test 07) — Most Important

Three controls designed to **fail** if the signal is prime-specific:

**7a. Composite-lag indices**
Replace primes {2,3,5,…,37} with composites {4,6,8,…,22}.
Expected: r ≈ 0 — BK predicts prime-specific structure only.

**7b. Random-phase zeros**
Synthetic zeros with randomised spacing — no arithmetic structure.
Expected: r ≈ 0 — prime signal requires real zero ordering.

**7c. GUE eigenvalues (100 runs)**
Compare real r against GUE 95th percentile.
Expected: real r >> GUE 95th percentile.

If all three collapse → strong (not conclusive) evidence
the signal is prime-indexed rather than generic.

---

## Robustness (Test 08)

| Sub-test | Varies | Stable if genuine |
|----------|--------|-------------------|
| 8a | N = 500…10K, start position | Yes |
| 8b | Prime cutoff: 6, 9, 12, 15 | Yes |
| 8c | Normalization: 4 formulas | Low-T expected to drop |
| 8d | 50 random sub-blocks per N | Yes |

---

## How to Run

```bash
# All controls — recommended
python run_all.py zeros3.txt

# Negative controls only
python 07_negative_controls.py zeros3.txt

# Robustness only
python 08_robustness_tests.py zeros3.txt
```

Download zero files from:
```
http://www-users.cse.umn.edu/~odlyzko/zeta_tables/
```
Scripts fall back to synthetic GUE data if files are not found.

---

## Interpreting Results

| Result | Meaning |
|--------|---------|
| Tests 01, 02, 07 → r ≈ 0 | Signal in prime ordering, not artifacts |
| Tests 03, 04, 08a/b/d → r stable | Not finite-size or windowing artifact |
| Test 08c → r drops for low-T | Normalization sensitivity (expected, known confound) |
| Test 05 → peaks near primes | Prime-specific without prior knowledge |

All tests passing is **necessary but not sufficient**.
Independent replication required.
