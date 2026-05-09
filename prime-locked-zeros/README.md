# Experimental Computation: Zeta Zero Spacing Correlations

Exploratory numerical investigation of prime-related structure
in Riemann zeta zero spacing statistics.

## What this code does

`analyze.py` computes spacing covariance C(h) for prime lags h=p,
tests correlation with the BK predictor B(p) = (log p)²/p,
and outputs Pearson r, p-value, and scatter plot.

## Status

Exploratory experimental mathematics — not a confirmed result.
See `../controls/` for null hypothesis tests.

## Usage

```bash
pip install -r requirements.txt
python analyze.py
```

Place Odlyzko zero file (e.g. `zeros3.txt`) in this directory.
Download from: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/

## Key normalization

```python
# CORRECT — high-T unfolded
tau_p = log(p) / log(T / 2*pi)

# WRONG — gives r ≈ 0.4
tau_p = log(p) / (2*pi)
```

## Output

- Pearson r and p-value
- Scatter plot: C(p) vs B(p)
- Comparison with published results (zeros2/3/4)

## Limitations

- Only 12 data points (primes 2..37)
- Normalization artifacts not fully ruled out
- Independent replication needed

## References

- Bogomolny & Keating (1996): Nonlinearity 9
- Montgomery (1973): Proc. Sympos. Pure Math. 24
- Odlyzko (1992): zero tables

**Not a proof of RH. Not a confirmed theorem.**
