import numpy as np
from scipy.optimize import curve_fit

users = np.array([50,100,150,200,250,300,350], float)
resp = np.array([82,95,115,145,185,238,305], float)
rmse = lambda y, p: np.sqrt(np.mean((y-p)**2))

# --- Parameter change: model choice (linear vs quadratic vs cubic) ---
for deg in (1, 2, 3):
    c = np.polyfit(users, resp, deg)
    print(f"Polynomial degree {deg}: RMSE={rmse(resp, np.polyval(c, users)):.2f} ms, prediction at 400 users={np.polyval(c, 400):.1f} ms")

# --- New case: exponential growth of mobile-payment transactions (millions/month) ---
# Illustrative synthetic data
months = np.arange(0, 12, dtype=float)
tx = np.array([10.2,11.1,12.4,13.2,14.9,16.1,17.8,19.9,21.6,24.3,26.5,29.4])
model = lambda t, a, r: a*np.exp(r*t)
(a, r), cov = curve_fit(model, months, tx, p0=[10, 0.1])
pred = model(months, a, r)
ss_res = np.sum((tx-pred)**2); ss_tot = np.sum((tx-tx.mean())**2)
print(f"Fitted: y = {a:.3f} * exp({r:.4f} t)")
print(f"Monthly growth rate: {np.exp(r)-1:.2%} | Doubling time: {np.log(2)/r:.2f} months")
print(f"RMSE: {rmse(tx, pred):.3f} M | R^2: {1-ss_res/ss_tot:.4f}")
print(f"Forecast month 15: {model(15, a, r):.2f} M | Std error of a, r: {np.sqrt(np.diag(cov)).round(4)}")
