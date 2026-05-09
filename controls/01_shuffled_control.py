"""
Control Test 1: Shuffled Zeros
================================
H0: No prime-correlated structure in zero spacings.

Method: Randomly permute γₙ values and repeat the
full BK amplitude test. If r ≈ 0 for shuffled data,
the signal is in the ordering — not a marginal artifact.
"""

import numpy as np

def _safe_load(path):
    """Load Odlyzko zero file, skipping non-numeric header lines."""
    vals = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                vals.append(float(line))
            except ValueError:
                continue
    if not vals:
        raise ValueError(f"No numeric data in {path}")
    return __import__('numpy').array(vals)
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── CONFIG ──────────────────────────────────────────
ZEROS_FILE = "zeros3.txt"   # Odlyzko data file
N_SHUFFLES = 1000           # number of permutations
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]
# ────────────────────────────────────────────────────

def load_zeros(path):
    return _safe_load(path)

def spacing_covariance(gamma, prime_lags):
    """Compute C(p) for each prime lag p."""
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

def bk_predictor(primes):
    lp = np.log(primes)
    return lp**2 / primes

def run_test(gamma, primes):
    Ap = spacing_covariance(gamma, primes)
    Bp = bk_predictor(np.array(primes))
    r, pv = pearsonr(Ap, Bp)
    return r, pv, Ap

def main():
    print("=" * 55)
    print("Control Test 1: Shuffled Zeros Permutation Test")
    print("=" * 55)

    # Load data
    try:
        gamma = load_zeros(ZEROS_FILE)
    except FileNotFoundError:
        print(f"[INFO] {ZEROS_FILE} not found.")
        print("[INFO] Generating synthetic GUE-like zeros for demo...")
        rng = np.random.default_rng(42)
        # Synthetic: GUE-like spacings (no prime structure)
        gamma = np.cumsum(np.abs(rng.standard_normal(12000)) + 0.5)
        gamma = gamma / gamma.max() * 1e12

    print(f"Loaded {len(gamma):,} zeros")
    T_approx = gamma.mean()
    print(f"Approx height T ≈ {T_approx:.2e}")

    # Real data result
    r_real, pv_real, Ap_real = run_test(gamma, PRIMES)
    print(f"\nREAL DATA:    r = {r_real:.4f}  p = {pv_real:.3e}")

    # Null distribution: shuffled
    print(f"\nRunning {N_SHUFFLES} shuffle controls...")
    r_null = []
    rng = np.random.default_rng(0)
    for i in range(N_SHUFFLES):
        gamma_sh = gamma.copy()
        rng.shuffle(gamma_sh)
        gamma_sh = np.sort(gamma_sh)  # keep sorted (spacings well-defined)
        # Actually shuffle spacings directly
        delta = np.diff(gamma)
        rng.shuffle(delta)
        gamma_sh = np.concatenate([[gamma[0]], gamma[0] + np.cumsum(np.abs(delta))])
        r_sh, _, _ = run_test(gamma_sh, PRIMES)
        r_null.append(r_sh)
        if (i+1) % 200 == 0:
            print(f"  {i+1}/{N_SHUFFLES} done...")

    r_null = np.array(r_null)

    # Results
    p_empirical = np.mean(r_null >= r_real)
    print(f"\nNULL DISTRIBUTION:")
    print(f"  Mean r (shuffled):   {r_null.mean():.4f}")
    print(f"  Std  r (shuffled):   {r_null.std():.4f}")
    print(f"  Max  r (shuffled):   {r_null.max():.4f}")
    print(f"  Empirical p-value:   {p_empirical:.4f}")
    print(f"\nCONCLUSION:")
    if p_empirical < 0.05:
        print(f"  Real r={r_real:.4f} exceeds {100*(1-p_empirical):.1f}% of null dist.")
        print(f"  → Signal is NOT explained by marginal distribution alone.")
    else:
        print(f"  → Signal may be a marginal/ordering artifact.")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle("Shuffled Zeros Control Test", fontsize=13, fontweight='bold')

    axes[0].hist(r_null, bins=50, color='steelblue', alpha=0.7, label='Null (shuffled)')
    axes[0].axvline(r_real, color='red', lw=2, label=f'Real r = {r_real:.4f}')
    axes[0].set_xlabel('Pearson r')
    axes[0].set_ylabel('Count')
    axes[0].set_title('Null Distribution of r')
    axes[0].legend()

    Bp = bk_predictor(np.array(PRIMES))
    axes[1].scatter(Bp, Ap_real, color='red', s=60, zorder=5, label='Real data')
    axes[1].axhline(0, color='gray', lw=0.8, ls='--')
    for p, b, a in zip(PRIMES, Bp, Ap_real):
        axes[1].annotate(f'p={p}', (b, a), fontsize=7, ha='left')
    axes[1].set_xlabel('B(p) = (log p)²/p')
    axes[1].set_ylabel('C(p) observed')
    axes[1].set_title(f'Real: r = {r_real:.4f}')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig('results_shuffled_control.png', dpi=150)
    print("\nSaved: results_shuffled_control.png")

if __name__ == "__main__":
    main()
