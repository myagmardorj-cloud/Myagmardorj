"""
Control Test 2: GUE Surrogate
================================
H0: If the signal were pure GUE (no prime structure),
    what would r look like?

Method: Generate GUE eigenvalue spacings and run the
same BK amplitude test. True prime structure should
only appear in actual Riemann zeros, not GUE surrogates.
"""

import numpy as np
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37]
N_SIMULATIONS = 500
N_ZEROS = 10000   # match dataset size

def gue_spacings(n, rng):
    """
    Approximate GUE spacings using the Wigner surmise.
    P(s) = (π/2) s exp(−πs²/4)
    """
    # Inverse transform sampling of Wigner surmise
    u = rng.uniform(0, 1, n)
    # CDF^{-1}: solve 1 - exp(-πs²/4) = u
    s = np.sqrt(-4/np.pi * np.log(1 - u + 1e-10))
    return s

def build_zeros_from_spacings(spacings, T_start=1e12):
    """Convert spacings to zero heights."""
    return T_start + np.cumsum(spacings)

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

def bk_predictor(primes):
    lp = np.log(primes)
    return lp**2 / primes

def main():
    print("=" * 55)
    print("Control Test 2: GUE Surrogate Simulation")
    print("=" * 55)
    print(f"Generating {N_SIMULATIONS} GUE surrogates (n={N_ZEROS} each)...")

    rng = np.random.default_rng(42)
    Bp = bk_predictor(np.array(PRIMES))

    r_gue = []
    for i in range(N_SIMULATIONS):
        spacings = gue_spacings(N_ZEROS, rng)
        gamma = build_zeros_from_spacings(spacings)
        Ap = spacing_covariance(gamma, PRIMES)
        r, _ = pearsonr(Ap, Bp)
        r_gue.append(r)
        if (i+1) % 100 == 0:
            print(f"  {i+1}/{N_SIMULATIONS}...")

    r_gue = np.array(r_gue)

    # Reference: published result
    r_real = 0.6847  # zeros1 result (reanalyzed)

    print(f"\nGUE SURROGATE DISTRIBUTION:")
    print(f"  Mean r: {r_gue.mean():.4f}")
    print(f"  Std  r: {r_gue.std():.4f}")
    print(f"  95th percentile: {np.percentile(r_gue, 95):.4f}")
    print(f"  Max r:  {r_gue.max():.4f}")
    print(f"\nREAL DATA (zeros1): r = {r_real:.4f}")
    p_emp = np.mean(r_gue >= r_real)
    print(f"Fraction of GUE surrogates ≥ {r_real}: {p_emp:.4f}")

    print(f"\nCONCLUSION:")
    if p_emp < 0.05:
        print(f"  → Real r={r_real:.4f} is unlikely under pure GUE.")
        print(f"  → Suggests prime-specific structure beyond GUE baseline.")
    else:
        print(f"  → Real r is consistent with pure GUE. Signal may be artifact.")

    # Plot
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(r_gue, bins=40, color='steelblue', alpha=0.75, label='GUE surrogates')
    ax.axvline(r_real, color='red', lw=2.5, ls='--', label=f'Real zeros1 r = {r_real}')
    ax.set_xlabel('Pearson r', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('GUE Surrogate vs Real: BK Amplitude Correlation', fontsize=13)
    ax.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig('results_gue_surrogate.png', dpi=150)
    print("\nSaved: results_gue_surrogate.png")

if __name__ == "__main__":
    main()
