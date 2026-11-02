import numpy as np
from scipy.optimize import root

# --- Parameter change: circle radius^2 4 -> 9 and a poor initial guess ---
def make(r2):
    return lambda z: [z[0]**2 + z[1]**2 - r2, z[1] - (z[0]**2 - 1)]
for r2 in (4, 9):
    for g in ([1.0, 1.0], [-1.0, 1.0], [0.0, -3.0]):
        s = root(make(r2), g)
        print(f"r^2={r2}, guess={g}: x,y={np.round(s.x,4)}, converged={s.success}")

# --- New case: ellipse x^2/9 + y^2/4 = 1 meets hyperbola xy = 1 (four intersections) ---
eq = lambda z: [z[0]**2/9 + z[1]**2/4 - 1, z[0]*z[1] - 1]
found = set()
for g in ([2,0.5],[0.5,2],[-2,-0.5],[-0.5,-2]):
    s = root(eq, g)
    if s.success:
        found.add(tuple(float(v) for v in np.round(s.x, 4)))
for p in sorted(found): print("Intersection (x,y):", p, "residual:", [round(float(v),4) for v in eq(p)])
# Polynomial roots: cubic x^3 - 6x^2 + 11x - 6 = 0
print("Roots of x^3-6x^2+11x-6:", np.roots([1,-6,11,-6]))
