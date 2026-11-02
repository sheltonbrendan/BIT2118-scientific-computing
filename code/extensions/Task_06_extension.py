import numpy as np
A = np.array([[4.,2.],[8.,12.]])

# --- Parameter change: totals 26 CPU, 76 GB ---
sol = np.linalg.solve(A, np.array([26.,76.]))
print("New totals -> Type A, Type B:", sol)

# --- New case: 3-loop mesh circuit (mesh currents, amps)
# Loop1: 10I1 - 4I2        = 12
# Loop2: -4I1 + 12I2 - 3I3 = 0
# Loop3:      -3I2 + 8I3   = -6   (battery opposes)
R = np.array([[10.,-4.,0.],[-4.,12.,-3.],[0.,-3.,8.]])
V = np.array([12.,0.,-6.])
I = np.linalg.solve(R, V)
print("Mesh currents I1,I2,I3 (A):", np.round(I, 4))
print("Residual norm:", np.linalg.norm(V - R @ I))
print("Condition number:", round(np.linalg.cond(R), 3))
