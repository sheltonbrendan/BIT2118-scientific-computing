import numpy as np
from scipy.optimize import root_scalar

def bisect(f, a, b, tol=1e-8):
    n = 0
    while (b-a)/2 > tol:
        m = (a+b)/2; n += 1
        if f(a)*f(m) <= 0: b = m
        else: a = m
    return (a+b)/2, n

# --- Parameter change: heat-loss coefficient 10 -> 20, wider bracket ---
for c in (10, 20):
    f = lambda T, c=c: T - 25 - c*np.exp(-T/20)
    r = root_scalar(f, bracket=[20, 60], method="bisect", xtol=1e-10)
    print(f"coefficient={c}: equilibrium T = {r.root:.6f} C")
# Effect of bracket width on bisection iterations (own implementation)
f = lambda T: T - 25 - 10*np.exp(-T/20)
for a, b in ((20, 40), (20, 100), (26, 28)):
    r, n = bisect(f, a, b)
    print(f"bracket [{a},{b}]: root={r:.6f}, iterations={n}")

# --- New case: break-even volume. Cost = 5000 + 12q + 0.02q^2 ; Revenue = 40q ---
profit = lambda q: 40*q - (5000 + 12*q + 0.02*q**2)
for a, b in ((100, 400), (1000, 1400)):
    r, n = bisect(profit, a, b)
    print(f"Break-even in [{a},{b}]: q={r:.4f} units ({n} iterations), profit there={profit(r):.6f}")
print("Exact (quadratic formula):", np.round(np.roots([-0.02, 28, -5000]), 4))
