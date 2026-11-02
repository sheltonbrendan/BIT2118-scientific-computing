import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve

# --- Parameter change: diagonal 4 -> 6 (stronger diagonal) ---
for d in (4.0, 6.0):
    A = np.array([[d,-1,0],[-1,d,-1],[0,-1,d-1]], dtype=float)
    print(f"diag={d}: solution for b=[15,10,10] ->", np.round(np.linalg.solve(A, [15,10,10]), 4))

# --- New case: 400-node spring/structure model, 300 load cases: LU once vs solve each time ---
n, m = 400, 300
rng = np.random.default_rng(1)
K = np.diag(np.full(n, 4.0)) + np.diag(np.full(n-1, -1.0), 1) + np.diag(np.full(n-1, -1.0), -1)
loads = rng.uniform(0, 10, (n, m))

def repeated():
    return [np.linalg.solve(K, loads[:, j]) for j in range(m)]
def lu_reuse():
    lu, piv = lu_factor(K)
    return [lu_solve((lu, piv), loads[:, j]) for j in range(m)]

t1 = timeit.timeit(repeated, number=1)
t2 = timeit.timeit(lu_reuse, number=1)
a, b = repeated()[0], lu_reuse()[0]
print(f"Repeated solve: {t1:.4f}s | LU reuse: {t2:.4f}s | speed-up {t1/t2:.1f}x")
print("Max difference between methods:", np.max(np.abs(a-b)))
