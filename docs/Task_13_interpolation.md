# Task 13: Interpolation

Program: [`code/Task_13_interpolation.py`](../code/Task_13_interpolation.py) · Output: [`outputs/Task_13_interpolation_output.txt`](../outputs/Task_13_interpolation_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Hourly temperatures 08:00–14:00.
- **Operation:** Linear interpolation (`interp1d`) and cubic spline (`CubicSpline`) evaluated every 10 minutes.

## C. Parameter change
Reading at 12:00 changed 25.0 → 27.5 °C: the 11:30 estimate rises 24.50 → 25.75 (linear) and 24.54 → 25.99 (cubic). The spline reacts more because it uses neighbouring points globally.

Code: [`code/extensions/Task_13_extension.py`](../code/extensions/Task_13_extension.py) · Output: [`outputs/Task_13_extension_output.txt`](../outputs/Task_13_extension_output.txt)

## D. Meaning of the output
10:30 estimate: 23.25 °C (linear) vs 23.36 °C (cubic). Graph (`outputs/figures/Task_13_interpolation.png`): the linear curve is piecewise straight with corners at measurements; the spline is smooth and bulges slightly above the line where the data are concave.

## E. Related real-world case
- **Case:** Estimating missing CO₂ sensor readings at hours 9, 12, 15 from the remaining data.
- **Assumptions / input data:** True signal 420 + 80·sin(π(t−6)/12) ppm, used only to measure error.
- **Output:** Absolute errors: linear 1.9–2.7 ppm; cubic spline 0.02–0.03 ppm.
- **Interpretation:** For smooth signals a cubic spline recovers missing values far more accurately than linear. For noisy or abrupt data it can overshoot.
