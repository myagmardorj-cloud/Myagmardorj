# results/v2/ — Next Version Placeholder

**Status:** Not yet produced  
**Planned:** After independent replication of v1

---

## What will go here

Results from any of:
- Larger datasets (T ~ 10²¹)
- Bootstrap confidence intervals (controls/06_bootstrap.py)
- Negative controls output (controls/07_negative_controls.py)
- Robustness tests output (controls/08_robustness_tests.py)
- Independent replication on different machine

---

## Policy

- v2 results do NOT overwrite v1
- v1/README.md remains frozen permanently
- Each version is independently reproducible from its git tag

---

## To produce v2 results

```bash
git checkout v1.1.0   # (future tag)
python controls/run_all.py zeros1.txt
python controls/07_negative_controls.py zeros1.txt
python controls/08_robustness_tests.py zeros1.txt
# Save outputs here
```
