from scipy.optimize import root_scalar

# --- Parameter change: higher final cash inflow and different start guess ---
def make(cf):
    npv = lambda r: sum(c/(1+r)**t for t, c in enumerate(cf))
    d = lambda r: sum(-t*c/(1+r)**(t+1) for t, c in enumerate(cf) if t > 0)
    return npv, d
for cf in ([-10000,3000,3500,4000,2500], [-10000,3000,3500,4000,4500]):
    npv, d = make(cf)
    s = root_scalar(npv, fprime=d, x0=0.10, method="newton")
    print(f"cash flows {cf}: IRR={s.root:.4%}, iterations={s.iterations}")
npv, d = make([-10000,3000,3500,4000,2500])
for x0 in (0.10, 0.50, 1.0):
    s = root_scalar(npv, fprime=d, x0=x0, method="newton")
    print(f"Newton start x0={x0}: root={s.root:.6%}, iterations={s.iterations}")

# --- New case: effective loan rate. Borrow 50,000; repay 4,500 per month for 12 months ---
P, pay, n = 50000, 4500, 12
f  = lambda i: P - pay*(1-(1+i)**-n)/i
sec = root_scalar(f, x0=0.01, x1=0.05, method="secant", xtol=1e-12)
print(f"Monthly rate (secant): {sec.root:.6%} | iterations: {sec.iterations}")
print(f"Nominal annual rate: {12*sec.root:.4%} | Effective annual rate: {(1+sec.root)**12-1:.4%}")
