"""Туслах функцууд"""
import numpy as np

def load_odlyzko_zeros(filepath, n_max=None, skip=0):
    """Odlyzko zeros_ht файлыг унших
    Формат: γ_n (imaginary parts) утгууд, нэг баганад
    """
    zeros = np.loadtxt(filepath)
    if skip > 0:
        zeros = zeros[skip:]
    if n_max is not None:
        zeros = zeros[:n_max]
    return zeros

def prime_frequencies(primes):
    """τ = log(p) / 2π тооцоолох"""
    return np.log(primes) / (2 * np.pi)

def power_spectrum_fast(tau, gamma):
    """Багцалсан tau-д power spectrum тооцоолох"""
    N = len(gamma)
    tau = np.asarray(tau)
    Z = np.sum(np.exp(1j * np.outer(tau, gamma)), axis=1)
    return np.abs(Z)**2 / N
