# Results

## Main result

Empirical agreement with BK-type amplitude scaling observed
after high-T normalization across 3 independent datasets:

| Dataset | Height    | Pearson r | p-value     |
|---------|-----------|-----------|-------------|
| zeros2  | ~74,920   | 0.9783    | 3.82e-186   |
| zeros3  | ~10^12    | 0.9992    | 2.64e-15    |
| zeros4  | ~10^13    | 0.9421    | 5.0e-6      |

Consistency of the prime-correlated excess signal was observed
across tested prime ranges (p = 2, 3, 5, ..., 37) on all datasets.

Empirical ratio R(p) = C(p)/B(p) ~ 16.5 is approximately
constant across primes (zeros3). This value has no
theoretical derivation in this work.

## Null control results

| Control        | Result                         | Interpretation           |
|----------------|-------------------------------|--------------------------|
| Shuffled zeros | r ~ 0.0 +/- 0.2               | Signal in ordering only  |
| GUE surrogate  | r ~ 0.0 +/- 0.2               | Exceeds GUE baseline     |
| Scaling law    | r stable across N=500..10,000 | Not obvious finite artifact |
| Window test    | r stable across window types  | Not Fourier leakage      |
| Blind test     | Peaks cluster near primes     | Prime-specific pattern   |

## Interpretation (provisional)

The observed signal is empirically consistent with the
Bogomolny-Keating (1996) prediction for prime-dependent
corrections to GUE statistics.

This is NOT evidence that:
- The BK amplitude law has been proved
- The Riemann Hypothesis has been advanced
- The constant C = 16.5 has been theoretically explained

See LIMITATIONS.md and notes/speculative_notes.md for
a clear separation of observation from interpretation.
