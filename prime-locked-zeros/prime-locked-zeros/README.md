# Prime-Locked Correlations in High Riemann Zero Blocks

## Overview

This repository contains experimental computations on local correlations of high Riemann zeta zeros.

The main observation is:

> Prime-indexed shifts exhibit statistically significant excess correlation amplitudes.

The effect persists across multiple extremely high zero blocks, including:

- zeros near height ~10^13
- zeros near height ~10^21

---

# Data Source

The zero datasets are from Odlyzko-style zero tables.

Example block:

- zero numbers: 10^21 + 1 through 10^21 + 10^4
- height offset:
  
  144176897509546973000

---

# Core Quantity

For zero spacings:

delta_n = gamma_{n+1} - gamma_n

define the shifted covariance:

C(h) = (1/(N-h)) * sum_{n=1}^{N-h} (delta_n - delta_bar)(delta_{n+h} - delta_bar)

We then define the normalized residual:

A(h) = (C(h) - mu(h)) / sigma(h)

where:
- mu(h) = local background mean
- sigma(h) = local background standard deviation

---

# Main Experimental Observation

For prime shifts p:

A(p) > 0

with strong consistency across tested blocks.

Furthermore:

A(p) ~ C * (log p)^2 / p

shows strong empirical agreement.

---

# High-Height Results

## zeros3 block (~10^12)
- 12/12 tested prime shifts gave positive excess
- r = 0.9992
- p-value = 2.64e-15

## zeros4 block (~10^13)
- 12/12 tested prime shifts gave positive excess
- r = 0.9421
- p-value = 5.0e-6

---

# Interpretation

The phenomenon suggests:

- prime-indexed structure survives deep into the zero statistics
- local zero-spacing correlations are not fully random
- arithmetic information may persist in microscopic correlations

This resembles a weak "prime locking" effect.

---

# Repository Contents

| File | Description |
|---|---|
| analyze.py | Main analysis script |
| zeros4_highT_raw_logp_summary.csv | Summary statistics |
| zeros4_highT_raw_logp_prime_excess_table.csv | Prime excess table |
| zeros4_highT_prime_excess.png | Prime excess plot |
| zeros4_highT_amplitude_scatter.png | Amplitude scaling scatter |

---

# Status

This is currently an experimental numerical observation.

It is NOT a proof of the Riemann Hypothesis.

Further work is needed to determine:

- universality
- robustness
- theoretical derivation
- relation to pair correlation theory
- relation to explicit formula / trace formula frameworks

---

# License

MIT
