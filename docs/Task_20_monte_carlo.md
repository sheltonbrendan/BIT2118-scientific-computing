# Task 20: Random Numbers and Monte Carlo Methods

Program: [`code/Task_20_monte_carlo.py`](../code/Task_20_monte_carlo.py) · Output: [`outputs/Task_20_monte_carlo_output.txt`](../outputs/Task_20_monte_carlo_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Demand ~ Normal(850, 120), capacity 1000, N = 100,000, seed 42.
- **Operation:** Simulate demand, count demand > capacity, estimate overload probability.

## C. Parameter change
N = 1,000 / 100,000 / 1,000,000: estimate 10.10 % / 10.62 % / 10.57 % (exact 10.565 %). Capacity 1000 → 1100: probability 10.6 % → 1.9 %. Error shrinks roughly as 1/√N.

Code: [`code/extensions/Task_20_extension.py`](../code/extensions/Task_20_extension.py) · Output: [`outputs/Task_20_extension_output.txt`](../outputs/Task_20_extension_output.txt)

## D. Meaning of the output
Estimated overload probability 10.616 % (10,616 of 100,000 runs). Graph (`outputs/figures/Task_20_monte_carlo.png`): the running estimate fluctuates early and settles near 0.106 as simulations increase.

## E. Related real-world case
- **Case:** (a) Estimating π; (b) project-delay risk with three sequential tasks.
- **Assumptions / input data:** (b) Triangular durations (5,8,15), (7,10,20), (4,6,12) days; deadline 30 days; 200,000 runs.
- **Output:** π estimates: 3.19600 (N=1,000), 3.14476 (100,000), 3.14174 (5,000,000). Project: mean 29.02 days, 5–95 % range 23.0–35.7 days, P(>30 days) = 38.63 %.
- **Interpretation:** Although the mean is under 30 days, the right-skewed durations give a 39 % chance of missing the deadline.
