"""Null hypothesis тестүүд"""
import numpy as np

def load_zeros(filepath, n_max=100000):
    return np.loadtxt(filepath)[:n_max]

def power_spectrum(tau, gamma):
    N = len(gamma)
    Z = np.sum(np.exp(1j * tau * gamma))
    return np.abs(Z)**2 / N

gamma = load_zeros('data/zeros_ht', 100000)
primes = np.array([2,3,5,7,11,13,17,19,23,29,31,37])
tau_p = np.log(primes) / (2*np.pi)
B_p = (np.log(primes))**2 / primes

def test_shuffled_zeros(gamma, primes, tau_p, B_p, n_shuffle=100):
    """Zeros-ийг permutation хийх"""
    results = []
    for _ in range(n_shuffle):
        gamma_shuffled = np.random.permutation(gamma)
        S_shuffled = np.array([power_spectrum(t, gamma_shuffled) for t in tau_p])
        DeltaK_shuffled = S_shuffled - 1.0
        R_shuffled = DeltaK_shuffled / B_p
        results.append(np.mean(R_shuffled))
    return np.mean(results), np.std(results)

def test_random_positions(gamma, n_random=1000):
    """Санамсаргүй τ позиц дээр тест хийх"""
    tau_random = np.random.uniform(0, 0.6, n_random)
    S_rand = np.array([power_spectrum(t, gamma) for t in tau_random])
    return np.mean(S_rand), np.std(S_rand)

def test_zero_blocks(gamma, primes, tau_p):
    """Өөр block of zeros дээр тест хийх"""
    block_size = len(gamma) // 2
    gamma_1 = gamma[:block_size]
    gamma_2 = gamma[block_size:2*block_size]
    
    S_1 = np.array([power_spectrum(t, gamma_1) for t in tau_p])
    S_2 = np.array([power_spectrum(t, gamma_2) for t in tau_p])
    
    return np.mean(S_1), np.mean(S_2), np.std(S_1 - S_2)

print("\n=== NULL TESTS ===")

mean_R, std_R = test_shuffled_zeros(gamma, primes, tau_p, B_p, n_shuffle=50)
print(f"Shuffled zeros: mean R = {mean_R:.4f} ± {std_R:.4f}")

mean_S, std_S = test_random_positions(gamma, n_random=500)
S_obs = np.array([power_spectrum(t, gamma) for t in tau_p])
print(f"Random τ: mean S = {mean_S:.4f} ± {std_S:.4f}")
print(f"Prime positions mean S = {np.mean(S_obs):.4f}")
print(f"Signal-to-noise ratio = {(np.mean(S_obs) - mean_S) / std_S:.2f}σ")

mean_1, mean_2, std_diff = test_zero_blocks(gamma, primes, tau_p)
print(f"Block 1 mean S = {mean_1:.4f}")
print(f"Block 2 mean S = {mean_2:.4f}")
print(f"Difference = {mean_1 - mean_2:.4f} ± {std_diff:.4f}")
