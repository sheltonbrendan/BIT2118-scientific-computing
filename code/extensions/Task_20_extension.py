import numpy as np
from math import erf, sqrt

# --- Parameter change: number of simulations N and capacity ---
for cap in (1000.0, 1100.0):
    exact = 0.5*(1 - erf((cap-850)/(120*sqrt(2))))
    for N in (1_000, 100_000, 1_000_000):
        d = np.random.default_rng(42).normal(850, 120, N)
        print(f"capacity={cap:.0f}, N={N:>9,}: estimate={np.mean(d>cap):.4%} | exact={exact:.4%}")

# --- New case 1: estimate pi (quarter-circle method) ---
rng = np.random.default_rng(7)
for N in (1_000, 100_000, 5_000_000):
    p = rng.random((N, 2)); inside = np.sum(p[:,0]**2 + p[:,1]**2 <= 1)
    print(f"pi estimate N={N:>9,}: {4*inside/N:.5f}  (error {abs(4*inside/N-np.pi):.5f})")

# --- New case 2: project delay risk. Three sequential tasks, triangular durations (min, mode, max) days.
#     Deadline 30 days. P(overrun)? ---
rng = np.random.default_rng(11); N = 200_000
total = (rng.triangular(5, 8, 15, N) + rng.triangular(7, 10, 20, N) + rng.triangular(4, 6, 12, N))
print(f"Project duration: mean={total.mean():.2f} d, 5th-95th percentile=({np.percentile(total,5):.1f}, {np.percentile(total,95):.1f}) d")
print(f"P(duration > 30 days) = {np.mean(total>30):.2%}")
