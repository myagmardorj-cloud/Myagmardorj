"""
Control Test 6: Block Bootstrap
=================================
Computes bootstrap confidence intervals for Pearson r
using block bootstrap to account for autocorrelation
in consecutive spacing covariances.

Block bootstrap preserves local dependence structure
unlike iid resampling.

Usage:
    python 06_bootstrap.py [zeros_file]
"""

import sys
import numpy as np
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PRIMES   = [2,3,5,7,11,13,17,19,23,29,31,37]
N_BOOT   = 1000
BLOCK_SZ = 50

def load_zeros(path):
    try:
        return np.loadtxt(path)
    except FileNotFoundError:
        print(f"[INFO] {path} not found -- using synthetic GUE data")
        rng = np.random.default_rng(42)
        u = rng.uniform(0, 1, 10000)
        sp = np.sqrt(-4/np.pi * np.log(1-u+1e-10))
        return 1e12 + np.cumsum(sp)

def cov_lags(gamma, lags):
    d = np.diff(gamma)
    d -= d.mean()
    return np.array([
        np.mean(d[:-h]*d[h:]) if len(d) > h+10 else 0.0
        for h in lags
    ])

def bk(primes):
    lp = np.log(np.array(primes, float))
    return lp**2 / np.array(primes, float)

def block_bootstrap(gamma, primes, Bp, n_boot, block_sz, rng):
    delta = np.diff(gamma)
    delta -= delta.mean()
    n = len(delta)
    r_boot = []
    n_blocks = (n + block_sz - 1) // block_sz
    for _ in range(n_boot):
        starts = rng.integers(0, max(1, n - block_sz), size=n_blocks)
        d_boot = np.concatenate([delta[i:i+block_sz] for i in starts])[:n]
        g_boot = gamma[0] + np.concatenate([[0], np.cumsum(np.abs(d_boot))])
        Ap = cov_lags(g_boot, primes)
        r, _ = pearsonr(Ap, Bp)
        r_boot.append(r)
    return np.array(r_boot)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "zeros3.txt"
    rng  = np.random.default_rng(42)

    print("=" * 55)
    print("Control Test 6: Block Bootstrap")
    print("=" * 55)

    gamma = load_zeros(path)
    Bp    = bk(PRIMES)
    Ap    = cov_lags(gamma, PRIMES)
    r_real, p_naive = pearsonr(Ap, Bp)

    print(f"  Real r                  = {r_real:.4f}")
    print(f"  Naive p-value           = {p_naive:.3e} (uncorrected)")
    print(f"  Running {N_BOOT} block bootstrap (block={BLOCK_SZ})...")

    r_boot = block_bootstrap(gamma, PRIMES, Bp, N_BOOT, BLOCK_SZ, rng)
    ci_lo, ci_hi = np.percentile(r_boot, [2.5, 97.5])
    p_boot = np.mean((r_boot - r_boot.mean()) >= r_real)

    print(f"  Bootstrap 95%% CI       = [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Bootstrap mean r        = {r_boot.mean():.4f}")
    print(f"  Bootstrap p-value       = {p_boot:.4f} (approx)")
    print()
    print("  NOTE: Naive p assumes independence -- likely too small.")
    print("  Bootstrap CI accounts for autocorrelation.")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(r_boot, bins=40, color='steelblue', alpha=0.75,
            label='Block bootstrap')
    ax.axvline(r_real, color='red', lw=2,
               label=f'Real r = {r_real:.4f}')
    ax.axvline(ci_lo, color='orange', lw=1.5, ls='--',
               label=f'95%% CI [{ci_lo:.3f}, {ci_hi:.3f}]')
    ax.axvline(ci_hi, color='orange', lw=1.5, ls='--')
    ax.set_xlabel('Pearson r')
    ax.set_ylabel('Count')
    ax.set_title('Test 6: Block Bootstrap Confidence Interval')
    ax.legend()
    plt.tight_layout()
    plt.savefig('results_06_bootstrap.png', dpi=150)
    plt.close()
    print("  Saved: results_06_bootstrap.png")

if __name__ == "__main__":
    main()
