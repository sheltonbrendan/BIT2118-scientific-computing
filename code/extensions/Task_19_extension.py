import numpy as np
from scipy.optimize import minimize, linprog

def solve(cost_a, cost_b, cap_a, cap_b, need):
    r = minimize(lambda z: cost_a*z[0]+cost_b*z[1], x0=[5,3], method="SLSQP",
                 bounds=[(0,None)]*2,
                 constraints={"type":"ineq","fun":lambda z: cap_a*z[0]+cap_b*z[1]-need})
    best = min(((cost_a*a+cost_b*b, a, b) for a in range(40) for b in range(40) if cap_a*a+cap_b*b >= need))
    return r, best

# --- Parameter change: capacity need 1000 -> 2000 ; cost of B 18 -> 15 ---
for need, cb in ((1000,18),(2000,18),(1000,15)):
    r, best = solve(12, cb, 100, 170, need)
    print(f"need={need}, costB={cb}: continuous A={r.x[0]:.3f}, B={r.x[1]:.3f}, cost={r.fun:.2f} | integer (cost,A,B)={best}")

# --- New case: factory production mix (maximise profit) with linprog ---
# Chairs: profit 45, 3 h carpentry, 1 h finishing ; Tables: profit 80, 4 h carpentry, 3 h finishing
# Available: 240 h carpentry, 120 h finishing
res = linprog(c=[-45, -80], A_ub=[[3,4],[1,3]], b_ub=[240,120], bounds=[(0,None)]*2)
print(f"Optimal mix: chairs={res.x[0]:.2f}, tables={res.x[1]:.2f}, max profit={-res.fun:.2f}")
print("Carpentry used:", 3*res.x[0]+4*res.x[1], "h | Finishing used:", res.x[0]+3*res.x[1], "h")
best = max((45*c+80*t, c, t) for c in range(81) for t in range(41) if 3*c+4*t <= 240 and c+3*t <= 120)
print("Best whole-number plan (profit, chairs, tables):", best)
