"""Тэгүүдийн power spectrum S(tau) тооцоолох"""
import numpy as np
import matplotlib.pyplot as plt

def load_zeros(filepath, n_max=100000):
    """Odlyzko zeros2 файлыг унших"""
    zeros = np.loadtxt(filepath)[:n_max]
    return zeros

def power_spectrum(tau, gamma):
    """S(tau) = |Σ e^{i τ γ_n}|² / N"""
    N = len(gamma)
    Z = np.sum(np.exp(1j * tau * gamma))
    return np.abs(Z)**2 / N

# Үндсэн тооцоолол
gamma = load_zeros('data/zeros2', n_max=100000)
primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37])
tau_p = np.log(primes) / (2*np.pi)

S_obs = np.array([power_spectrum(t, gamma) for t in tau_p])

# Хадгалах
np.savetxt('results/tables/power_spectrum_peaks.csv', 
           np.column_stack([primes, tau_p, S_obs]),
           header='p,tau,S_obs', delimiter=',')

# График зурах
tau_all = np.linspace(0, 0.8, 1000)
S_all = np.array([power_spectrum(t, gamma) for t in tau_all])

plt.figure(figsize=(12,5))
plt.plot(tau_all, S_all, 'b-', linewidth=1, alpha=0.7)
plt.scatter(tau_p, S_obs, c='red', s=80, zorder=5, label='Prime positions')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$S(\tau)$')
plt.title(f'Power Spectrum of Riemann Zeros (N={len(gamma)})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('results/figures/power_spectrum_full.png', dpi=150)
plt.show()
