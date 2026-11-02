# Task 04: Floating-Point Arithmetic and Numerical Errors

Program: [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py) · Output: [`outputs/Task_04_numerical_errors_output.txt`](../outputs/Task_04_numerical_errors_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 0.1 + 0.2 vs 0.3; √2 vs 1.414; x = 1e-4, 1e-8, 1e-12.
- **Operation:** Equality test, `np.isclose`, absolute/relative error, and (√(1+x)−1)/x vs its algebraically equivalent stable form 1/(√(1+x)+1).

## C. Parameter change
Approximation 1.414 → 1.4142 → 1.41421356: relative error 0.0151 % → 0.0010 % → ~1.7e-7 %. More digits, proportionally smaller error.

Code: [`code/extensions/Task_04_extension.py`](../code/extensions/Task_04_extension.py) · Output: [`outputs/Task_04_extension_output.txt`](../outputs/Task_04_extension_output.txt)

## D. Meaning of the output
`0.1+0.2 == 0.3` is False (0.30000000000000004) but `isclose` is True. The direct formula degrades as x shrinks (x=1e-12 gives 0.500044 instead of 0.5) from cancellation in √(1+x)−1; the stable form stays exact.

## E. Related real-world case
- **Case:** Banking: summing 1000 transactions of 0.10, which should total 100.00.
- **Assumptions / input data:** Float, `Decimal` and integer-cents arithmetic compared.
- **Output:** Float sum = 99.9999999999986 (error 1.4e-12, `== 100.0` False); Decimal and integer cents give exactly 100.00.
- **Interpretation:** Tiny errors accumulate over many operations. Use tolerances for comparisons and Decimal/integer cents for money.
