# Task 03: Mathematical Functions and Vectorization

Program: [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py) · Output: [`outputs/Task_03_vectorization_output.txt`](../outputs/Task_03_vectorization_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 1,000,000 random latencies in ms (uniform 5–250), seed 42.
- **Operation:** ms → s (÷1000) then square, done with a Python loop and with one vectorized expression; timed with `timeit`.

## C. Parameter change
Array size 1,000,000 → 10,000. Speed-up in the extension run: 56.8× (1M) and 119× (10k). Vectorization wins at every size because it avoids per-element interpreter overhead. Exact timings vary between runs and machines (original run: 23.5×).

Code: [`code/extensions/Task_03_extension.py`](../code/extensions/Task_03_extension.py) · Output: [`outputs/Task_03_extension_output.txt`](../outputs/Task_03_extension_output.txt)

## D. Meaning of the output
Squared latencies in s² (e.g. 0.0379 s² for the first reading). Loop 0.486 s vs vectorized 0.021 s: same result, far less time.

## E. Related real-world case
- **Case:** Converting 12-bit ADC counts (0–4095, 3.3 V reference) from a sensor into volts and computing RMS voltage.
- **Assumptions / input data:** ADC counts uniform random; V = count × 3.3/4095.
- **Output:** Mean 1.6510 V, RMS 1.9059 V, max 3.3000 V.
- **Interpretation:** RMS (1.906 V) exceeds the mean (1.651 V) because squaring weights larger values more; for uniform data RMS ≈ 3.3/√3 ≈ 1.905 V, matching.
