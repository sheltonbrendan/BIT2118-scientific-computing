# Task 10: Root Finding: Bisection and Fixed-Point Methods

Program: [`code/Task_10_bisection_fixed_point.py`](../code/Task_10_bisection_fixed_point.py) · Output: [`outputs/Task_10_bisection_fixed_point_output.txt`](../outputs/Task_10_bisection_fixed_point_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** f(T) = T − 25 − 10e^(−T/20); bracket [20, 40]; fixed-point start T = 30; tolerance 1e-10.
- **Operation:** Bisection halves the bracket; fixed-point iterates T = 25 + 10e^(−T/20).

## C. Parameter change
Coefficient 10 → 20: equilibrium moves 27.525 → 29.562 °C (larger heat term, higher balance temperature). Bracket [20,40] → [20,100] → [26,28]: 30 → 32 → 27 iterations (iterations ≈ log₂(width/tol)).

Code: [`code/extensions/Task_10_extension.py`](../code/extensions/Task_10_extension.py) · Output: [`outputs/Task_10_extension_output.txt`](../outputs/Task_10_extension_output.txt)

## D. Meaning of the output
Both methods give 27.525211 °C; fixed-point took 13 iterations. Graph (`outputs/figures/Task_10_bisection_fixed_point.png`): the curve crosses zero at 27.53 °C (dashed line). Fixed-point converges because |g′(T)| ≈ 0.13 < 1.

## E. Related real-world case
- **Case:** Break-even production volume. Cost = 5000 + 12q + 0.02q², revenue = 40q.
- **Assumptions / input data:** Profit(q) = 28q − 0.02q² − 5000; brackets [100,400] and [1000,1400].
- **Output:** Break-even at q = 210.10 and q = 1189.90 units (34 and 35 iterations); matches the exact quadratic roots.
- **Interpretation:** Production is profitable between about 210 and 1190 units; above 1190 the quadratic cost term outgrows revenue.
