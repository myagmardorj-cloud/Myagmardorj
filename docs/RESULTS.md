# Results

## Main result

Empirical agreement with BK-type amplitude scaling observed
after high-T normalization across 3 independent datasets:

| Dataset | Height  | Pearson r | naive p-value (uncorrected) |
|---------|---------|-----------|----------------------------|
| zeros2  | ~74,920 | 0.9783    | 3.82e-186                  |
| zeros3  | ~10^12  | 0.9992    | 2.64e-15                   |
| zeros4  | ~10^13  | 0.9421    | 5.0e-6                     |

NOTE: Naive p-values assume independence. Autocorrelation
and multiple testing reduce effective degrees of freedom.
See controls/06_bootstrap.py for corrected confidence intervals.

Consistency of the prime-correlated excess signal was observed
across tested prime ranges (p = 2, 3, 5, ..., 37) on all datasets.

Empirical ratio R(p) = C(p)/B(p) ~ ~3 in tested datasets; not universally stable
across primes (zeros3). No theoretical derivation exists.

## Null control results

| Control        | Result                           | Interpretation            |
|----------------|----------------------------------|---------------------------|
| Shuffled zeros | r ~ 0.0 +/- 0.2                 | Signal in ordering only   |
| GUE surrogate  | r ~ 0.0 +/- 0.2                 | Exceeds GUE baseline      |
| Scaling N      | r stable across N=500..10,000   | Not obvious finite artifact|
| Window test    | r stable across window types    | Not Fourier leakage       |
| Blind test     | Peaks cluster near primes       | Prime-specific pattern    |

## Provisional interpretation

The BK amplitude law is supported by numerical observations
in this dataset. The observed signal is empirically consistent
with the Bogomolny-Keating (1996) prediction for prime-dependent
corrections to pair correlation statistics of zeta zeros.

This is NOT evidence that:
- The Riemann Hypothesis has been advanced
- C = 16.5 (earlier estimate — not stable across datasets) has been theoretically explained
- These results will replicate under asymptotic analysis

See LIMITATIONS.md for full caveat list.
