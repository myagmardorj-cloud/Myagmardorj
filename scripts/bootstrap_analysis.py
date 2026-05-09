"""
bootstrap_analysis.py — Bootstrap robustness test for BK amplitude correlation
================================================================
Usage:
    python bootstrap_analysis.py zeros_ht.txt
    python bootstrap_analysis.py zeros_100k.txt

Tests whether r = 0.9992 is stable across random subsets of zeros.
"""

import sys
import os
import re
import numpy as np
from scipy.stats import pearsonr

N_BOOTSTRAP = 1000
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
np.random.seed(42)


def load_zeros(path):
    offset = 0.0
    vals = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = re.search(r'gamma\s*-\s*([\d,]+)', line, re.IGNORECASE)
            if m:
                offset = float(m.group(1).replace(',', ''))
                continue
            try:
                vals.append(float(line))
            except ValueError:
                continue
    arr = np.array(vals)
    if offset > 0 and arr.mean() < 1e6:
        arr = arr + offset
    return arr


def compute_r(gamma, subset_idx=None):
    if subset_idx is not None:
        gamma = gamma[subset_idx]
    T = gamma[len(gamma) // 2]
    log_T = np.log(T / (2 * np.pi))
    delta = np.diff(gamma)
    delta -= delta.mean()
    A = np.array([np.mean(delta[:-p] * delta[p:]) for p in PRIMES])
    B = (np.log(PRIMES) ** 2) / np.array(PRIMES, float)
    r, pv = pearsonr(A, B)
    return r


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'zeros_ht.txt'
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"Loading: {path}")
    gamma = load_zeros(path)
    N = len(gamma)
    print(f"N = {N:,} zeros")

    # Full dataset r
    r_full = compute_r(gamma)
    print(f"\nFull dataset:  r = {r_full:.4f}")

    # Bootstrap — random subsets of size N//2
    subset_size = max(N // 2, 500)
    print(f"Bootstrap: {N_BOOTSTRAP} iterations, subset size = {subset_size}")
    print("Running", end='', flush=True)

    rs = []
    for i in range(N_BOOTSTRAP):
        idx = np.sort(np.random.choice(N - 1, subset_size, replace=False))
        r = compute_r(gamma, idx)
        rs.append(r)
        if (i + 1) % 100 == 0:
            print('.', end='', flush=True)
    print()

    rs = np.array(rs)

    print(f"\n{'='*45}")
    print(f"BOOTSTRAP RESULTS ({N_BOOTSTRAP} iterations)")
    print(f"{'='*45}")
    print(f"  Mean r:        {rs.mean():.4f}")
    print(f"  Std  r:        {rs.std():.4f}")
    print(f"  95% CI:        [{np.percentile(rs, 2.5):.4f}, {np.percentile(rs, 97.5):.4f}]")
    print(f"  Min r:         {rs.min():.4f}")
    print(f"  Max r:         {rs.max():.4f}")
    print(f"  r > 0.8:       {(rs > 0.8).sum()}/{N_BOOTSTRAP} ({100*(rs>0.8).mean():.1f}%)")
    print(f"  r > 0.5:       {(rs > 0.5).sum()}/{N_BOOTSTRAP} ({100*(rs>0.5).mean():.1f}%)")
    print(f"  r < 0:         {(rs < 0).sum()}/{N_BOOTSTRAP} ({100*(rs<0).mean():.1f}%)")
    print(f"{'='*45}")

    if rs.std() < 0.1 and rs.mean() > 0.7:
        verdict = "STABLE — signal appears robust to subsampling"
    elif rs.std() < 0.2:
        verdict = "MODERATE — some variability, interpret cautiously"
    else:
        verdict = "UNSTABLE — high variance, possible overfitting"

    print(f"\nVerdict: {verdict}")
    print("\nCAVEATS:")
    print("  Bootstrap subsets are not independent.")
    print("  Result depends on which zero file is used.")
    print("  Not a proof of the Riemann Hypothesis.")

    # Save results
    out = f"bootstrap_{os.path.splitext(os.path.basename(path))[0]}.txt"
    with open(out, 'w') as f:
        f.write(f"Bootstrap analysis — {path}\n")
        f.write(f"N={N}, subset_size={subset_size}, iterations={N_BOOTSTRAP}\n")
        f.write(f"mean_r={rs.mean():.4f}\n")
        f.write(f"std_r={rs.std():.4f}\n")
        f.write(f"ci_low={np.percentile(rs,2.5):.4f}\n")
        f.write(f"ci_high={np.percentile(rs,97.5):.4f}\n")
        f.write(f"verdict={verdict}\n")
    print(f"Results saved: {out}")


if __name__ == '__main__':
    main()
