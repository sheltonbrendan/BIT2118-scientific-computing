import numpy as np
from scipy.integrate import simpson

t = np.array([0,2,4,6,8,10,12], float)
# --- Parameter change: peak reading 1.8 -> 3.0 kW ---
for p in (np.array([0.8,1.0,1.4,1.8,1.6,1.2,0.9]), np.array([0.8,1.0,1.4,3.0,1.6,1.2,0.9])):
    print(f"peak={p.max()} kW: trapezoid={np.trapezoid(p,t):.3f}, Simpson={simpson(p,x=t):.3f} kWh")

# --- New case: river-flow volume. Flow Q(t) = 50 + 30 sin(pi t/12) m^3/s, t in hours, 0..12 h.
#     Exact volume = int Q dt * 3600 ---
Q = lambda h: 50 + 30*np.sin(np.pi*h/12)
exact = (50*12 + 30*24/np.pi) * 3600       # m^3
for n in (4, 7, 13, 25):
    h = np.linspace(0, 12, n)
    tr = np.trapezoid(Q(h), h)*3600; sp = simpson(Q(h), x=h)*3600
    print(f"{n:>2} samples: trapezoid={tr:,.0f} (err {abs(tr-exact):,.0f}) | Simpson={sp:,.0f} (err {abs(sp-exact):,.0f}) m^3")
print(f"Exact volume: {exact:,.0f} m^3")
