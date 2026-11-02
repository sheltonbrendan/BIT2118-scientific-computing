# Task 15: Numerical Differentiation

Program: [`code/Task_15_numerical_differentiation.py`](../code/Task_15_numerical_differentiation.py) · Output: [`outputs/Task_15_numerical_differentiation_output.txt`](../outputs/Task_15_numerical_differentiation_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** GPS time (0–6 s) and position (m).
- **Operation:** Forward difference at the start, central differences inside, backward difference at the end.

## C. Parameter change
Step size h for f(x)=sin(x) at x=1: central error 9.0e-4 → 9.0e-6 → 9.0e-10 as h goes 0.1 → 0.01 → 1e-4 (∝h²); forward error ∝h (4.3e-2 → 4.2e-5). Below h≈1e-8 round-off dominates and error rises again (1e-12: 1.2e-5 central).

Code: [`code/extensions/Task_15_extension.py`](../code/extensions/Task_15_extension.py) · Output: [`outputs/Task_15_extension_output.txt`](../outputs/Task_15_extension_output.txt)

## D. Meaning of the output
Speed rises from 4.80 to 8.00 m/s: the vehicle is accelerating. Endpoint estimates are one-sided and less accurate. Graph (`outputs/figures/Task_15_numerical_differentiation.png`): a rising line.

## E. Related real-world case
- **Case:** Acceleration of a lift from velocity samples every 0.5 s using `np.gradient`.
- **Assumptions / input data:** Velocity ramps up to 2.0 m/s, holds, then slows.
- **Output:** Peak acceleration +1.15 m/s² at 1.0 s; zero during the 3.0 s cruise; peak deceleration −1.40 m/s² at 5.0 s.
- **Interpretation:** Positive derivative = speeding up, zero = constant speed, negative = braking.
