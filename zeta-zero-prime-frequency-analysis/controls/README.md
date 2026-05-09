# Control Tests — Null Hypothesis Testing

These scripts test whether the observed prime-indexed excess 
in Riemann zero spacing statistics survives rigorous null controls.

## H₀ (Null hypothesis)
> There is no prime-correlated structure in Riemann zero spacings.
> The observed correlation is a statistical artifact.

## Tests

| Script | Test | What it answers |
|--------|------|-----------------|
| `01_shuffled_control.py` | Permutation test | Is signal in ordering, not marginals? |
| `02_gue_simulation.py` | GUE surrogate | Is signal beyond pure GUE baseline? |
| `03_scaling_law.py` | N scaling | Does signal survive larger N? |
| `04_window_effects.py` | Window stability | Is signal robust to windowing? |
| `05_blind_test.py` | Blind detection | Do peaks cluster near primes blindly? |

## How to run

```bash
pip install numpy scipy matplotlib
python 01_shuffled_control.py   # uses zeros3.txt if present
python 02_gue_simulation.py
python 03_scaling_law.py
python 04_window_effects.py
python 05_blind_test.py
```

## Data
Place Odlyzko zero files in the same directory:
- `zeros2.txt` — http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros2
- `zeros3.txt` — http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros3
- `zeros4.txt` — http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros4

Scripts fall back to synthetic GUE data if files are not found.

## Interpreting results

| Result | Interpretation |
|--------|----------------|
| r(shuffled) ≈ 0 | Signal is in ordering, not marginal distribution ✅ |
| r(GUE) << r(real) | Signal exceeds pure GUE baseline ✅ |
| r stable as N grows | Not a finite-size artifact ✅ |
| r stable across windows | Not Fourier leakage ✅ |
| Blind peaks match primes | Prime-specific structure ✅ |

If **all 5** tests pass → "Interesting experimental mathematics result."
If **any** test fails → the corresponding confound must be addressed.
