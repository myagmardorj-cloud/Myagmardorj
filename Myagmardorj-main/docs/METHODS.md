# Methods

## 1. Data

Odlyzko zero tables (University of Minnesota):
- zeros_ht: 100,000 zeros near T ~ 74,920  [Odlyzko file: zeros2]
- zeros1: ~2M zeros near T ~ 10^12         [Odlyzko file: zeros3]
- zeros6: ~10,000 zeros near T ~ 10^13     [Odlyzko file: zeros4]

Format: imaginary parts gamma_n of non-trivial zeros of zeta(s).
Source: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

## 2. Spacing covariance

Let delta_n = gamma_{n+1} - gamma_n. Center: delta_n -= mean(delta).

Covariance at lag h:
  C(h) = mean( delta_n * delta_{n+h} )  for n = 1..N-h

## 3. BK predictor

  B(p) = (log p)^2 / p

## 4. Normalization

High-T unfolded prime frequency (empirically effective in this study):
  tau_p = log(p) / log(T / 2*pi)   [used in this work]
  tau_p = log(p) / (2*pi)          [gives r ~ 0.4, not used]

See notes/failure_analysis.md for details.

## 5. Correlation test

Pearson r between {C(p)} and {B(p)} across primes p = 2..37.

## 6. Null controls (controls/ directory)

Test 1: Shuffled zeros -- randomly permute spacings, recompute r
Test 2: GUE surrogates -- Wigner-surmise spacings, recompute r
Test 3: Scaling law -- vary N from 500 to 10,000
Test 4: Window stability -- Hann, Blackman, Hamming windowing
Test 5: Blind detection -- find top-k peaks without knowing primes
Test 6: Block bootstrap -- confidence intervals for r

## 7. Parameters

Primes tested:  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
N shuffles:     500
N GUE:          300
Bootstrap N:    1000 (block size 50)
Random seed:    42

## 8. Statistical caveats

Naive p-values assume independence of covariance estimates.
This assumption is violated: consecutive spacing covariances are
correlated. Effective degrees of freedom < 12. Multiple testing
(12 primes) is not corrected. Use block bootstrap CI (Test 6)
for any formal inference.
