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
| Zero file used | zeros2 / zeros3 / zeros4 |
| Zero file SHA-256 | `sha256sum zeros3.txt` |

---

### Command run

```bash
# Paste exact command here
python analyze.py zeros3.txt
```

---

### Result obtained

| Metric | Your value | Expected (v0.3) |
|--------|-----------|-----------------|
| Pearson r | | 0.9992 |
| Naive p-value | | 2.64e-15 |
| R(p) mean | | ~16.5 |

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
