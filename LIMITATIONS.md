# Limitations

## Statistical

1. Naive p-values assume independence -- violated by autocorrelation
   in consecutive spacing covariances. Effective DOF < 12.
   Use block bootstrap CI (controls/06_bootstrap.py) instead.

2. Multiple testing -- 12 primes tested with no Bonferroni
   or FDR correction. Reported p-values are uncorrected.

3. Only 12 data points -- Pearson r with n=12 is sensitive
   to individual outliers and overfitting.

4. Normalization fitted to data -- high-T unfolded normalization
   was chosen after observing that low-T gave weak results.
   This introduces selection bias.

## Computational

5. Finite-window effects -- C(h) from a finite zero block
   may contain spectral leakage. Window stability tests (Test 4)
   are partial checks only.

6. Unknown asymptotic behavior -- we do not know whether
   r -> 0 or stabilizes as N -> infinity.
   Scaling tests cover only N = 500..10,000.

7. Dataset dependence -- only 3 Odlyzko datasets tested.
   Results at other heights are unknown.

## Theoretical

8. No analytic derivation -- the empirical constant C ~ 16.5
   has no theoretical prediction or derivation in this work.

9. Relation to BK (1996) is heuristic -- BK predicted
   prime-dependent corrections as a form, not the exact constant.
   Our statistic and normalization differ from BK's setup.

10. Not evidence for RH -- this work provides no pathway
    toward a proof or disproof of the Riemann Hypothesis.

## What this work is NOT

- NOT a proof of the Riemann Hypothesis
- NOT a confirmation of the BK amplitude law
- NOT a peer-reviewed or independently replicated result
- NOT a new mathematical theorem
- NOT evidence of a hidden mechanism or prime locking

## What this work IS

- A reproducible numerical observation
- Empirically consistent with BK-type scaling
- A basis for further controlled investigation
- An open computational experiment
