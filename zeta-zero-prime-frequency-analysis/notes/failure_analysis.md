# Failure Analysis — Why Initial BK Test Failed

## Initial results (zeros2, low-T normalization)

- Pearson r ≈ 0.4–0.6
- BK law appeared NOT confirmed

## Root cause: Wrong normalization

### ❌ Wrong (low-T formula)
```
τ_p = log(p) / (2π)
```
This is the formula for zeros near T ≈ 0.
Result: r ≈ 0.4–0.6 → no signal.

### ✅ Correct (high-T unfolded)
```
τ_p = log(p) / log(T / 2π)
```
At height T, zeros have mean spacing ~2π/log(T/2π).
The unfolded coordinate accounts for this.
Result: r = 0.9992 on zeros3 block → strong signal.

## Why this matters

Montgomery's pair correlation uses exactly this
unfolded normalization. Without it, the BK-type
prime-lock effect is masked by the scaling mismatch.

## Lesson

Normalization is not a minor detail — it is the
critical ingredient. This failure led directly to
the key insight that produced r = 0.9992.

## Current status

| Normalization | Dataset | r | Signal |
|---------------|---------|---|--------|
| log(p)/2π (wrong) | zeros2 | ~0.5 | ❌ |
| log(p)/log(T/2π) | zeros2 | 0.9783 | ✅ |
| log(p)/log(T/2π) | zeros3 | 0.9992 | ✅ |
| log(p)/log(T/2π) | zeros4 | 0.9421 | ✅ |

## Important caveat

These results are numerical observations only.
Not a confirmed theorem. Independent replication needed.
