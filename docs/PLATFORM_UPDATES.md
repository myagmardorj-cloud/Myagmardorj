# Platform Update Guide — v0.3

Copy-paste ready text for each platform.

---

## 1. ZENODO — New version (v3)

`zenodo.org/records/20077673` → Edit → New version

### Description (replace entirely)
```
Exploratory computational study of prime-indexed structure
in Riemann zero spacing covariance statistics.

Main observation: Pearson r ≥ 0.94 between empirical
covariance A(p) and BK predictor B(p) = (log p)²/p
across 12 primes on three independent Odlyzko datasets
(T ~ 10¹², 10¹³). Null controls (shuffled zeros, GUE
surrogates, composite lags) produce r ≈ 0.

IMPORTANT CAVEATS:
- These are computational observations only
- The normalization τ_p = log(p)/log(T/2π) was selected
  after observing weak low-T results — selection bias,
  known confound
- n = 12 data points; naive p-values assume independence
- Not a confirmed theorem
- Not a proof of the Riemann Hypothesis
- Independent replication required

Repository: https://github.com/myagmardorj-cloud/Myagmardorj
Website: https://research.nexcore.ltd
Version: v0.3 (May 2026)
```

Upload: `paper/main.tex` from clean zip → Publish

---

## 2. GITHUB README / Release note

```
Repository updated with more conservative scientific framing.

Main changes:
- "verification" → "comparison"
- "BK confirmed" → "BK-type agreement observed"
- Explicit distinction between computational evidence and proof
- Robustness / null-control structure expanded
- Normalization-selection caveat documented

Important limitation: The normalization procedure was selected
after observing weak low-T results. This introduces potential
selection bias and should be treated as a known confound
requiring independent replication.

This repository presents exploratory computational evidence only
and does not constitute a proof of the Riemann Hypothesis.
```

---

## 3. MATH STACKEXCHANGE — Edit post, add at bottom

```
Update (v0.3 revision):
I revised the project wording to avoid overstating the claims.
Current framing is "BK-type agreement observed" rather than
"verification" or "confirmation".

Explicit caveat added:
The normalization was selected after observing weak low-T
behavior, which introduces possible selection bias.

The repository now focuses on reproducibility, controls,
robustness checks, and computational comparison only.
No proof of RH is claimed.

DOI: 10.5281/zenodo.20077673
```

---

## 4. REDDIT — Add comment (not edit)

```
Project update (v0.3):

Revised repository and manuscript to use more conservative
wording with stronger caveats regarding normalization and
possible selection bias.

Current position:
• Exploratory computational evidence
• BK-type agreement observed in this dataset
• Not a proof of RH
• Independent replication needed

Main improvements:
• Robustness tests expanded (8 controls)
• Controls organized into separate folder
• Reproducibility workflow: python scripts/run_all.py zeros3.txt
• Zenodo + GitHub versioning cleaned up
• Normalization selection bias explicitly documented

DOI: 10.5281/zenodo.20077673
GitHub: github.com/myagmardorj-cloud/Myagmardorj
```

---

## 5. RESEARCH.NEXCORE.LTD

Deploy updated HTML files from clean zip.
All pages already updated with:
- "Computational observations" wording
- "Not a proof of RH" disclaimers
- Version footer: v0.3 · May 2026

---

## Order of operations

```
1. GitHub    → upload clean zip contents         (5 min)
2. Zenodo    → New version → paste description   (5 min)
             → upload paper/main.tex → Publish
3. Website   → deploy updated HTML files         (2 min)
4. StackExch → edit post → paste update note     (2 min)
5. Reddit    → new comment → paste update        (2 min)
```

Total: ~15 minutes
