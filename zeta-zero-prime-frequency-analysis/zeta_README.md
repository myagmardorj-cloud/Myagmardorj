# Zeta Zero Prime Frequency Analysis

Numerical study of prime-correlated structure in
high Riemann zero spacing statistics.

## Main finding

Strong numerical evidence for BK-type amplitude scaling:

```
A(p) ~ C · (log p)² / p,   C ≈ 16.5
```

across 3 independent Odlyzko zero blocks.

| Dataset | Height | r | p-value | 12/12 |
|---------|--------|---|---------|-------|
| zeros2 | ~74,920 | 0.9783 | 3.82e-186 | ✅ |
| zeros3 | ~10¹² | 0.9992 | 2.64e-15 | ✅ |
| zeros4 | ~10¹³ | 0.9421 | 5.0e-6 | ✅ |

> ⚠️ Numerical observations only.
> Not a confirmed theorem. Not a proof of RH.
> Independent replication and peer review needed.

## Key normalization

```python
# CORRECT — high-T unfolded
tau_p = log(p) / log(T / 2*pi)

# WRONG — gives r ≈ 0.4-0.6
tau_p = log(p) / (2*pi)
```

## Repository structure

```
code/
  01_power_spectrum.py     ← S(τ) power spectrum
  02_prime_excess.py       ← ΔK(p) excess at prime lags
  03_BK_amplitude_test.py  ← BK law Pearson correlation
  04_null_tests.py         ← shuffled zeros control
  utils.py                 ← shared utilities

paper/
  main.tex                 ← LaTeX preprint

notes/
  failure_analysis.md      ← why low-T normalization failed
  framework_summary.md     ← Mellin operator framework

data/
  README.md                ← data sources (Odlyzko tables)
```

## Usage

```bash
pip install -r requirements.txt
python code/03_BK_amplitude_test.py
```

## References

- Bogomolny & Keating (1996): Nonlinearity 9
- Montgomery (1973): Proc. Sympos. Pure Math. 24
- Odlyzko (1992): zero tables
- Hiary & Odlyzko (2012): arXiv:1105.4312

## Preprint

DOI: [10.5281/zenodo.20077673](https://zenodo.org/records/20077673)
