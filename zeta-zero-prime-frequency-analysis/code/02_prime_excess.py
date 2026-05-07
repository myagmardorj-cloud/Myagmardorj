"""Prime excess ΔK(p) тооцоолох"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def load_zeros(filepath, n_max=100000):
    return np.loadtxt(filepath)[:n_max]

def power_spectrum(tau, gamma):
    N = len(gamma)
    Z = np.sum(np.exp(1j * tau * gamma))
    return np.abs(Z)**2 / N

def baseline_smooth(tau, gamma, delta=0.05):
    """Local GUE baseline тооцоолох (null hypothesis)"""
    # Энгийн хувилбар: 1 (normalized)
    # Бодит тооцоололд ойролцоох цэгүүдийн дундаж
    return 1.0

# Өгөгдөл
gamma = load_zeros('data/zeros2', 100000)
primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37])
tau_p = np.log(primes) / (2*np.pi)

S_obs = np.array([power_spectrum(t, gamma) for t in tau_p])
S_base = np.array([baseline_smooth(t, gamma) for t in tau_p])
DeltaK = S_obs - S_base

# Статистик
corr, p_val = pearsonr(tau_p, DeltaK)

print("=== PRIME EXCESS RESULTS ===")
print(f"Mean ΔK = {np.mean(DeltaK):.4f}")
print(f"Correlation τ vs ΔK = {corr:.4f} (p={p_val:.2e})")
print(f"All ΔK > 0: {np.all(DeltaK > 0)}")

# Хүснэгт
table = np.column_stack([primes, tau_p, S_obs, S_base, DeltaK])
np.savetxt('results/tables/local_amplitude_table.csv', table,
           header='p,tau,S_obs,S_base,DeltaK', delimiter=',', fmt='%.6f')

# График
plt.figure(figsize=(10,6))
plt.bar(range(len(primes)), DeltaK, tick_label=primes)
plt.xlabel('Prime p')
plt.ylabel(r'$\Delta K(p)$')
plt.title('Prime-Location Excess Signal')
plt.axhline(y=0, color='r', linestyle='--')
plt.savefig('results/figures/prime_windows_plot.png', dpi=150)
plt.show()
