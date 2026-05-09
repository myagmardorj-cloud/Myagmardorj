"""
Control Test 4: Window Effects
================================
Question: Are the results sensitive to window choice?

Method: Test with different window sizes, Hann/Blackman
windowing, and varying cutoff T values. A genuine signal
should be stable; an artifact may appear only in specific
window configurations.
"""

import numpy as np
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]

def spacing_covariance(gamma, prime_lags):
    delta = np.diff(gamma)
    delta -= delta.mean()
    covs = []
    for p in prime_lags:
        if len(delta) > p + 10:
            cov = np.mean(delta[:-p] * delta[p:])
        else:
            cov = 0.0
        covs.append(cov)
    return np.array(covs)

def spacing_covariance_windowed(gamma, prime_lags, window_fn=None):
    """Apply optional window function to spacings before covariance."""
    delta = np.diff(gamma)
    delta -= delta.mean()
    n = len(delta)
    if window_fn is not None:
        w = window_fn(n)
        delta = delta * w
    covs = []
    for p in prime_lags:
        if n > p + 10:
            cov = np.mean(delta[:-p] * delta[p:])
        else:
            cov = 0.0
        covs.append(cov)
    return np.array(covs)

def bk_predictor(primes):
    lp = np.log(primes)
    return lp**2 / primes

def main():
    print("=" * 55)
    print("Control Test 4: Window & Stability Effects")
    print("=" * 55)

    # Generate synthetic data (replace with real zeros file if available)
    rng = np.random.default_rng(42)
    n = 10000
    # Wigner-like spacings with slight prime structure
    spacings = np.abs(rng.standard_normal(n)) + 0.3
    gamma = 1e12 + np.cumsum(spacings)
    Bp = bk_predictor(np.array(PRIMES))

    print("\n1. Window function comparison:")
    windows = {
        'None (rectangular)': None,
        'Hann':      np.hanning,
        'Blackman':  np.blackman,
        'Hamming':   np.hamming,
    }
    window_results = {}
    for name, wfn in windows.items():
        Ap = spacing_covariance_windowed(gamma, PRIMES, wfn)
        r, pv = pearsonr(Ap, Bp)
        window_results[name] = r
        print(f"  {name:25} r = {r:.4f}  p = {pv:.3e}")

    print("\n2. Varying window size (fraction of dataset):")
    size_results = {}
    fractions = [0.2, 0.3, 0.5, 0.7, 1.0]
    for frac in fractions:
        n_use = int(len(gamma) * frac)
        g_sub = gamma[:n_use]
        Ap = spacing_covariance(g_sub, PRIMES)
        r, pv = pearsonr(Ap, Bp)
        size_results[frac] = r
        print(f"  Fraction {frac:.1f} (N={n_use:,}): r = {r:.4f}")

    print("\n3. Subwindow stability (5 non-overlapping blocks):")
    block_size = len(gamma) // 5
    block_r = []
    for i in range(5):
        g_block = gamma[i*block_size:(i+1)*block_size]
        Ap = spacing_covariance(g_block, PRIMES)
        r, _ = pearsonr(Ap, Bp)
        block_r.append(r)
        print(f"  Block {i+1}: r = {r:.4f}")
    print(f"  Std across blocks: {np.std(block_r):.4f}")

    print(f"\nCONCLUSION:")
    r_range = max(window_results.values()) - min(window_results.values())
    if r_range < 0.3:
        print(f"  → r is stable across window functions (range = {r_range:.3f}).")
        print(f"  → Window effect is not the primary driver.")
    else:
        print(f"  → r varies significantly with window choice (range = {r_range:.3f}).")
        print(f"  → Window/Fourier leakage may be contributing to the signal.")

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle("Window & Stability Tests", fontsize=13)

    # Window comparison
    names = list(window_results.keys())
    vals  = list(window_results.values())
    axes[0].barh(names, vals, color=['steelblue']*len(names))
    axes[0].set_xlabel('Pearson r')
    axes[0].set_title('Window Function Comparison')
    axes[0].axvline(0, color='gray', lw=0.8)

    # Size scaling
    axes[1].plot(fractions, list(size_results.values()), 'o-', color='steelblue', lw=2)
    axes[1].set_xlabel('Fraction of dataset used')
    axes[1].set_ylabel('Pearson r')
    axes[1].set_title('Window Size Stability')
    axes[1].grid(True, alpha=0.3)

    # Block stability
    axes[2].bar(range(1,6), block_r, color='steelblue', alpha=0.8)
    axes[2].axhline(np.mean(block_r), color='red', ls='--', lw=1.5,
                    label=f'Mean r = {np.mean(block_r):.3f}')
    axes[2].set_xlabel('Block index')
    axes[2].set_ylabel('Pearson r')
    axes[2].set_title('Subwindow Block Stability')
    axes[2].legend()

    plt.tight_layout()
    plt.savefig('results_window_effects.png', dpi=150)
    print("\nSaved: results_window_effects.png")

if __name__ == "__main__":
    main()
