# Task 08: Iterative Methods for Linear Systems

Program: [`code/Task_08_iterative_linear.py`](../code/Task_08_iterative_linear.py) · Output: [`outputs/Task_08_iterative_linear_output.txt`](../outputs/Task_08_iterative_linear_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 5×5 tridiagonal A, b = [100,0,0,0,20] (boundary temperatures 100 °C and 20 °C), tolerance 1e-8.
- **Operation:** Jacobi and Gauss-Seidel iterations from x = 0, stopping when the maximum change < tolerance.

## C. Parameter change
Right boundary 20 → 60 °C: iteration counts barely change (150/75 → 152/77); the boundary value changes the answer, not the speed. Tolerance 1e-8 → 1e-4: 86 (Jacobi) and 43 (GS) iterations, GS error rises to 2.9e-4.

Code: [`code/extensions/Task_08_extension.py`](../code/extensions/Task_08_extension.py) · Output: [`outputs/Task_08_extension_output.txt`](../outputs/Task_08_extension_output.txt)

## D. Meaning of the output
Temperatures 86.67, 73.33, 60.00, 46.67, 33.33 °C: a straight-line drop from 100 to 20, as expected for steady heat conduction. Graph (`outputs/figures/Task_08_iterative_linear.png`): both error curves are straight lines on the log scale (steady geometric convergence); Gauss-Seidel is steeper, needing about half the iterations.

## E. Related real-world case
- **Case:** Steady-state temperature of a 1-D metal rod with 30 interior nodes, ends at 100 °C and 0 °C.
- **Assumptions / input data:** Tolerance 1e-6, same iterative methods.
- **Output:** Jacobi 2604 iterations, Gauss-Seidel 1296; node temperatures match the direct solution (96.774, 51.613, 3.226 °C at nodes 1, 15, 30).
- **Interpretation:** More nodes make convergence much slower, and Gauss-Seidel stays ≈2× faster than Jacobi. Iterative methods pay off for large sparse systems where direct factorization is expensive.
