"""
Control Test 5: Blind Peak Detection
================================
Question: Can we detect prime-associated peaks
WITHOUT knowing prime locations in advance?

Method:
1. Compute C(h) for all lags h = 1..50
2. Find the top-k peaks (blind, no prime knowledge)
3. Check overlap with actual prime positions
4. Compare against random overlap (null expectation)

If primes are genuinely special: peaks should cluster
near prime lags more than chance would predict.
"""

import numpy as np
from scipy.stats import pearsonr, hypergeom
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]
MAX_LAG = 50
TOP_K = 12  # how many peaks to declare

def spacing_covariance_all(gamma, max_lag):
    """Compute C(h) for h = 1..max_lag."""
    delta = np.diff(gamma)
    delta -= delta.mean()
    covs = {}
    for h in range(1, max_lag + 1):
        if len(delta) > h + 10:
            covs[h] = np.mean(delta[:-h] * delta[h:])
        else:
            covs[h] = 0.0
    return covs

def bk_predictor(primes):
    lp = np.log(primes)
    return lp**2 / primes

def main():
    print("=" * 55)
    print("Control Test 5: Blind Peak Detection")
    print("=" * 55)
    print(f"Lag range: 1..{MAX_LAG}")
    print(f"Top-k peaks declared: {TOP_K}")
    print(f"Prime positions: {PRIMES}\n")

    # Generate test data
    rng = np.random.default_rng(42)
    n = 10000
    spacings = np.abs(rng.standard_normal(n)) + 0.3
    gamma = 1e12 + np.cumsum(spacings)

    # Compute C(h) for all lags
    covs = spacing_covariance_all(gamma, MAX_LAG)
    lags = np.array(sorted(covs.keys()))
    vals = np.array([covs[h] for h in lags])

    # Blind peak detection: top-k positive lags
    positive_mask = vals > 0
    pos_lags = lags[positive_mask]
    pos_vals  = vals[positive_mask]
    top_idx   = np.argsort(pos_vals)[-TOP_K:][::-1]
    top_lags  = pos_lags[top_idx]

    print(f"Top {TOP_K} positive lags (blind): {sorted(top_lags)}")
    print(f"Prime positions:                   {PRIMES}")

    # Overlap
    prime_set = set(PRIMES)
    top_set   = set(top_lags)
    overlap   = len(prime_set & top_set)
    print(f"\nOverlap: {overlap}/{TOP_K} detected peaks match prime positions")

    # Null expectation via hypergeometric distribution
    # Population N=MAX_LAG, successes K=len(PRIMES), draws n=TOP_K
    M, K, n_draw = MAX_LAG, len(PRIMES), TOP_K
    expected_overlap = n_draw * K / M
    p_val_hyper = hypergeom.sf(overlap - 1, M, K, n_draw)
    print(f"Expected overlap by chance: {expected_overlap:.2f}")
    print(f"Hypergeometric p-value: {p_val_hyper:.4f}")

    if p_val_hyper < 0.05:
        print("\n→ Blind peaks cluster near primes more than chance predicts.")
        print("→ Consistent with prime-specific structure.")
    else:
        print("\n→ Overlap consistent with chance.")
        print("→ Peak-prime alignment not statistically significant here.")

    # BK correlation on all lags
    Bp_all = (np.log(lags)**2) / lags
    r_all, pv_all = pearsonr(vals, Bp_all)
    print(f"\nBK correlation (all {MAX_LAG} lags): r = {r_all:.4f}, p = {pv_all:.3e}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 4))
    fig.suptitle("Blind Peak Detection Test", fontsize=13)

    axes[0].bar(lags, vals, color=['tomato' if l in prime_set else 'steelblue'
                                    for l in lags], alpha=0.8, width=0.6)
    for l in top_lags:
        axes[0].axvline(l, color='green', lw=1, alpha=0.5, ls='--')
    axes[0].set_xlabel('Lag h')
    axes[0].set_ylabel('C(h)')
    axes[0].set_title('C(h) spectrum\nRed=prime lags | Green=top-k detected')
    axes[0].legend(handles=[
        plt.Rectangle((0,0),1,1, color='tomato', alpha=0.8, label='Prime lag'),
        plt.Line2D([0],[0], color='green', ls='--', label=f'Top-{TOP_K} detected'),
    ], fontsize=9)

    Bp_full = (np.log(lags)**2) / lags
    axes[1].scatter(Bp_full, vals,
                    c=['tomato' if l in prime_set else 'steelblue' for l in lags],
                    s=50, alpha=0.8, zorder=5)
    axes[1].set_xlabel('B(h) = (log h)²/h')
    axes[1].set_ylabel('C(h) observed')
    axes[1].set_title(f'All lags: r = {r_all:.4f}\n(Red = prime lags)')
    axes[1].axhline(0, color='gray', lw=0.8, ls='--')

    plt.tight_layout()
    plt.savefig('results_blind_test.png', dpi=150)
    print("\nSaved: results_blind_test.png")

if __name__ == "__main__":
    main()
