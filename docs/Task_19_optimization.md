# Task 19: Numerical Optimization

Program: [`code/Task_19_optimization.py`](../code/Task_19_optimization.py) · Output: [`outputs/Task_19_optimization_output.txt`](../outputs/Task_19_optimization_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Cost 12/unit (A), 18/unit (B); capacity 100 (A), 170 (B); need ≥ 1000.
- **Operation:** `minimize` (SLSQP) with an inequality constraint and non-negative bounds; integer check by enumeration.

## C. Parameter change
Need 1000 → 2000: cost 105.88 → 211.76 (scales with need). Cost of B 18 → 15: cost 105.88 → 88.24. Whole-server plans: 6 B (108), 12 B (216), 6 B (90).

Code: [`code/extensions/Task_19_extension.py`](../code/extensions/Task_19_extension.py) · Output: [`outputs/Task_19_extension_output.txt`](../outputs/Task_19_extension_output.txt)

## D. Meaning of the output
Use 5.882 units of Type B only (cost 105.88). Type B costs 0.106 per capacity unit vs 0.12 for A. Rounded to whole servers: 6 B, capacity 1020, cost 108.

## E. Related real-world case
- **Case:** Factory production mix: chairs (profit 45; 3 h carpentry, 1 h finishing) and tables (profit 80; 4 h, 3 h); 240 h carpentry, 120 h finishing available.
- **Assumptions / input data:** Maximise profit with `linprog`.
- **Output:** 48 chairs and 24 tables, profit 4,080; both resources fully used; whole-number search gives the same plan.
- **Interpretation:** The optimum is at a corner where both constraints bind, so neither resource is left idle.
