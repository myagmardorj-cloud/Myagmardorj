# Contributing

Thank you for your interest in this project.
This is an exploratory computational study — contributions that
improve reproducibility, controls, or scientific rigor are most valuable.

---

## Most Valuable Contributions

### 1. Independent Replication
Run the analysis on your own machine and report the result:

```bash
git clone https://github.com/myagmardorj-cloud/Myagmardorj
cd Myagmardorj
pip install -r requirements.txt
python scripts/analyze.py zeros3.txt
```

Open a [Discussion → Replication Attempts](.github/DISCUSSION_TEMPLATE/replication_attempt.md)
with your r value, environment, and zero file checksum.
Both matching and non-matching results are valuable.

### 2. Alternative Normalization Tests
Test a different `τ_p` formula and report whether r changes.
Open a [Discussion → Alternative Normalization](.github/DISCUSSION_TEMPLATE/alternative_normalization.md).

### 3. Bug Reports / Discrepancies
Something in the code or docs is wrong?
Open an [Issue](.github/ISSUE_TEMPLATE/discrepancy_report.md).

### 4. Additional Datasets
Results at heights T ~ 10²¹ (Hiary–Odlyzko) would be particularly valuable.

---

## What NOT to Contribute

- Claims that this work proves or disproves the Riemann Hypothesis
- Wording that overstates the result beyond "computational observation"
- Code that removes the null controls or limitations documentation

---

## Code Style

- Python 3.9+
- `numpy`, `scipy`, `matplotlib` — no exotic dependencies
- Every script must run standalone with: `python script.py zeros3.txt`
- Every script must print caveats at the end (see existing scripts)

---

## Scientific Standards

This project follows these principles:

1. **Null hypothesis first** — every claim must state what would falsify it
2. **Limitations visible** — never bury caveats
3. **Reproducible** — every result must be regenerable from public data
4. **Conservative language** — "observed", "consistent with", "computational observation"

---

## Contact

Open a GitHub Issue or Discussion.
