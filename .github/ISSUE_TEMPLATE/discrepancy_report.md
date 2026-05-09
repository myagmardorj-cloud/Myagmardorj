---
name: Discrepancy / Replication Failure
about: Report a different result or error when running the analysis
labels: discrepancy
---

## Discrepancy Report

### What did you run?

```bash
# Paste command
```

### What did you get?

```
# Paste output
```

### What was expected?

From `REPRODUCIBILITY.md`:
- r = 0.9992 on zeros3
- Shuffled null: r ~ 0

### Your environment

- OS:
- Python:
- numpy:
- scipy:
- Zero file + SHA-256:

### Normalization check

```python
# Which formula did you use?
tau_p = np.log(p) / np.log(T / (2 * np.pi))  # high-T ← required
```

### Additional context

_Any other information that might be relevant._
