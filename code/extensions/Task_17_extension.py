import numpy as np

# --- Parameter change: step size and cooling constant (cooling of 90 C object, ambient 25 C) ---
def euler_cool(k, h, T0=90.0, Ta=25.0, end=30.0):
    n = int(round(end/h)); T = T0
    for _ in range(n): T += h*(-k*(T-Ta))
    return T
for k in (0.12, 0.30):
    ex = 25 + 65*np.exp(-k*30)
    for h in (5.0, 1.0, 0.1):
        T = euler_cool(k, h)
        print(f"k={k}, h={h}: Euler={T:.4f} C, exact={ex:.4f} C, error={abs(T-ex):.2e}")
print("k=0.5, h=5 (h*k=2.5 > 2):", round(euler_cool(0.5, 5.0), 2), "C -> unstable oscillation")

# --- New case: SIR epidemic, N=10,000, beta=0.30/day, gamma=0.10/day, I0=10, Euler h=0.5 day ---
N, beta, gamma, h, days = 10_000, 0.30, 0.10, 0.5, 160
S, I, R = N-10.0, 10.0, 0.0
peak_I, peak_t = I, 0.0
for i in range(int(days/h)):
    dS = -beta*S*I/N; dI = beta*S*I/N - gamma*I; dR = gamma*I
    S, I, R = S+h*dS, I+h*dI, R+h*dR
    if I > peak_I: peak_I, peak_t = I, (i+1)*h
print(f"R0 = {beta/gamma:.1f}")
print(f"Peak infected: {peak_I:.0f} people on day {peak_t:.1f}")
print(f"Final recovered after {days} days: {R:.0f} ({R/N:.1%} of population)")
