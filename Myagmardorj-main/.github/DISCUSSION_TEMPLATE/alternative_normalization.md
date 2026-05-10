---
title: "Alternative normalization test — [describe your variant]"
labels: normalization, robustness
---

## Alternative Normalization Test

One of the key open questions in this study is normalization sensitivity.
If you have tested a different normalization formula, please share your results.

---

### Normalization formula tested

```python
# Describe your formula here, e.g.:
tau_p = np.log(primes) / np.log(T / (2 * np.pi))   # high-T (baseline)
# vs
tau_p = np.log(primes) / (2 * np.pi)                # low-T
# vs
tau_p = ???                                          # your variant
```

---

### Motivation

_Why did you test this normalization? Any theoretical justification?_

---

### Results

| Dataset | Normalization | Pearson r | p-value |
|---------|--------------|-----------|---------|
| zeros1 | high-T (baseline) | 0.6847 | bootstrap UNSTABLE |
| zeros1 | your variant | | |

---

### Interpretation

- [ ] Signal robust under this normalization
- [ ] Signal weaker (r drops significantly)
- [ ] Signal absent (r ~ 0)
- [ ] Signal stronger than baseline (r > 0.6847 on zeros1)

---

### Notes

_Any observations about why this normalization performs differently._
