import numpy as np

# --- Parameter change: step size h for f(x)=sin(x) at x=1 (exact derivative cos(1)) ---
exact = np.cos(1.0)
print(f"{'h':>8} {'forward err':>13} {'central err':>13}")
for h in (1e-1, 1e-2, 1e-4, 1e-8, 1e-12):
    fwd = (np.sin(1+h) - np.sin(1))/h
    cen = (np.sin(1+h) - np.sin(1-h))/(2*h)
    print(f"{h:8.0e} {abs(fwd-exact):13.3e} {abs(cen-exact):13.3e}")

# --- New case: acceleration of a lift from velocity samples (every 0.5 s) ---
t = np.arange(0, 5.5, 0.5)
v = np.array([0.0,0.35,0.9,1.5,1.9,2.0,2.0,2.0,1.85,1.3,0.6])    # m/s
a = np.gradient(v, t)                    # 2nd-order central differences inside
for ti, vi, ai in zip(t, v, a):
    print(f"t={ti:.1f}s v={vi:.2f} m/s a={ai:+.2f} m/s^2")
print(f"Peak acceleration: {a.max():.2f} m/s^2 at t={t[a.argmax()]:.1f}s ; peak deceleration: {a.min():.2f} m/s^2 at t={t[a.argmin()]:.1f}s")
