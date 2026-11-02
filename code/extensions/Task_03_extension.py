import numpy as np, timeit
rng = np.random.default_rng(42)

def compare(n):
    x = rng.uniform(5, 250, n)
    def loop():
        out = []
        for v in x:
            out.append((v/1000.0)**2)
        return out
    def vec():
        return (x/1000.0)**2
    lt = timeit.timeit(loop, number=1)
    vt = timeit.timeit(vec, number=3)/3
    return lt, vt

# --- Parameter change: array size 1,000,000 -> 10,000 ---
for n in (1_000_000, 10_000):
    lt, vt = compare(n)
    print(f"N={n:>9,}: loop={lt:.4f}s vectorized={vt:.6f}s speed-up={lt/vt:.1f}x")

# --- New case: ADC counts (12-bit, 3.3 V ref) -> volts -> RMS voltage ---
adc = rng.integers(0, 4096, 1_000_000)
volts = adc * 3.3 / 4095
rms = np.sqrt(np.mean(volts**2))
print(f"ADC mean voltage: {volts.mean():.4f} V, RMS: {rms:.4f} V, max: {volts.max():.4f} V")
