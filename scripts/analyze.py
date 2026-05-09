"""
analyze.py — Main BK amplitude correlation test
================================================
Usage:
    python scripts/analyze.py zeros3.txt
    python scripts/analyze.py          # tries zeros3.txt, zeros2.txt, zeros4.txt

Computational observation only. Not a confirmed result.
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def load_zeros(path):
    """Load Odlyzko zero file, skipping any non-numeric header lines."""
    values = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                values.append(float(line))
            except ValueError:
                # Skip header lines like "Values of imaginary parts..."
                continue
    if not values:
        raise ValueError(f"No numeric values found in {path}")
    return np.array(values)


def find_zeros_file(arg=None):
    """Resolve zero file path from argument or fallback list."""
    candidates = [arg] if arg else []
    candidates += ["zeros3.txt", "zeros2.txt", "zeros4.txt"]
    for p in candidates:
        if p and os.path.exists(p):
            return p
    raise FileNotFoundError(
        "No zero file found. Download from:\n"
        "  http://www-users.cse.umn.edu/~odlyzko/zeta_tables/\n"
        "Then run: python scripts/analyze.py zeros3.txt"
    )


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    path = find_zeros_file(arg)
    print(f"Loading: {path}")

    gamma = load_zeros(path)
    N = len(gamma)
    T = gamma[N // 2]  # midpoint as height estimate
    print(f"  N = {N:,} zeros | T ≈ {T:.0f}")

    # Spacings and centering
    delta = np.diff(gamma)
    delta -= delta.mean()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Empirical covariance A(p)
    A = np.array([
        np.mean(delta[:-p] * delta[p:]) if len(delta) > p + 10 else 0.0
        for p in primes
    ])

    # BK predictor B(p) = (log p)^2 / p
    B = (np.log(primes) ** 2) / np.array(primes, float)

    r, pval = pearsonr(A, B)

    print(f"\nResults ({os.path.basename(path)}):")
    print(f"  Pearson r = {r:.4f}")
    print(f"  Naive p   = {pval:.2e}  (uncorrected — see LIMITATIONS.md)")
    print(f"  R(p) mean = {np.mean(A / B):.2f}  (A/B ratio, no theoretical derivation)")
    print()
    print("Prime-by-prime:")
    print(f"  {'p':>4}  {'A(p)':>10}  {'B(p)':>10}  {'R=A/B':>8}")
    for p, a, b in zip(primes, A, B):
        print(f"  {p:>4}  {a:>10.4f}  {b:>10.4f}  {a/b:>8.2f}")

    print()
    print("CAVEATS:")
    print("  Computational observation only — not a confirmed result.")
    print("  Normalization choice (high-T) was selected post-hoc.")
    print("  Naive p-value assumes independence (violated).")
    print("  Not a proof of the Riemann Hypothesis.")

    # Plot
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(B, A, color='steelblue', s=60, edgecolors='white', linewidths=0.5, zorder=3)
    for i, p in enumerate(primes):
        ax.annotate(f'p={p}', (B[i], A[i]), textcoords='offset points',
                    xytext=(6, 3), fontsize=7, color='#888')
    m, b_coef = np.polyfit(B, A, 1)
    xs = np.linspace(B.min() * 0.9, B.max() * 1.05, 100)
    ax.plot(xs, m * xs + b_coef, '--', color='steelblue', alpha=0.5, lw=1.2)
    ax.set_xlabel('B(p) = (log p)² / p')
    ax.set_ylabel('A(p) = spacing covariance')
    ax.set_title(f'BK amplitude test — {os.path.basename(path)} — r={r:.4f}')
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    out = f"scatter_{os.path.splitext(os.path.basename(path))[0]}.png"
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"Plot saved: {out}")


if __name__ == "__main__":
    main()
