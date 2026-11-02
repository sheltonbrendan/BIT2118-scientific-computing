import numpy as np

def system(n, left, right):
    A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n); b[0] = left; b[-1] = right
    return A, b

def jacobi(A, b, tol):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b)
    for k in range(1, 20000):
        xn = (b - R @ x)/D
        if np.max(np.abs(xn-x)) < tol: return xn, k
        x = xn
    return x, k

def gs(A, b, tol):
    x = np.zeros_like(b)
    for k in range(1, 20000):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i,:i]@x[:i] - A[i,i+1:]@old[i+1:])/A[i,i]
        if np.max(np.abs(x-old)) < tol: return x, k
    return x, k

# --- Parameter change: right boundary 20 -> 60 C; tolerance 1e-8 -> 1e-4 (n=5) ---
for right, tol in ((20, 1e-8), (60, 1e-8), (20, 1e-4)):
    A, b = system(5, 100, right)
    xj, kj = jacobi(A, b, tol); xg, kg = gs(A, b, tol)
    err = np.max(np.abs(xg - np.linalg.solve(A, b)))
    print(f"right={right}, tol={tol:.0e}: Jacobi {kj} it, Gauss-Seidel {kg} it, GS error vs direct {err:.2e}")

# --- New case: 1-D metal rod, 30 interior nodes, ends 100 C and 0 C ---
A, b = system(30, 100, 0)
xj, kj = jacobi(A, b, 1e-6); xg, kg = gs(A, b, 1e-6)
ex = np.linalg.solve(A, b)
print(f"Rod (30 nodes): Jacobi {kj} it, Gauss-Seidel {kg} it")
print("Temperatures at nodes 1, 15, 30 (GS):", np.round(xg[[0,14,29]], 3))
print("Exact at nodes 1, 15, 30:", np.round(ex[[0,14,29]], 3))
