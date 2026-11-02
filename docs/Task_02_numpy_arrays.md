# Task 02: NumPy Arrays and Numerical Computation

Program: [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py) · Output: [`outputs/Task_02_numpy_arrays_output.txt`](../outputs/Task_02_numpy_arrays_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 24 hourly temperatures (°C) stored in one `np.array`.
- **Operation:** `mean`, `min`, `max` (reductions) and vectorized conversion F = 1.8C + 32.

## C. Parameter change
Every reading +5 °C (heatwave): mean 23.12 → 28.12, min 17.50 → 22.50, max 29.40 → 34.40. Location statistics shift by exactly the added offset; every °F value shifts by 9.

Code: [`code/extensions/Task_02_extension.py`](../code/extensions/Task_02_extension.py) · Output: [`outputs/Task_02_extension_output.txt`](../outputs/Task_02_extension_output.txt)

## D. Meaning of the output
Mean 23.12 °C, minimum 17.50 °C (03:00), maximum 29.40 °C (12:00). The first Fahrenheit values (65.3, 64.4, …) are the same readings on another scale.

## E. Related real-world case
- **Case:** IoT soil-moisture sensor, 24 hourly readings (% volumetric water content).
- **Assumptions / input data:** Synthetic readings; irrigation needed below 22 %.
- **Output:** Mean 27.62 %, min 18 %, max 36 %; 4 hours below threshold (hours 11–14). Min-max normalisation maps readings to [0,1].
- **Interpretation:** Moisture falls through the day and is below threshold around midday, so irrigation is needed then. The jump after hour 14 indicates a watering/rain event.
