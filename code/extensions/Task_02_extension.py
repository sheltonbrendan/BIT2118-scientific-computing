import numpy as np
# --- Parameter change: heatwave, every reading +5 C ---
base = np.array([18.5,18.0,17.8,17.5,17.9,19.0,21.5,23.8,25.6,27.1,28.3,29.0,
                 29.4,29.1,28.5,27.6,26.2,24.8,23.4,22.1,21.0,20.2,19.6,19.0])
hot = base + 5
print(f"Original mean/min/max: {base.mean():.2f} / {base.min():.2f} / {base.max():.2f} C")
print(f"Heatwave mean/min/max: {hot.mean():.2f} / {hot.min():.2f} / {hot.max():.2f} C")

# --- New case: IoT soil-moisture sensor (% volumetric water content), 24 hourly readings ---
moisture = np.array([32,31,30,29,28,27,26,25,24,23,22,21,
                     20,19,18,28,36,35,34,33,32,31,30,29], dtype=float)
threshold = 22.0                      # irrigate below this
dry = moisture < threshold
normalised = (moisture - moisture.min()) / (moisture.max() - moisture.min())
print(f"Mean moisture: {moisture.mean():.2f} %  Min: {moisture.min():.0f} %  Max: {moisture.max():.0f} %")
print(f"Hours below {threshold:.0f} %: {dry.sum()} (hours {np.where(dry)[0].tolist()})")
print("Min-max normalised (first 6):", np.round(normalised[:6], 3))
