# Numerical Evidence for BK-Type Prime-Lock Scaling in High Riemann Zero Blocks

## Preprint
**Zenodo:** https://zenodo.org/records/20077673  
**DOI:** 10.5281/zenodo.20077673  
**Website:** https://research.nexcore.ltd

---

## Summary

This work presents **numerical evidence** for BK-type prime-correlated structure in the spacing statistics of high Riemann zero blocks.

> ⚠️ These are numerical observations only — not a confirmed theorem, not a proof of RH.  
> Independent replication and peer review are needed.

### Results

| Dataset | Block height | r | p-value | 12/12 primes |
|---------|-------------|---|---------|--------------|
| zeros2 | ~T = 74,920 | 0.9783 | 3.82×10⁻¹⁸⁶ | ✅ |
| zeros3 | ~T = 10¹² | 0.9992 | 2.64×10⁻¹⁵ | ✅ |
| zeros4 | ~T = 10¹³ | 0.9421 | 5.0×10⁻⁶ | ✅ |

The observed amplitude scaling:

```
A(p) ~ C · (log p)² / p,   C ≈ 16.5
```

is consistent with the Bogomolny–Keating (1996) prediction — but **has not been rigorously proved**.

---

## What this is

✅ Strong numerical evidence for prime-correlated structure  
✅ Consistent with BK (1996) prediction across 3 datasets  
✅ Effect robust under high-T normalization τ_p = log(p)/log(T/2π)  

❌ Not a confirmed theorem  
❌ Not peer-reviewed  
❌ Not a proof of the Riemann Hypothesis  

---

## Key normalization

The correct prime frequency at height T:
```
τ_p = log(p) / log(T/2π)   ✅  (high-T unfolded)
τ_p = log(p) / 2π           ❌  (gives r ≈ 0.4–0.6)
```

---

## Repository structure

```
prime-locked-zeros/
  analyze.py              ← main analysis script
  requirements.txt

zeta-zero-prime-frequency-analysis/
  code/
    01_power_spectrum.py
    02_prime_excess.py
    03_BK_amplitude_test.py
    04_null_tests.py
    utils.py
  paper/
    main.tex              ← LaTeX paper
  notes/
    failure_analysis.md   ← why low-T normalization failed
    framework_summary.md  ← Mellin operator framework
  data/README.md
```

---

## References

- Bogomolny & Keating (1996): *Random matrix theory and the Riemann zeros*
- Montgomery (1973): *The pair correlation of zeros of the zeta function*
- Odlyzko (1992): *The 10²⁰-th zero of the Riemann zeta function*
- Hiary & Odlyzko (2012): arXiv:1105.4312

---

## Citation

```bibtex
@misc{namnansuren2026prime,
  author    = {Namnansuren, Myagmardorj},
  title     = {Numerical Evidence for Prime-Correlated
               Structure in High Riemann Zero Blocks},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20077673},
  url       = {https://zenodo.org/records/20077673}
}
```

---

*Myagmardorj Namnansuren · Nexcore LTD · Ulaanbaatar, Mongolia · 2026*
