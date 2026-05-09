# Platform Update Guide — v0.3

---

## 1. ZENODO — New version (v3)

URL: https://zenodo.org/records/20077673 → Edit → New version

### Title (unchanged)
```
Numerical Evidence for Prime-Correlated Structure
in High Riemann Zero Blocks
```

### Description (replace entirely)
```
Exploratory computational study of prime-indexed structure
in Riemann zero spacing covariance statistics.

Main observation: Pearson r ≥ 0.94 between empirical
covariance A(p) and BK predictor B(p) = (log p)²/p
across 12 primes on three independent Odlyzko datasets
(T ~ 10¹², 10¹³).

Null controls (shuffled zeros, GUE surrogates, composite
lags) produce r ≈ 0.

IMPORTANT CAVEATS:
- These are computational observations only
- Normalization was selected after observing weak low-T results
  (selection bias — known confound)
- n = 12 data points; naive p-values assume independence
- Not a confirmed theorem
- Not a proof of the Riemann Hypothesis
- Independent replication required

Key normalization: τ_p = log(p) / log(T/2π)

Repository: https://github.com/myagmardorj-cloud/Myagmardorj
Website: https://research.nexcore.ltd
Version: v0.3 (May 2026)
```

### Upload new file
→ Upload updated `paper/main.tex` from the clean zip

---

## 2. GITHUB — Already updated via clean zip upload

After uploading Myagmardorj-clean.zip:
- README already has disclaimer at top
- All wording updated
- Structure reorganized

No additional action needed if zip was uploaded correctly.

---

## 3. MATH STACKEXCHANGE — Edit your post

Find your post → Edit → Update the description paragraph:

### Add/replace with:
```
Update (v0.3, May 2026): The repository has been reorganized
with explicit null controls (shuffled zeros, GUE surrogates,
composite-lag indices), robustness tests, and a full limitations
document. Key caveat: the high-T normalization was selected
after observing weak results with low-T formula — this is a
known selection bias. These remain computational observations
only and are not a confirmed result.

Repository: https://github.com/myagmardorj-cloud/Myagmardorj
DOI: https://zenodo.org/records/20077673
```

---

## 4. REDDIT — Edit your post or add comment

### Comment to add under your post:
```
Update (v0.3, May 2026):

Repository has been significantly improved:
- 8 null/robustness/negative control tests added
- Explicit null hypothesis stated
- Normalization sensitivity documented (known confound)
- Full limitations section
- One-command reproduction: python scripts/run_all.py zeros3.txt

Key clarification: the high-T normalization τ_p = log(p)/log(T/2π)
was selected after observing that low-T gave r ≈ 0.4 — this is
a selection bias and the most important caveat.

These are computational observations only — not a proof of RH.
Independent replication welcome.

GitHub: https://github.com/myagmardorj-cloud/Myagmardorj
DOI: 10.5281/zenodo.20077673
```

---

## 5. RESEARCH.NEXCORE.LTD — Already updated

The HTML files (index.html, verify.html, landscape.html, intro.html)
are all updated in the clean zip with:
- "Computational observations" wording
- "Not a proof of RH" disclaimers
- Fixed script tags
- Proper version footer

Just deploy the updated HTML files to your hosting.

---

## Order of operations

```
1. GitHub    → upload Myagmardorj-clean.zip contents
2. Zenodo    → New version → update description + upload main.tex
3. Website   → deploy updated HTML files
4. StackExchange → edit post, add update note
5. Reddit    → add comment with update
```
