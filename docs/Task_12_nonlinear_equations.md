# Task 12: Polynomial and Nonlinear Equation Solving

Program: [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py) · Output: [`outputs/Task_12_nonlinear_equations_output.txt`](../outputs/Task_12_nonlinear_equations_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Circle x²+y²=4 and parabola y=x²−1; initial guesses (1,1) and (−1,1).
- **Operation:** `scipy.optimize.root` finds (x,y) making both residuals zero.

## C. Parameter change
Radius² 4 → 9: intersections move to (±1.8364, 2.3723). A poor guess (0,−3) fails (`converged=False`) because no real intersection exists in the lower region (it would need x² < 0).

Code: [`code/extensions/Task_12_extension.py`](../code/extensions/Task_12_extension.py) · Output: [`outputs/Task_12_extension_output.txt`](../outputs/Task_12_extension_output.txt)

## D. Meaning of the output
Two intersections (±1.5175, 1.3028); residuals ~1e-13 and `Converged: True` confirm both lie on both curves. The starting guess selects which root is found.

## E. Related real-world case
- **Case:** Ellipse x²/9 + y²/4 = 1 meeting hyperbola xy = 1; also cubic x³−6x²+11x−6.
- **Assumptions / input data:** Four starting guesses, one per quadrant; `np.roots` for the cubic.
- **Output:** Four intersections: ±(0.5073, 1.9712) and ±(2.9568, 0.3382); cubic roots 1, 2, 3.
- **Interpretation:** Nonlinear systems may have several solutions; different guesses find different ones.
