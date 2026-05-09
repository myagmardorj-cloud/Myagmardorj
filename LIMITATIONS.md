# Limitations

## Statistical

1. p-values assume independence — violated by autocorrelation
   in consecutive spacing covariances. Effective DOF < 12.

2. Multiple testing — 12 primes tested with no Bonferroni
   or FDR correction. Reported p-values are uncorrected.

3. Only 12 data points — Pearson r with n=12 is highly
   sensitive to individual outliers and overfitting.

4. Normalization fitted to data — the choice of high-T
   unfolded normalization was made after observing that
   low-T normalization gave weak results. This introduces
   selection bias.

## Computational

5. Finite-window effects — C(h) from a finite zero block
   may contain spectral leakage artifacts. Window stability
   tests (Test 4) are partial checks only.

6. Unknown asymptotic stability — we do not know whether
   r -> 0 or r -> 1 as N -> infinity. Scaling tests cover
   only N = 500..10,000.

7. Dataset dependence — only 3 Odlyzko datasets tested.
   Results at other heights are unknown.

## Theoretical

8. No analytic derivation — the empirical constant C ~ 16.5
   has no theoretical prediction or derivation.

9. Relation to BK (1996) is heuristic — BK predicted
   A(p) ~ C*(log p)^2/p as a form, not the exact constant.
   Our normalization and statistic differ from BK's setup.

10. Not evidence for RH — this work provides no pathway
    toward a proof or disproof of the Riemann Hypothesis.

## What this work is NOT

- NOT a proof of the Riemann Hypothesis
- NOT a confirmation of the BK amplitude law
- NOT a peer-reviewed or independently replicated result
- NOT a new mathematical theorem
- NOT evidence of a "hidden mechanism" or "prime locking"

## What this work IS

- A reproducible numerical observation
- Empirically consistent with BK-type scaling
- A basis for further investigation with proper controls
- An open computational experiment
