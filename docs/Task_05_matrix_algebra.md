# Task 05: Matrix Algebra and Matrix Operations

Program: [`code/Task_05_matrix_algebra.py`](../code/Task_05_matrix_algebra.py) · Output: [`outputs/Task_05_matrix_algebra_output.txt`](../outputs/Task_05_matrix_algebra_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Unit-square corner points; rotation 45°; scale (2, 1.5).
- **Operation:** T = R·S (scale first, then rotate); points transformed by `points @ T.T`; determinant.

## C. Parameter change
Rotation 90°, scale (3, 1): square becomes a 3-tall by 1-wide rectangle (points (0,3), (−1,3), (−1,0)). Determinant stays 3 because rotation preserves area and scale factors multiply (3×1).

Code: [`code/extensions/Task_05_extension.py`](../code/extensions/Task_05_extension.py) · Output: [`outputs/Task_05_extension_output.txt`](../outputs/Task_05_extension_output.txt)

## D. Meaning of the output
Point (1,0) → (1.414, 1.414). Determinant 3 means areas are multiplied by 3 (2×1.5); positive sign means orientation is preserved.

## E. Related real-world case
- **Case:** Drone waypoints: rotate by 30° heading and translate by (10, 5) m using a 3×3 homogeneous matrix.
- **Assumptions / input data:** Square flight path with 10 m sides in the drone frame.
- **Output:** World-frame waypoints: (10,5), (18.66,10), (13.66,18.66), (5,13.66); side length 10.0 m.
- **Interpretation:** A rigid transform keeps distances unchanged (side still 10 m) while changing position and orientation. Homogeneous coordinates let translation be done by matrix multiplication.
