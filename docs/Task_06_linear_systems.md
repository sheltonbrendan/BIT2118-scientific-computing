# Task 06: Solution of Systems of Linear Equations

Program: [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py) · Output: [`outputs/Task_06_linear_systems_output.txt`](../outputs/Task_06_linear_systems_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** A = [[4,2],[8,12]], b = [20,72] (CPU and memory totals).
- **Operation:** `np.linalg.solve(A,b)`, then verification via residual b − A·x.

## C. Parameter change
Totals 20 CPU/72 GB → 26 CPU/76 GB: solution changes from (3, 4) to (5, 3) servers. More CPU with little memory increase shifts the mix toward Type A (CPU-heavier).

Code: [`code/extensions/Task_06_extension.py`](../code/extensions/Task_06_extension.py) · Output: [`outputs/Task_06_extension_output.txt`](../outputs/Task_06_extension_output.txt)

## D. Meaning of the output
3 Type A and 4 Type B servers; residual 0 confirms both resource totals are reproduced.

## E. Related real-world case
- **Case:** Three-loop mesh circuit: 10I₁−4I₂=12, −4I₁+12I₂−3I₃=0, −3I₂+8I₃=−6.
- **Assumptions / input data:** Resistances in ohms, voltages in volts; unknowns are mesh currents.
- **Output:** I₁ = 1.3100 A, I₂ = 0.2749 A, I₃ = −0.6469 A; residual 6.7e-16; condition number 3.0.
- **Interpretation:** Negative I₃ means the current flows opposite to the assumed direction. Condition number 3 means the system is well conditioned (stable solution).
