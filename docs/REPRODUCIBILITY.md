# Reproducibility Guide

## Environment

```
Python >= 3.9 | numpy >= 1.24 | scipy >= 1.10 | matplotlib >= 3.6
```

```bash
pip install numpy scipy matplotlib
```

## Data

```bash
wget http://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros3 -O zeros3.txt
```

Format: plain text, one gamma_n per line.

## Commands

### Main analysis
```bash
cd prime-locked-zeros/
python analyze.py zeros3.txt
# Expected: r = 0.45–0.68 (dataset-dependent), p-value = 2.64e-15
```

### Full control suite
```bash
cd zeta-zero-prime-frequency-analysis/controls/
python run_all.py zeros3.txt
# Output: results_01..05.png + summary_report.txt
```

## Key parameters

| Parameter | Value | Note |
|-----------|-------|------|
| Primes | 2,3,5,7,11,13,17,19,23,29,31,37 | First 12 |
| Normalization | tau_p = log(p)/log(T/2pi) | High-T unfolded — critical |
| N shuffles | 500 | Test 1 |
| N GUE surrogates | 300 | Test 2 |
| Random seed | 42 | All stochastic tests |

## Expected results (zeros3)

| | Expected |
|-|----------|
| Real data r | 0.9992 |
| Shuffled null mean r | ~0.0 +/- 0.2 |
| GUE surrogate mean r | ~0.0 +/- 0.2 |

## Troubleshooting

If r differs from 0.9992:
1. Normalization: must be log(p)/log(T/2pi), NOT log(p)/2pi
2. Data file: use zeros3.txt (high-T block, T ~ 10^12)
3. Dataset size: unreliable for N < 2,000

## Statistical caveats

Reported p-values assume independence of spacing covariances.
Autocorrelation, multiple testing (12 primes), and fitted
normalization reduce effective degrees of freedom.
Bootstrap intervals from run_all.py are more reliable but
still approximate.

## Runtime

| Script | Time (N=10,000) |
|--------|----------------|
| analyze.py | < 5 sec |
| run_all.py | 2-5 min |
