# Task 16: Numerical Integration

Program: [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py) · Output: [`outputs/Task_16_numerical_integration_output.txt`](../outputs/Task_16_numerical_integration_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Power (kW) at 2-hour intervals over 12 h.
- **Operation:** Trapezoidal rule and Simpson's rule approximate ∫P dt.

## C. Parameter change
Peak 1.8 → 3.0 kW: energy 15.70/15.80 → 18.10/19.00 kWh. A sharper peak increases the gap between the two rules (0.10 → 0.90 kWh).

Code: [`code/extensions/Task_16_extension.py`](../code/extensions/Task_16_extension.py) · Output: [`outputs/Task_16_extension_output.txt`](../outputs/Task_16_extension_output.txt)

## D. Meaning of the output
Energy used ≈ 15.7–15.8 kWh over the period (kW × h = kWh); the 0.1 kWh difference measures sensitivity to the method.

## E. Related real-world case
- **Case:** Total water volume of a river over 12 h from flow Q(t) = 50 + 30 sin(πt/12) m³/s.
- **Assumptions / input data:** 4, 7, 13, 25 samples; exact volume 2,985,059 m³.
- **Output:** Simpson error: 16,717 → 356 → 22 → 1 m³. Trapezoid error: 76,813 → 18,936 → 4,718 → 1,178 m³.
- **Interpretation:** More samples reduce error; Simpson converges much faster on smooth data (error ∝h⁴ vs h²).
