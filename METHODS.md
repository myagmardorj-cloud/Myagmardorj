# Methods

## 1. Data

Odlyzko zero tables (University of Minnesota):
- zeros2: 100,000 zeros near T ~ 74,920
- zeros3: ~10,000 zeros near T ~ 10^12
- zeros4: ~10,000 zeros near T ~ 10^13

Format: imaginary parts gamma_n of non-trivial zeros of zeta(s).
Source: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

## 2. Spacing covariance

Let delta_n = gamma_{n+1} - gamma_n. Center: delta_n -= mean(delta).

Covariance at lag h:
  C(h) = mean( delta_n * delta_{n+h} )  for n = 1..N-h

## 3. BK predictor

  B(p) = (log p)^2 / p

## 4. Normalization (critical)

High-T unfolded prime frequency:
  tau_p = log(p) / log(T / 2*pi)   [CORRECT]
  tau_p = log(p) / (2*pi)          [WRONG — gives r ~ 0.4]

Using the low-T formula produces no meaningful signal.
See notes/failure_analysis.md.

## 5. Correlation test

Pearson r between {C(p)} and {B(p)} across primes p = 2..37.

## 6. Null controls (controls/ directory)

Test 1: Shuffled zeros — randomly permute spacings, recompute r
Test 2: GUE surrogates — Wigner-surmise spacings, recompute r
Test 3: Scaling law — vary N from 500 to 10,000
Test 4: Window stability — Hann, Blackman, Hamming windowing
Test 5: Blind detection — find top-k peaks without knowing primes

## 7. Parameters

Primes tested:  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
N shuffles:     500
N GUE:          300
Random seed:    42 (all stochastic tests)

## 8. Statistical caveats

p-values assume independence of covariance estimates at different lags.
This assumption is violated: consecutive spacing covariances are
correlated. Effective degrees of freedom < 12. Multiple testing
(12 primes) is not corrected. These p-values are approximate.
