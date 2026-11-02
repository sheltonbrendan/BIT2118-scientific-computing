import numpy as np
from scipy.integrate import solve_ivp

# --- Parameter change: RC charging, R 1000 -> 2000 ohm (time constant doubles) ---
for R in (1000.0, 2000.0):
    C = 0.001; tau = R*C
    s = solve_ivp(lambda t, V: [(5-V[0])/(R*C)], (0, 10), [0.0], dense_output=True, rtol=1e-9, atol=1e-11)
    print(f"R={R:.0f}: tau={tau:.1f} s | V(tau)={s.sol(tau)[0]:.3f} V (63.2% of 5 V) | V(3 tau)={s.sol(3*tau)[0]:.3f} V | V(5 s)={s.sol(5)[0]:.3f} V")

# --- New case: car suspension, mass-spring-damper  m x'' + c x' + k x = 0
#     m=1200 kg, k=60000 N/m, x(0)=0.10 m bump, v(0)=0 ---
m, k = 1200.0, 60000.0
def run(c):
    f = lambda t, y: [y[1], -(c*y[1] + k*y[0])/m]
    s = solve_ivp(f, (0, 4), [0.10, 0.0], t_eval=np.linspace(0, 4, 2000), rtol=1e-8, atol=1e-10)
    return s
zeta = lambda c: c/(2*np.sqrt(k*m))
for c in (1000.0, 6000.0, 20000.0):
    s = run(c); x = s.y[0]
    settle = s.t[np.where(np.abs(x) > 0.02*0.10)[0][-1]] if np.any(np.abs(x) > 0.002) else 0
    print(f"c={c:>7.0f} N s/m: damping ratio={zeta(c):.2f}, min displacement={x.min():+.4f} m, 2% settling time={settle:.2f} s")
