---
title: "Replication attempt — [your environment]"
labels: replication
---

## Replication Attempt

Thank you for trying to replicate this result.
Please fill in as much detail as possible.

---

### Environment

| Item | Value |
|------|-------|
| OS | e.g. Ubuntu 22.04 / macOS 14 / Windows 11 |
| Python version | e.g. 3.11.2 |
| numpy version | `python -c "import numpy; print(numpy.__version__)"` |
| scipy version | `python -c "import scipy; print(scipy.__version__)"` |
| Zero file used | zeros_ht / zeros1 / zeros6 |
| Zero file SHA-256 | `sha256sum zeros1.txt` |

---

### Command run

```bash
# Paste exact command here
python analyze.py zeros1.txt
```

---

### Result obtained

| Metric | Your value | Expected (v0.3) |
|--------|-----------|-----------------|
| Pearson r | | 0.45–0.68 (dataset-dependent) |
| Naive p-value | | 2.64e-15 |
| R(p) mean | | varies (not stable) |

---

### Matches expected?

- [ ] Yes — full replication
- [ ] Partial — r within ±0.01
- [ ] No — significant difference
- [ ] Error during run

---

### Notes / Observations

_Any differences, errors, or additional observations._

---

### Normalization used

- [ ] High-T: `τ_p = log(p) / log(T/2π)`  ← required
- [ ] Other: _describe_

> **Note:** Using `log(p)/2π` (low-T) gives r ≈ 0.4–0.6 and is the
> most common replication discrepancy. See REPRODUCIBILITY.md §Troubleshooting.
