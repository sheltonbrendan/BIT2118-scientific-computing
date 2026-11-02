import numpy as np
from scipy.interpolate import interp1d, CubicSpline

hours = np.array([8,9,10,11,12,13,14], float)
# --- Parameter change: reading at 12:00 changed 25.0 -> 27.5 ---
for t12 in (25.0, 27.5):
    T = np.array([18.0,20.0,22.5,24.0,t12,25.5,25.0])
    print(f"T(12:00)={t12}: linear(11:30)={float(interp1d(hours,T)(11.5)):.3f}, cubic(11:30)={float(CubicSpline(hours,T)(11.5)):.3f}")

# --- New case: missing sensor values. True signal: CO2 (ppm) = 420 + 80*sin(pi*(t-6)/12).
#     Sensor drops out; estimate missing hours from remaining readings and compare to truth ---
truth = lambda t: 420 + 80*np.sin(np.pi*(t-6)/12)
t_all = np.arange(6, 19, dtype=float)
missing = np.array([9, 12, 15], float)
t_known = np.array([t for t in t_all if t not in missing])
y_known = truth(t_known)
lin = interp1d(t_known, y_known)(missing)
cub = CubicSpline(t_known, y_known)(missing)
print("Missing hours:", missing.astype(int).tolist())
print("True values :", np.round(truth(missing), 2))
print("Linear      :", np.round(lin, 2), "abs error:", np.round(abs(lin-truth(missing)), 3))
print("Cubic spline:", np.round(cub, 2), "abs error:", np.round(abs(cub-truth(missing)), 3))
