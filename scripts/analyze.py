"""
analyze.py — BK amplitude correlation test with high-T unfolding
Usage: python scripts/analyze.py zeros_ht.txt
"""
import sys, os, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def load_zeros(path):
    """Load Odlyzko zero file — handles headers and offset formats."""
    offset = 0.0
    values = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if 'gamma -' in line.lower() or 'values of gamma' in line.lower():
                m = re.search(r'gamma\s*-\s*([\d,]+)', line, re.IGNORECASE)
                if m:
                    offset = float(m.group(1).replace(',', ''))
                continue
            try:
                values.append(float(line))
            except ValueError:
                continue
    if not values:
        raise ValueError(f"No numeric data in {path}")
    arr = np.array(values)
    if offset > 0 and arr.mean() < 1e6:
        arr = arr + offset
    return arr


def find_zeros_file(arg=None):
    candidates = [arg] if arg else []
    candidates += ["zeros_ht.txt", "zeros3.txt", "zeros2.txt", "zeros4.txt"]
    for p in candidates:
        if p and os.path.exists(p):
            return p
    raise FileNotFoundError(
        "No zero file found.\n"
        "Download from: http://www-users.cse.umn.edu/~odlyzko/zeta_tables/\n"
        "Zeros number 10^12+1 through 10^12+10^4 [text]"
    )


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    path = find_zeros_file(arg)
    print(f"Loading: {path}")

    gamma = load_zeros(path)
    N = len(gamma)
    T = gamma[N // 2]
    print(f"  N = {N:,} zeros | T ≈ {T:,.0f}")

    # HIGH-T UNFOLDING: normalize spacings by local mean spacing
    # Mean spacing at height T ≈ 2π / log(T/2π)
    log_T = np.log(T / (2 * np.pi))
    mean_spacing = 2 * np.pi / log_T
    print(f"  log(T/2π) = {log_T:.4f} | mean spacing ≈ {mean_spacing:.6f}")

    # Raw spacings
    raw_delta = np.diff(gamma)

    # Unfolded spacings (dimensionless)
    delta = raw_delta / mean_spacing
    delta -= delta.mean()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Empirical amplitude A(p) — covariance at prime lag p
    A = np.array([np.mean(delta[:-p] * delta[p:]) for p in primes])

    # High-T normalized BK predictor
    # τ_p = log(p) / log(T/2π)
    tau = np.log(primes) / log_T
    B = tau ** 2 / np.array(primes, float)

    r, pval = pearsonr(A, B)

    print(f"\nResults ({os.path.basename(path)}) — HIGH-T UNFOLDED:")
    print(f"  Pearson r = {r:.4f}")
    print(f"  Naive p   = {pval:.2e}  (uncorrected — see LIMITATIONS.md)")
    R = A / B
    print(f"  R(p) mean = {np.nanmean(R[np.isfinite(R)]):.2f}  (A/B ratio, no theoretical derivation)")
    print()
    print(f"  {'p':>4}  {'A(p)':>12}  {'B(p)':>12}  {'R=A/B':>8}")
    for p, a, b in zip(primes, A, B):
        print(f"  {p:>4}  {a:>12.6f}  {b:>12.6f}  {a/b:>8.2f}")

    print("\nCAVEATS:")
    print("  Computational observation only — not a confirmed result.")
    print("  High-T normalization selected post-hoc (selection bias risk).")
    print("  Naive p-value assumes independence (violated — autocorrelated).")
    print("  n=12 primes: small sample, outlier sensitivity.")
    print("  Not a proof of the Riemann Hypothesis.")

    # Plot
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(B, A, color='steelblue', s=60, edgecolors='white', lw=0.5, zorder=3)
    for i, p in enumerate(primes):
        ax.annotate(f'p={p}', (B[i], A[i]), textcoords='offset points',
                    xytext=(6, 3), fontsize=7, color='#888')
    m, b0 = np.polyfit(B, A, 1)
    xs = np.linspace(B.min()*0.9, B.max()*1.05, 100)
    ax.plot(xs, m*xs+b0, '--', color='steelblue', alpha=0.5, lw=1.2)
    ax.set_xlabel('B(p) = τ_p² / p  (high-T)')
    ax.set_ylabel('A(p) = unfolded spacing covariance')
    ax.set_title(f'BK amplitude — {os.path.basename(path)} — r={r:.4f}')
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    out = f"scatter_{os.path.splitext(os.path.basename(path))[0]}.png"
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Plot saved: {out}")


if __name__ == "__main__":
    main()
