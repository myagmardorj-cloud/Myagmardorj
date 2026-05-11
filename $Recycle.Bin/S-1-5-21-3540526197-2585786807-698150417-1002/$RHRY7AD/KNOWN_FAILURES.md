# Known Failures and Limitations

## 1. Wrong normalization (identified and fixed)

Using tau_p = log(p) / (2*pi) instead of log(p)/log(T/2pi)
gives r = 0.4-0.6 — no meaningful signal.
See notes/failure_analysis.md for details.

## 2. Small N (N < 500)

r is highly variable (std > 0.3). Results unreliable below N = 2,000.

## 3. Low-height zeros (zeros2, T ~ 74,920)

Signal is weaker: r = 0.9783 vs 0.9992 for zeros3.
The high-T normalization is less precise at lower heights.

## 4. p-value reliability

Reported p-values assume independent covariance estimates.
Consecutive spacing covariances are correlated, so effective
degrees of freedom < 12. True p-values are likely larger
than reported.

## 5. Prime lags chosen in advance

We selected prime lags before computing C(h). This is not
fully blind — see Test 5 (blind_test.py) for a partial check.
A fully pre-registered analysis has not been done.

## 6. Window sensitivity

Signal is stable across Hann, Blackman, Hamming windows
(Test 4). However, for N < 500, results vary substantially.

## 7. C = 16.5 has no theoretical derivation

The empirical constant C in A(p) ~ C*(log p)^2/p is
estimated from data. Its value may depend on the normalization
choice and dataset. No theoretical prediction exists in this work.

## 8. Not independently replicated

No other researcher has independently confirmed these results
by running the code on the same data.

## 9. Multiple testing not corrected

12 primes were tested simultaneously. No Bonferroni or
FDR correction was applied to the reported p-values.

## What we do NOT claim

- This is NOT a proof of the Riemann Hypothesis
- This is NOT a confirmed mathematical theorem
- r = 0.9992 alone does NOT establish the BK amplitude law
- C = 16.5 is NOT theoretically derived
- The effect has NOT been independently replicated
