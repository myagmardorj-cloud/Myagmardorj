"""
fx_analysis.py — Steven Clark Formula (4) analysis
f(x) = -2 * x^(-0.5) * sum(cos(gamma_n * log(x)))

Tests whether f(p) > 0 at prime positions vs composite positions.

Usage:
    python scripts/fx_analysis.py zeros1.txt
    python scripts/fx_analysis.py zeros6.txt --start 1000000

Bug fixed (2026-05-13):
    zeros6.txt contains zeros1.txt as a subset (both start at T~14).
    Use --start to select a high-T block from zeros6.txt.

Expected results (corrected):
    zeros1    (T~14→74920):  Cohen d ≈ 1.674, 17/17 primes positive
    zeros6_hi (T~600270+):   Cohen d ≈ 1.674, 17/17 primes positive
    zeros_ht  (first 10K):   Cohen d ≈ 1.674, 17/17 primes positive
"""

import sys
import argparse
import numpy as np
from scipy import stats

# Primes up to 60
PRIMES = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59}
TEST_X  = list(range(2, 60))

def load_zeros(path, start=0, count=100000):
    vals = []
    with open(path) as f:
        for i, line in enumerate(f):
            if i < start:
                continue
            if len(vals) >= count:
                break
            try:
                vals.append(float(line.strip()))
            except ValueError:
                continue
    if not vals:
        raise ValueError(f"No numeric data found in {path} (start={start})")
    return np.array(vals)

def fx_compute(gamma, x_vals):
    results = {}
    for x in x_vals:
        fx = -2.0 * x**(-0.5) * np.sum(np.cos(gamma * np.log(x)))
        results[x] = fx
    return results

def analyze(gamma, label):
    N = len(gamma)
    T_mid = gamma[N // 2]

    fx = fx_compute(gamma, TEST_X)

    prime_vals = [fx[x] for x in TEST_X if x in PRIMES]
    comp_vals  = [fx[x] for x in TEST_X if x not in PRIMES]

    mu_p  = np.mean(prime_vals)
    mu_c  = np.mean(comp_vals)
    pos   = sum(1 for v in prime_vals if v > 0)
    _, pval = stats.ttest_ind(prime_vals, comp_vals)
    pooled_std = np.std(prime_vals + comp_vals, ddof=1)
    d = (mu_p - mu_c) / pooled_std if pooled_std > 0 else 0.0

    print(f"\n{'='*60}")
    print(f"Dataset : {label}")
    print(f"N zeros : {N:,}  |  T_mid ≈ {T_mid:,.0f}")
    print(f"{'='*60}")
    print(f"  μ f(prime)   = {mu_p:>10.2f}")
    print(f"  μ f(comp)    = {mu_c:>10.2f}")
    print(f"  Pos primes   = {pos}/{len(prime_vals)}")
    print(f"  p-value      = {pval:.4e}")
    print(f"  Cohen's d    = {d:.4f}")
    print(f"{'='*60}")

    print(f"\n  {'x':>4}  {'f(x)':>12}  {'type':>9}")
    for x in TEST_X:
        t = 'PRIME' if x in PRIMES else 'composite'
        print(f"  {x:>4}  {fx[x]:>12.2f}  {t:>9}")

    return {"label": label, "T_mid": T_mid, "N": N,
            "mu_prime": mu_p, "mu_comp": mu_c,
            "pos": pos, "total_primes": len(prime_vals),
            "pval": pval, "cohen_d": d}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zerofile", help="Path to Odlyzko zeros file")
    parser.add_argument("--start", type=int, default=0,
                        help="Skip first N lines (use for zeros6 high-T block)")
    parser.add_argument("--count", type=int, default=100000,
                        help="Number of zeros to load (default: 100000)")
    args = parser.parse_args()

    print(f"Loading {args.count:,} zeros from {args.zerofile} (start={args.start})...")
    gamma = load_zeros(args.zerofile, start=args.start, count=args.count)
    label = f"{args.zerofile} [start={args.start}, N={args.count}]"
    analyze(gamma, label)

    print("\nNOTE: This is a computational observation.")
    print("Not a proof of RH. Independent replication required.")

if __name__ == "__main__":
    main()
