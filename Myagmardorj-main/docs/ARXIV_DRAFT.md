# arXiv Submission Draft
## Prime-Indexed Excess in Riemann Zero Spacing Covariance

---

## Recommended Title

```
Empirical Observations of Prime-Indexed Structure in High Riemann
Zero Spacing Covariance: A Computational Study
```

**Alternatives (conservative → slightly stronger):**

```
[A] Computational Observations Related to Bogomolny–Keating-Type
    Prime Correlations in Zeta Zero Statistics

[B] Prime-Indexed Covariance Excess in High Riemann Zero Blocks:
    Empirical Structure Consistent with BK Predictions

[C] Empirical Structure in Prime-Indexed Zero Statistics:
    A Numerical Exploration
```

Recommendation: use [A] or [C]. Avoids implying confirmation of BK.

---

## Abstract (arXiv-ready)

```
We report a computational observation: statistically elevated
covariance at prime-indexed lags in the spacing statistics of
high Riemann zero blocks, empirically consistent with the
Bogomolny--Keating (1996) prediction for prime-dependent
corrections to GUE pair correlation.

Using high-T unfolded normalization on three independent Odlyzko
datasets at heights T ~ 10^{74920}, 10^12, 10^13, we observe
Pearson r varies: 0.45–0.68 (dataset-dependent) between the empirical spacing covariance A(p)
and the BK predictor B(p) = (log p)^2/p across 12 primes
(p = 2, 3, ..., 37). Null controls using shuffled zeros, GUE
surrogates, and composite-lag indices produce r ~ 0, consistent
with a prime-specific rather than generic signal.

Several confounds have not been fully excluded: the high-T
normalization was selected after observing weak results with the
low-T formula (selection bias), the sample size is small (n=12
prime lags), consecutive spacing covariances are not independent
(effective DOF < 12), and no asymptotic analysis has been
performed. An empirical ratio R(p) = A(p)/B(p) was reported as ~16.5 in v1 but is not reproduced in reanalysis; it appears
approximately stable across primes but has no theoretical
derivation.

These are computational observations only. This work is not a
confirmed theorem and not a proof of the Riemann Hypothesis.
Independent replication and rigorous asymptotic analysis are
required. All code and data instructions are publicly available.
```

**Word count:** ~200 words (arXiv limit: 1920 chars — this fits)

---

## arXiv Categories

**Primary:**
```
math.NT  (Number Theory)
```

**Cross-list:**
```
math-ph  (Mathematical Physics)
```

**Keywords:**
```
Riemann zeta function; pair correlation; Bogomolny-Keating;
GUE statistics; prime numbers; computational number theory;
experimental mathematics; spacing covariance
```

---

## MSC Classification

```
11M26   (Nonreal zeros of zeta and L-functions)
11Y35   (Analytic computations)
15B52   (Random matrices)
```

---

## Cover Letter Note (for journal submission)

> This paper reports a computational observation and makes no
> claim of proof. The authors are aware that similar-sounding
> claims have appeared in non-peer-reviewed form; this submission
> is distinguished by explicit negative controls, documented
> limitations, and open reproducible code. We submit to
> Experimental Mathematics as an exploratory numerical result
> appropriate for that venue.

---

## Submission Checklist

- [ ] `paper/main.tex` compiles without errors (`pdflatex main.tex`)
- [ ] All figures generated from `generate_flagship_figure.py`
- [ ] A(p) values in figure match actual `analyze.py` output
- [ ] `CHECKSUMS.sha256` filled with verified zero file hashes
- [ ] Abstract word count within arXiv limit
- [ ] No "proof", "confirmed", "solved" in title or abstract
- [ ] DOI (Zenodo) in paper header
- [ ] GitHub URL in paper body
