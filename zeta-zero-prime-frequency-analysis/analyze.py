import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# load zero heights
x = np.loadtxt("zeros4.txt")

# spacings
d = np.diff(x)

# centered spacings
d = d - d.mean()

primes = [2,3,5,7,11,13,17,19,23,29,31,37]

vals = []

for p in primes:
    a = d[:-p]
    b = d[p:]
    c = np.mean(a*b)
    vals.append(c)

vals = np.array(vals)

target = (np.log(primes)**2)/np.array(primes)

r, pv = pearsonr(vals, target)

print("correlation =", r)
print("p-value =", pv)

plt.scatter(target, vals)
plt.xlabel(r'$(\log p)^2/p$')
plt.ylabel('Amplitude')
plt.title('Prime-Locked Excess')
plt.savefig("scatter.png", dpi=200)

print("done")
