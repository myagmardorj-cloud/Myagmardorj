"""
Control Test 8: Robustness Analysis
======================================
Tests whether the observed correlation is stable under
systematic variations of key parameters.

Tests:
  8a. Zero range variation    — different N values, different start positions
  8b. Prime cutoff variation  — 6, 9, 12, 15 primes
  8c. Normalization variants  — 4 different tau_p formulas
  8d. Random subsets          — 50 random sub-samples at each N

If r remains high across all variants, the signal is robust.
If r collapses under any variant, that variant is a confound.

Computational observation only. Not a confirmed result.
"""

import numpy as np
from scipy.stats import pearsonr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, sys

# ── CONFIG ──────────────────────────────────────────────────
ZEROS_FILE   = sys.argv[1] if len(sys.argv) > 1 else "zeros3.txt"
ALL_PRIMES   = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
N_SIZES      = [500, 1_000, 2_000, 3_000, 5_000, 8_000, 10_000]
N_SUBSETS    = 50
SEED         = 42
# ────────────────────────────────────────────────────────────

rng = np.random.default_rng(SEED)

NORM_VARIANTS = {
    "high-T (used)":   lambda p, T: np.log(p) / np.log(T / (2 * np.pi)),
    "low-T (wrong)":   lambda p, T: np.log(p) / (2 * np.pi),
    "log-only":        lambda p, T: np.log(p),
    "1/sqrt(p)":       lambda p, T: 1.0 / np.sqrt(p),
}


def load_zeros(path):
    for p in [path, "zeros3.txt", "zeros2.txt", "zeros4.txt"]:
        if p and os.path.exists(p):
            g = np.loadtxt(p)
            print(f"  Loaded {len(g):,} zeros from {p}")
            return g
    print("  [INFO] No zero file — using synthetic spacing.")
    sp = np.sqrt(-4 / np.pi * np.log(1 - rng.uniform(0, 1, 12_000) + 1e-10))
    return 1e12 + np.cumsum(sp)


def spacing_cov(gamma, lags):
    d = np.diff(gamma)
    d -= d.mean()
    return np.array([
        np.mean(d[:-h] * d[h:]) if len(d) > h + 10 else 0.0
        for h in lags
    ])


def bk(lags):
    lp = np.log(np.array(lags, float))
    return lp ** 2 / np.array(lags, float)


print("=" * 60)
print("TEST 8: Robustness Analysis")
print("Experimental — not a confirmed result")
print("=" * 60)

