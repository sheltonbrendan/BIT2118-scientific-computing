# Task 18: Numerical Solution of ODEs Using SciPy

Program: [`code/Task_18_scipy_ode.py`](../code/Task_18_scipy_ode.py) · Output: [`outputs/Task_18_scipy_ode_output.txt`](../outputs/Task_18_scipy_ode_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Vs=5 V, R=1000 Ω, C=0.001 F, V₀=0, time 0–5 s.
- **Operation:** `solve_ivp` solves dV/dt = (Vs − V)/(RC); compared with exact curve.

## C. Parameter change
R 1000 → 2000 Ω: time constant 1 → 2 s; V(5 s) falls 4.966 → 4.590 V. In both cases V(τ) = 3.161 V (63.2 % of 5 V).

Code: [`code/extensions/Task_18_extension.py`](../code/extensions/Task_18_extension.py) · Output: [`outputs/Task_18_extension_output.txt`](../outputs/Task_18_extension_output.txt)

## D. Meaning of the output
Capacitor reaches 4.9663 V at 5 s; maximum error vs exact 9.3e-10 V. Graph (`outputs/figures/Task_18_scipy_ode.png`): the solver and exact curves overlap; voltage rises quickly then levels at 5 V.

## E. Related real-world case
- **Case:** Car suspension (mass-spring-damper) after a 0.10 m bump.
- **Assumptions / input data:** m=1200 kg, k=60,000 N/m, x(0)=0.10 m; damping c = 1000, 6000, 20000 N·s/m.
- **Output:** c=1000: ζ=0.06, min −0.0831 m, not settled within 4 s. c=6000: ζ=0.35, min −0.0305 m, settles in 1.55 s. c=20000: ζ=1.18, no overshoot, settles in 1.09 s.
- **Interpretation:** Low damping keeps oscillating; moderate damping settles fast with small overshoot; high damping (ζ>1) never overshoots.
