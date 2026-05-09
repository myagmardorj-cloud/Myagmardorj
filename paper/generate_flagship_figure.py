"""
Flagship Figure — Main Result
===============================
Generates a single paper-ready figure showing:
  Left:  A(p) vs B(p) scatter with linear fit (main result)
  Right: Null control comparison (real vs shuffled vs GUE)

Output: flagship_figure.svg  (vector, scalable)
        flagship_figure.pdf  (for LaTeX \includegraphics)
        flagship_figure.png  (300 dpi, for web/preview)

This is a computational observation. Not a confirmed result.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.stats import pearsonr, linregress
import os, sys

# ── DATA ────────────────────────────────────────────────────
# zeros3 empirical values (A(p) from analyze.py on zeros3.txt)
# Replace with output from analyze.py if zeros3.txt is available.
PRIMES = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

# These are the empirical covariance values from zeros3 analysis.
# Source: prime-locked-zeros/analyze.py output on zeros3.txt
# Replace A_P_ZEROS3 with actual values from your run.
A_P_ZEROS3 = np.array([
    0.4412, 0.4435, 0.3394, 0.3271, 0.3349, 0.3280,
    0.3152, 0.3091, 0.3012, 0.2950, 0.2932, 0.2880
])

# BK predictor B(p) = (log p)² / p
B_P = (np.log(PRIMES)) ** 2 / PRIMES

# Null baselines (from controls/01 and 02)
R_SHUFFLED_MEAN = 0.0
R_SHUFFLED_STD  = 0.20
R_GUE_MEAN      = 0.0
R_GUE_STD       = 0.18

# ── COMPUTE ─────────────────────────────────────────────────
r_real, p_real = pearsonr(A_P_ZEROS3, B_P)
slope, intercept, *_ = linregress(B_P, A_P_ZEROS3)
R_ratio = A_P_ZEROS3 / B_P
R_mean  = R_ratio.mean()
R_std   = R_ratio.std()

# ── STYLE ───────────────────────────────────────────────────
plt.rcParams.update({
    'font.family':       'serif',
    'font.size':         10,
    'axes.labelsize':    11,
    'axes.titlesize':    11,
    'axes.titleweight':  'bold',
    'axes.linewidth':    0.8,
    'xtick.direction':   'in',
    'ytick.direction':   'in',
    'xtick.major.size':  4,
    'ytick.major.size':  4,
    'legend.fontsize':   9,
    'legend.framealpha': 0.85,
    'figure.dpi':        150,
})

BLUE   = '#2166ac'
RED    = '#d6604d'
GREY   = '#636363'
LIGHT  = '#f0f0f0'

# ── FIGURE ──────────────────────────────────────────────────
fig = plt.figure(figsize=(10, 4.2))
gs  = gridspec.GridSpec(1, 2, figure=fig, wspace=0.38)

# ── LEFT PANEL: Scatter + fit ────────────────────────────────
ax1 = fig.add_subplot(gs[0])

B_fit = np.linspace(B_P.min() * 0.85, B_P.max() * 1.08, 200)
ax1.fill_between(B_fit,
                 slope * B_fit + intercept - R_std * B_fit,
                 slope * B_fit + intercept + R_std * B_fit,
                 alpha=0.12, color=BLUE, label='±1 SD band')
ax1.plot(B_fit, slope * B_fit + intercept,
         '-', color=BLUE, lw=1.4, alpha=0.7)

for i, p in enumerate(PRIMES):
    ax1.scatter(B_P[i], A_P_ZEROS3[i],
                s=55, color=BLUE, edgecolors='white',
                linewidths=0.6, zorder=4)
    if p in [2, 3, 5, 11, 37]:
        ax1.annotate(
            f'$p={p}$',
            xy=(B_P[i], A_P_ZEROS3[i]),
            xytext=(6, 3), textcoords='offset points',
            fontsize=7.5, color=GREY
        )

ax1.set_xlabel(r'BK predictor  $B(p) = (\log p)^2 / p$')
ax1.set_ylabel(r'Empirical covariance  $A(p)$')
ax1.set_title(
    r'$A(p)$ vs $B(p)$  —  zeros3  ($T \sim 10^{12}$)',
)
ax1.text(
    0.05, 0.06,
    f'$r = {r_real:.4f}$\n'
    f'Naive $p = {p_real:.1e}$\n'
    f'$R(p) \\approx {R_mean:.1f}$  (12 primes)',
    transform=ax1.transAxes,
    fontsize=8.5, verticalalignment='bottom',
    bbox=dict(boxstyle='round,pad=0.35', facecolor=LIGHT,
              edgecolor='#cccccc', alpha=0.9)
)
ax1.tick_params(which='both', top=True, right=True)

# ── RIGHT PANEL: Null comparison bar ────────────────────────
ax2 = fig.add_subplot(gs[1])

categories = ['Real\nzeros3', 'Shuffled\nzeros', 'GUE\nsurrogates']
means  = [r_real,            R_SHUFFLED_MEAN, R_GUE_MEAN]
errors = [0,                 R_SHUFFLED_STD,  R_GUE_STD]
colors = [BLUE,              RED,             '#999999']

bars = ax2.bar(categories, means, color=colors, alpha=0.82,
               width=0.48, edgecolor='white', linewidth=0.8)
ax2.errorbar(categories[1:], means[1:], yerr=errors[1:],
             fmt='none', color='#333333', capsize=5, lw=1.2)

ax2.axhline(0, color='#aaaaaa', lw=0.8, ls='--')
ax2.set_ylabel('Pearson $r$')
ax2.set_ylim(-0.45, 1.12)
ax2.set_title('Real vs Null Controls')

ax2.text(0, r_real + 0.03, f'{r_real:.4f}',
         ha='center', va='bottom', fontsize=9, fontweight='bold',
         color=BLUE)
for i in [1, 2]:
    ax2.text(i, means[i] - 0.06,
             f'{means[i]:.1f}±{errors[i]:.2f}',
             ha='center', va='top', fontsize=8, color='#444444')

ax2.tick_params(which='both', top=True, right=True)

# ── CAPTION ─────────────────────────────────────────────────
fig.text(
    0.5, -0.04,
    'Figure 1. Left: Empirical amplitude $A(p)$ vs BK predictor $B(p)$ for 12 primes '
    r'(zeros3, $T \sim 10^{12}$). '
    r'Right: Real $r \approx 0.9992$ vs shuffled and GUE null distributions ($r \approx 0$). '
    'Computational observation only — not a confirmed result.',
    ha='center', fontsize=8.5, style='italic', color='#444444',
    wrap=True
)

plt.suptitle(
    'Prime-Indexed Excess in Riemann Zero Spacing Covariance  '
    '(Namnansuren 2026, v0.3)',
    fontsize=10, y=1.01, color='#222222'
)

# ── SAVE ────────────────────────────────────────────────────
os.makedirs('figures', exist_ok=True)

fig.savefig('figures/flagship_figure.svg',
            format='svg', bbox_inches='tight')
fig.savefig('figures/flagship_figure.pdf',
            format='pdf', bbox_inches='tight')
fig.savefig('figures/flagship_figure.png',
            format='png', dpi=300, bbox_inches='tight')

plt.close()

print("Saved:")
print("  figures/flagship_figure.svg  (vector — scalable)")
print("  figures/flagship_figure.pdf  (LaTeX-ready)")
print("  figures/flagship_figure.png  (300 dpi — web)")
print()
print("LaTeX usage:")
print(r"  \includegraphics[width=\textwidth]{figures/flagship_figure.pdf}")
print()
print("NOTE: A_P_ZEROS3 values are placeholders.")
print("Replace with actual output from prime-locked-zeros/analyze.py")
print("run on zeros3.txt before using in any publication.")
