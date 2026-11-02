import numpy as np
from decimal import Decimal

# --- Parameter change: better approximation of sqrt(2) ---
for approx in (1.414, 1.4142, 1.41421356):
    ae = abs(np.sqrt(2) - approx)
    print(f"approx={approx}: abs error={ae:.2e}, rel error={ae/np.sqrt(2):.4%}")

# --- New case: banking, 1000 transactions of 0.10 should total 100.00 ---
naive = 0.0
for _ in range(1000):
    naive += 0.10
exact = sum(Decimal("0.10") for _ in range(1000))
print("Float sum:", repr(naive), "| Equal to 100.0:", naive == 100.0, "| isclose:", np.isclose(naive, 100.0))
print("Error:", abs(naive - 100.0))
print("Decimal sum:", exact)
cents = sum(10 for _ in range(1000))   # integer cents
print("Integer-cents sum:", cents/100)
