"""
Control Test 7: Negative Controls
====================================
Three controls designed to FAIL if the signal is prime-specific.
If these produce r ~ 0 while real primes produce r ~ 0.99,
that is strong (but not conclusive) evidence the signal is
prime-indexed rather than an artifact.

Tests:
  7a. Composite indices  — replace primes with composites
  7b. Random phase zeros — synthetic data with no prime structure
  7c. Fake zero sets     — GUE eigenvalues, no arithmetic structure

Expected outcome:
  Real primes:      r varies: 0.45–0.68 (dataset-dependent)  (observed)
  Composite lags:   r ~ 0      (expected collapse)
  Random phases:    r ~ 0      (expected collapse)
  GUE eigenvalues:  r ~ 0      (expected collapse)

Computational observation only. Not a confirmed result.
Independent replication required.
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
import os, sys

# ── CONFIG ──────────────────────────────────────────────────
ZEROS_FILE = sys.argv[1] if len(sys.argv) > 1 else "zeros1.txt"
PRIMES     = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
COMPOSITES = [4, 6, 8, 9, 10, 14, 15, 16, 18, 20, 21, 22]  # same count
N_SYNTH    = 10_000
SEED       = 42
# ────────────────────────────────────────────────────────────

rng = np.random.default_rng(SEED)


def load_zeros(path):
    for p in [path, "zeros1.txt", "zeros_ht.txt", "zeros6.txt"]:
        if p and os.path.exists(p):
            g = _safe_load(p)
            print(f"  Loaded {len(g):,} zeros from {p}")
            return g
    print("  [INFO] No zero file found — using synthetic GUE spacing.")
    sp = np.sqrt(-4 / np.pi * np.log(1 - rng.uniform(0, 1, N_SYNTH) + 1e-10))
    return 1e12 + np.cumsum(sp)


def spacing_cov(gamma, lags):
    d = np.diff(gamma)
    d -= d.mean()
    return np.array([
        np.mean(d[:-h] * d[h:]) if len(d) > h + 10 else 0.0
        for h in lags
    ])


def bk_predictor(lags):
    lp = np.log(np.array(lags, float))
    return lp ** 2 / np.array(lags, float)


def gue_zeros(n, base=1e12):
    """Synthetic GUE zeros: Wigner-Dyson spacing, no arithmetic structure."""
    u = rng.uniform(0, 1, n)
    sp = np.sqrt(-4 / np.pi * np.log(1 - u + 1e-10))
    return base + np.cumsum(sp)


def random_phase_zeros(n, base=1e12):
    """Zeros with randomised spacing — destroys any residual structure."""
    sp = np.abs(rng.normal(loc=1.0, scale=0.3, size=n))
    return base + np.cumsum(sp)


# ── LOAD REAL ZEROS ─────────────────────────────────────────
print("=" * 60)
print("TEST 7: Negative Controls")
print("Experimental — not a confirmed result")
print("=" * 60)

gamma_real = load_zeros(ZEROS_FILE)

Bp_primes     = bk_predictor(PRIMES)
Bp_composites = bk_predictor(COMPOSITES)

Ap_real_primes     = spacing_cov(gamma_real, PRIMES)
Ap_real_composites = spacing_cov(gamma_real, COMPOSITES)

r_real_primes,     p_real_primes     = pearsonr(Ap_real_primes,     Bp_primes)
r_real_composites, p_real_composites = pearsonr(Ap_real_composites, Bp_composites)


# ── 7a: COMPOSITE LAGS ──────────────────────────────────────
print(f"\n[7a] Composite lag test")
print(f"  Real data / prime lags:      r = {r_real_primes:.4f}  (p = {p_real_primes:.2e})")
print(f"  Real data / composite lags:  r = {r_real_composites:.4f}  (p = {p_real_composites:.2e})")
collapse_a = abs(r_real_composites) < 0.5
print(f"  Collapse: {'YES — composite lags show no signal' if collapse_a else 'NO — signal present at composites too'}")


# ── 7b: RANDOM PHASE ZEROS ──────────────────────────────────
print(f"\n[7b] Random phase zeros test  (N = {N_SYNTH:,})")
gamma_rp = random_phase_zeros(N_SYNTH)
Ap_rp    = spacing_cov(gamma_rp, PRIMES)
r_rp, p_rp = pearsonr(Ap_rp, Bp_primes)
print(f"  Random-phase zeros / prime lags:  r = {r_rp:.4f}  (p = {p_rp:.2e})")
collapse_b = abs(r_rp) < 0.5
print(f"  Collapse: {'YES — no prime signal in random phases' if collapse_b else 'NO — unexpected signal'}")


# ── 7c: GUE EIGENVALUES ─────────────────────────────────────
print(f"\n[7c] GUE eigenvalue test  (N = {N_SYNTH:,})")
r_gue_vals = []
for _ in range(100):
    g_gue  = gue_zeros(N_SYNTH)
    Ap_gue = spacing_cov(g_gue, PRIMES)
    r_g, _ = pearsonr(Ap_gue, Bp_primes)
    r_gue_vals.append(r_g)
r_gue_arr = np.array(r_gue_vals)
print(f"  GUE mean r = {r_gue_arr.mean():.4f}  std = {r_gue_arr.std():.4f}")
print(f"  GUE 95th percentile = {np.percentile(r_gue_arr, 95):.4f}")
collapse_c = np.percentile(r_gue_arr, 95) < r_real_primes - 0.1
print(f"  Real r exceeds GUE 95th: {'YES' if collapse_c else 'NO'}")


# ── SUMMARY ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SUMMARY — Test 7: Negative Controls")
print("=" * 60)
results = [
    ("Real / prime lags",     r_real_primes,     "baseline"),
    ("Real / composite lags", r_real_composites, "COLLAPSE expected"),
    ("Random-phase zeros",    r_rp,              "COLLAPSE expected"),
    ("GUE mean r",            r_gue_arr.mean(),  "COLLAPSE expected"),
]
for label, val, note in results:
    print(f"  {label:30s}  r = {val:+.4f}   ({note})")

all_collapsed = collapse_a and collapse_b and collapse_c
print(f"\nAll expected collapses observed: {'YES' if all_collapsed else 'PARTIAL/NO'}")
print("\nCAVEATS:")
print("  These are computational observations only.")
print("  Negative control collapse is necessary but not sufficient")
print("  evidence for a genuine prime-specific signal.")
print("  Independent replication and asymptotic analysis required.")
print("=" * 60)


# ── PLOT ────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Test 7: Negative Controls — Expected to show r ≈ 0", fontsize=11)

# 7a: bar comparison
labels_a = ["Prime lags\n(real zeros)", "Composite lags\n(real zeros)"]
vals_a   = [r_real_primes, r_real_composites]
colors_a = ["steelblue", "tomato"]
axes[0].bar(labels_a, vals_a, color=colors_a, alpha=0.8, width=0.4)
axes[0].axhline(0, color="gray", lw=0.8, ls="--")
axes[0].set_ylabel("Pearson r")
axes[0].set_title("7a: Composite Lags")
axes[0].set_ylim(-0.3, 1.1)

# 7b: scatter
axes[1].scatter(Bp_primes, Ap_real_primes, color="steelblue",
                label=f"Real primes r={r_real_primes:.3f}", zorder=3)
axes[1].scatter(Bp_primes, Ap_rp, color="tomato", marker="x",
                label=f"Random-phase r={r_rp:.3f}", zorder=2)
axes[1].set_xlabel("B(p) predictor")
axes[1].set_ylabel("A(p) covariance")
axes[1].set_title("7b: Random Phase Zeros")
axes[1].legend(fontsize=8)

# 7c: GUE histogram
axes[2].hist(r_gue_arr, bins=25, color="steelblue", alpha=0.75,
             label="GUE null distribution")
axes[2].axvline(r_real_primes, color="tomato", lw=2,
                label=f"Real r = {r_real_primes:.4f}")
axes[2].axvline(np.percentile(r_gue_arr, 95), color="orange",
                lw=1.5, ls="--", label="GUE 95th pct")
axes[2].set_xlabel("Pearson r")
axes[2].set_ylabel("Count")
axes[2].set_title("7c: GUE Eigenvalues")
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig("results_07_negative_controls.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nPlot saved: results_07_negative_controls.png")