gamma_all = load_zeros(ZEROS_FILE)
T_approx  = gamma_all[len(gamma_all) // 2]   # midpoint height estimate

PRIMES_12 = ALL_PRIMES[:12]
Bp_12     = bk(PRIMES_12)


# ── 8a: ZERO RANGE VARIATION ────────────────────────────────
print("\n[8a] Zero range variation (different N, different start)")
range_results = {}
for N in N_SIZES:
    g = gamma_all[:min(N, len(gamma_all))]
    Ap = spacing_cov(g, PRIMES_12)
    r, _ = pearsonr(Ap, Bp_12)
    range_results[N] = r
    print(f"  N = {N:>6,}  r = {r:.4f}")

# Also test starting from middle
mid = len(gamma_all) // 2
for N in [1_000, 3_000, 5_000]:
    g = gamma_all[mid: mid + min(N, len(gamma_all) - mid)]
    if len(g) > 50:
        Ap = spacing_cov(g, PRIMES_12)
        r, _ = pearsonr(Ap, Bp_12)
        range_results[f"{N}_mid"] = r
        print(f"  N = {N:>6,} (mid)  r = {r:.4f}")


# ── 8b: PRIME CUTOFF VARIATION ──────────────────────────────
print("\n[8b] Prime cutoff variation")
cutoff_results = {}
for k in [6, 9, 12, 15]:
    primes_k = ALL_PRIMES[:min(k, len(ALL_PRIMES))]
    Bp_k = bk(primes_k)
    Ap_k = spacing_cov(gamma_all, primes_k)
    r, p = pearsonr(Ap_k, Bp_k)
    cutoff_results[k] = r
    print(f"  {k:2d} primes (up to {primes_k[-1]:3d}):  r = {r:.4f}  p = {p:.2e}")


# ── 8c: NORMALIZATION VARIANTS ──────────────────────────────
print("\n[8c] Normalization variants")
norm_results = {}
for name, tau_fn in NORM_VARIANTS.items():
    try:
        lags = np.array(PRIMES_12, float)
        tau  = np.array([tau_fn(p, T_approx) for p in lags])
        Bp_v = tau ** 2 / lags            # BK form with this normalisation
        Ap   = spacing_cov(gamma_all, PRIMES_12)
        r, p = pearsonr(Ap, Bp_v)
        norm_results[name] = r
        print(f"  {name:20s}  r = {r:.4f}  p = {p:.2e}")
    except Exception as e:
        print(f"  {name:20s}  ERROR: {e}")
        norm_results[name] = np.nan


# ── 8d: RANDOM SUBSETS ──────────────────────────────────────
print(f"\n[8d] Random subsets ({N_SUBSETS} iterations per N)")
subset_results = {}
for N in [1_000, 3_000, 5_000]:
    rs = []
    for _ in range(N_SUBSETS):
        start = rng.integers(0, max(1, len(gamma_all) - N - 10))
        g = gamma_all[start: start + N]
        Ap = spacing_cov(g, PRIMES_12)
        r, _ = pearsonr(Ap, Bp_12)
        rs.append(r)
    arr = np.array(rs)
    subset_results[N] = arr
    print(f"  N = {N:>6,}  mean r = {arr.mean():.4f}  std = {arr.std():.4f}  "
          f"min = {arr.min():.4f}  max = {arr.max():.4f}")


# ── SUMMARY ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("ROBUSTNESS SUMMARY")
print("=" * 60)

n_range  = [v for k, v in range_results.items() if isinstance(k, int)]
r_stable = (max(n_range) - min(n_range)) < 0.3
print(f"  Zero range:       r in [{min(n_range):.4f}, {max(n_range):.4f}]  "
      f"({'STABLE' if r_stable else 'VARIABLE'})")

n_cutoff = list(cutoff_results.values())
c_stable = (max(n_cutoff) - min(n_cutoff)) < 0.3
print(f"  Prime cutoff:     r in [{min(n_cutoff):.4f}, {max(n_cutoff):.4f}]  "
      f"({'STABLE' if c_stable else 'VARIABLE'})")

ht = norm_results.get("high-T (used)", np.nan)
lt = norm_results.get("low-T (wrong)", np.nan)
print(f"  Norm (high-T):    r = {ht:.4f}  ← used in main analysis")
print(f"  Norm (low-T):     r = {lt:.4f}  ← known to give weak signal")
print(f"  Normalization sensitive: {'YES — high-T essential' if abs(ht - lt) > 0.2 else 'NO'}")

for N, arr in subset_results.items():
    print(f"  Subsets N={N:>5,}: mean r = {arr.mean():.4f}  std = {arr.std():.4f}")

print("\nCAVEATS:")
print("  Normalization sensitivity is a known confound (see LIMITATIONS.md).")
print("  r stability across N does not rule out finite-range artifacts.")
print("  These tests are necessary but not sufficient for a confirmed result.")
print("=" * 60)


# ── PLOTS ───────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Test 8: Robustness Analysis", fontsize=12, fontweight="bold")

# 8a
int_keys = [k for k in range_results if isinstance(k, int)]
axes[0, 0].plot(int_keys, [range_results[k] for k in int_keys],
                "o-", color="steelblue", lw=2, label="First N zeros")
mid_keys = [k for k in range_results if isinstance(k, str)]
if mid_keys:
    mid_ns = [int(k.split("_")[0]) for k in mid_keys]
    axes[0, 0].plot(mid_ns, [range_results[k] for k in mid_keys],
                    "s--", color="orange", lw=1.5, label="Mid-block zeros")
axes[0, 0].set_xscale("log")
axes[0, 0].set_xlabel("N zeros used")
axes[0, 0].set_ylabel("Pearson r")
axes[0, 0].set_title("8a: Zero Range")
axes[0, 0].axhline(0.8, color="gray", ls=":", lw=1, label="r=0.8")
axes[0, 0].legend(fontsize=8)
axes[0, 0].grid(True, alpha=0.3)

# 8b
axes[0, 1].plot(list(cutoff_results.keys()), list(cutoff_results.values()),
                "o-", color="steelblue", lw=2)
axes[0, 1].set_xlabel("Number of primes included")
axes[0, 1].set_ylabel("Pearson r")
axes[0, 1].set_title("8b: Prime Cutoff")
axes[0, 1].grid(True, alpha=0.3)

# 8c
norm_labels = list(norm_results.keys())
norm_vals   = [norm_results[k] for k in norm_labels]
colors_c    = ["steelblue" if "used" in k else "tomato" for k in norm_labels]
axes[1, 0].barh(norm_labels, norm_vals, color=colors_c, alpha=0.8)
axes[1, 0].axvline(0, color="gray", lw=0.8)
axes[1, 0].set_xlabel("Pearson r")
axes[1, 0].set_title("8c: Normalization Variants")

# 8d
for N, arr in subset_results.items():
    axes[1, 1].hist(arr, bins=20, alpha=0.6, label=f"N={N:,}")
axes[1, 1].set_xlabel("Pearson r (random subsets)")
axes[1, 1].set_ylabel("Count")
axes[1, 1].set_title("8d: Random Subsets")
axes[1, 1].legend(fontsize=8)

plt.tight_layout()
plt.savefig("results_08_robustness.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nPlot saved: results_08_robustness.png")
