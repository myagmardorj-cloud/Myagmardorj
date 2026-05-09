"""Bogomolny–Keating amplitude law шалгах"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Өгөгдөл (жишээ утгууд, бодит тооцооллоор солих)
primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37])
DeltaK = np.array([0.441, 0.443, 0.339, 0.327, 0.335, 0.328, 
                   0.315, 0.309, 0.301, 0.295, 0.293, 0.288])

# BK predictor: B(p) = (log p)² / p
B_p = (np.log(primes))**2 / primes

# Ratio R(p) = ΔK / B
R_p = DeltaK / B_p

# Scatter plot
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(B_p, DeltaK, c='red', s=80, edgecolors='black')
plt.xlabel(r'$B(p) = (\log p)^2 / p$')
plt.ylabel(r'$\Delta K(p)$')
plt.title('BK Amplitude Law: ΔK vs B(p)')

slope, intercept, r, p_val, _ = linregress(B_p, DeltaK)
plt.plot(B_p, slope*B_p + intercept, 'b--', 
         label=f'r = {r:.3f}, slope = {slope:.3f}')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1,2,2)
plt.plot(primes, R_p, 'o-', color='green', markersize=8)
plt.axhline(y=np.mean(R_p), color='r', linestyle='--',
            label=f'mean R = {np.mean(R_p):.3f}')
plt.xlabel('Prime p')
plt.ylabel(r'$R(p) = \Delta K(p) / B(p)$')
plt.title('BK Ratio (should be ~constant)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('results/figures/amplitude_scatter.png', dpi=150)
plt.savefig('results/figures/ratio_plot.png', dpi=150)
plt.show()

# Output
print("\n=== BK AMPLITUDE LAW TEST ===")
print(f"Pearson r = {r:.4f} (p={p_val:.2e})")
print(f"Mean R = {np.mean(R_p):.4f} ± {np.std(R_p):.4f}")
print(f"R(p) range: [{np.min(R_p):.4f}, {np.max(R_p):.4f}]")
print(f"BK amplitude law: {'NOT CONSISTENT WITH BK-TYPE SCALING' if abs(r) < 0.8 else 'CONSISTENT WITH BK-TYPE SCALING'}")
