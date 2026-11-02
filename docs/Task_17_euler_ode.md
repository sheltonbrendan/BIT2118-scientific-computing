# Task 17: Ordinary Differential Equations – Euler Method

Program: [`code/Task_17_euler_ode.py`](../code/Task_17_euler_ode.py) · Output: [`outputs/Task_17_euler_ode_output.txt`](../outputs/Task_17_euler_ode_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** T₀=90 °C, T_ambient=25 °C, k=0.12 /min, h=1 min, 30 min.
- **Operation:** Euler update T_{n+1} = T_n + h·(−k(T_n − T_amb)); compared with exact solution.

## C. Parameter change
Step h = 5 / 1 / 0.1: error 1.51 / 0.372 / 0.038 °C (error ∝ h). k=0.3, h=5 oscillates around the answer (error 1.01); k=0.5, h=5 is unstable (h·k > 2) and blows up.

Code: [`code/extensions/Task_17_extension.py`](../code/extensions/Task_17_extension.py) · Output: [`outputs/Task_17_extension_output.txt`](../outputs/Task_17_extension_output.txt)

## D. Meaning of the output
After 30 min: Euler 26.40 °C vs exact 26.78 °C, error 0.372 °C. Graph (`outputs/figures/Task_17_euler_ode.png`): both curves decay exponentially towards 25 °C; Euler sits slightly below the exact curve.

## E. Related real-world case
- **Case:** SIR epidemic: S, I, R compartments, N = 10,000.
- **Assumptions / input data:** β=0.30/day, γ=0.10/day (R₀=3), I₀=10, h=0.5 day, 160 days.
- **Output:** Peak 3,067 infected on day 39.5; 9,436 recovered (94.4 %) by day 160.
- **Interpretation:** With R₀=3 the epidemic peaks about day 40 and infects almost everyone; reducing β (distancing) would lower and delay the peak.
