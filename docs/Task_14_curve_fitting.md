# Task 14: Curve Fitting and Approximation

Program: [`code/Task_14_curve_fitting.py`](../code/Task_14_curve_fitting.py) · Output: [`outputs/Task_14_curve_fitting_output.txt`](../outputs/Task_14_curve_fitting_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 7 measurements of users vs response time (ms); quadratic model.
- **Operation:** `curve_fit` minimises the sum of squared residuals.

## C. Parameter change
Model degree 1 → 2 → 3: RMSE 18.83 → 1.55 → 0.14 ms; prediction at 400 users 312.9 → 377.9 → 387.9 ms. Linear underfits; cubic fits 7 points almost exactly and risks overfitting.

Code: [`code/extensions/Task_14_extension.py`](../code/extensions/Task_14_extension.py) · Output: [`outputs/Task_14_extension_output.txt`](../outputs/Task_14_extension_output.txt)

## D. Meaning of the output
y = 0.002167x² − 0.1345x + 85.00, RMSE 1.55 ms, 377.9 ms predicted at 400 users. Graph (`outputs/figures/Task_14_curve_fitting.png`): the curve passes close to all points and bends upward, so delay grows faster with load. The 400-user value is an extrapolation.

## E. Related real-world case
- **Case:** Growth of mobile-payment transactions (millions/month), exponential model y = a·e^(rt).
- **Assumptions / input data:** Illustrative synthetic data, 12 months.
- **Output:** y = 10.016·e^(0.0975t); growth 10.24 %/month; doubling time 7.11 months; R² 0.9992; month-15 forecast 43.25 M.
- **Interpretation:** Near-perfect R² supports exponential growth over this window; the forecast assumes the trend continues.
