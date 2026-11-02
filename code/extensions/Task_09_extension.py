import numpy as np

def centrality(A):
    w, V = np.linalg.eig(A)
    i = np.argmax(w.real)
    v = np.abs(V[:, i].real)
    return w[i].real, v/v.sum()

A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], float)
# --- Parameter change: add link A-D ---
A2 = A.copy(); A2[0,3] = A2[3,0] = 1
for name, M in (("original", A), ("with A-D link", A2)):
    lam, c = centrality(M)
    print(f"{name}: lambda={lam:.4f}, centrality={np.round(c,4)}")

# --- New case: PageRank on 4 web pages (damping 0.85) ---
# links: P1->P2,P3 ; P2->P3 ; P3->P1 ; P4->P3
L = np.array([[0,1,1,0],[0,0,1,0],[1,0,0,0],[0,0,1,0]], float)
M = (L / L.sum(axis=1, keepdims=True)).T         # column-stochastic
d, n = 0.85, 4
G = d*M + (1-d)/n*np.ones((n,n))
w, V = np.linalg.eig(G)
i = np.argmax(w.real)
pr = np.abs(V[:, i].real); pr /= pr.sum()
print("Dominant eigenvalue of Google matrix:", round(w[i].real, 6))
for p, s in zip(("P1","P2","P3","P4"), pr):
    print(f"PageRank {p}: {s:.4f}")
