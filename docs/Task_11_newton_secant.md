# Task 11: Root Finding: Newton-Raphson and Secant Methods

Program: [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py) · Output: [`outputs/Task_11_newton_secant_output.txt`](../outputs/Task_11_newton_secant_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** Cash flows [−10000, 3000, 3500, 4000, 2500]; Newton start 0.10; secant starts 0.05 and 0.20.
- **Operation:** Solve NPV(r) = 0 for the internal rate of return.

## C. Parameter change
Final inflow 2500 → 4500: IRR 11.54 % → 17.09 %. Newton start 0.10 → 4 iterations; 0.50 → 7; 1.0 → converges to a meaningless −154.4 % root. Starting guess matters.

Code: [`code/extensions/Task_11_extension.py`](../code/extensions/Task_11_extension.py) · Output: [`outputs/Task_11_extension_output.txt`](../outputs/Task_11_extension_output.txt)

## D. Meaning of the output
IRR = 11.542461 % by both methods; NPV at the root ≈ 0, so discounting at this rate makes the investment break even.

## E. Related real-world case
- **Case:** Effective interest rate of a loan: borrow 50,000, repay 4,500 monthly for 12 months.
- **Assumptions / input data:** f(i) = 50000 − 4500·(1−(1+i)^−12)/i, secant from 0.01 and 0.05.
- **Output:** Monthly rate 1.2043 %, nominal annual 14.45 %, effective annual 15.45 % (6 iterations).
- **Interpretation:** Although the repayments look simple, the true annual cost of the loan is 15.45 %.
