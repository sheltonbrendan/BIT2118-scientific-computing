# Task 07: Gaussian Elimination and LU Decomposition

Program: [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py) · Output: [`outputs/Task_07_gaussian_lu_output.txt`](../outputs/Task_07_gaussian_lu_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 3×3 matrix A and three measurement vectors b.
- **Operation:** `lu_factor` once, then `lu_solve` for each b; compared with `np.linalg.solve`.

## C. Parameter change
Diagonal 4 → 6 (stronger diagonal): solution for b=[15,10,10] changes from [5,5,5] to [2.929, 2.574, 2.515]. Larger coefficients mean the same measurements imply smaller unknowns.

Code: [`code/extensions/Task_07_extension.py`](../code/extensions/Task_07_extension.py) · Output: [`outputs/Task_07_extension_output.txt`](../outputs/Task_07_extension_output.txt)

## D. Meaning of the output
Each row gives the unknowns for one measurement set; residual norms ~1e-15 show accurate solutions; LU result equals the direct solution.

## E. Related real-world case
- **Case:** Structural/spring model with 400 unknowns and 300 load cases.
- **Assumptions / input data:** Tridiagonal stiffness matrix (4 on diagonal, −1 off-diagonal); random loads 0–10.
- **Output:** Repeated `solve`: 0.6298 s; LU reused: 0.0183 s (34.3× faster); results identical (max difference 0.0).
- **Interpretation:** Factoring once and reusing the factors avoids repeating the expensive elimination for every load case.
