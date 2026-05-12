# Release Notes — v1.0.0-experimental

> **Tag:** `v1.0.0-experimental`  
> **Frozen:** _[date to be filled]_  
> **DOI:** 10.5281/zenodo.20077673  
> **Status:** Computational observation — not a confirmed theorem

---

## Stable Citation

Once the v1.0.0-experimental tag is created on GitHub:

```bibtex
@misc{namnansuren2026prime,
  author    = {Namnansuren, Myagmardorj},
  title     = {Prime-Indexed Excess in Riemann Zero Spacing Covariance},
  year      = {2026},
  version   = {1.0.0-experimental},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673},
  url       = {https://zenodo.org/records/20077673},
  note      = {Exploratory computational study.
               Not a proof of the Riemann Hypothesis.}
}
```

**Pin the exact commit hash** after tagging:
```bash
git tag v1.0.0-experimental
git push origin v1.0.0-experimental
# Then add to README:
# Stable commit: github.com/myagmardorj-cloud/Myagmardorj/tree/v1.0.0-experimental
```

After this tag: **no result numbers change**. Future work → v1.1+.

---



A frozen archive of the computational study as of v1.0.
Result numbers will not change after this tag.
Future analysis continues in v1.1+.

---

## What was verified before this release

- [ ] `python scripts/run_all.py zeros1.txt` completes without errors
- [ ] Main r value matches REPRODUCIBILITY.md expected output
- [ ] `data_v1/CHECKSUMS.sha256` filled with verified hashes
- [ ] At least one independent replication attempt documented
- [ ] `paper/main.tex` compiles: `pdflatex main.tex` (0 errors)
- [ ] No "proof", "confirmed", "solved" in any `.md` or `.html` file
- [ ] All HTML pages render correctly in Firefox and Chrome
- [ ] GitHub Discussions open with welcome post pinned

---

## What changed from v0.3 → v1.0

_(fill at release time)_

---

## Known limitations at time of freeze

1. Normalization selection bias — high-T formula chosen post-hoc
2. n = 12 data points — small sample, sensitive to outliers
3. No asymptotic analysis — r behavior as N → ∞ unknown
4. Independent replication: _(status at release time)_

Full list: [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md)

---

## Explicit null hypothesis

> **H₀ (null):** The observed correlation r = 0.6847 (zeros1) arises from
> normalization artifacts, finite-window effects, or hidden
> statistical bias — not from a genuine prime-indexed structure
> in Riemann zero spacing statistics.

The null has not been definitively rejected. Null controls
(shuffled zeros, GUE surrogates, composite lags) produce r ≈ 0,
which is consistent with but does not prove rejection of H₀.
Independent replication and asymptotic analysis are required.

---

## How to cite this release

```bibtex
@misc{namnansuren2026prime,
  author    = {Namnansuren, Myagmardorj},
  title     = {Prime-Indexed Excess in Riemann Zero Spacing Covariance},
  year      = {2026},
  version   = {1.0.0-experimental},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673}
}
```
