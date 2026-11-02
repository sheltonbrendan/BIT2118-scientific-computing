import numpy as np
pts = np.array([[0.,0.],[1.,0.],[1.,1.],[0.,1.]])

def transform(angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    R = np.array([[np.cos(a), -np.sin(a)],[np.sin(a), np.cos(a)]])
    S = np.diag([sx, sy])
    T = R @ S
    return T, pts @ T.T

# --- Parameter change: 90 deg rotation, scale (3, 1) ---
T, out = transform(90, 3.0, 1.0)
print("Matrix:\n", np.round(T, 4)); print("Points:\n", np.round(out, 4))
print("Determinant:", round(np.linalg.det(T), 4))

# --- New case: drone waypoints, rotate by heading 30 deg and translate (+10, +5) m
#     using homogeneous coordinates (3x3 matrix) ---
way = np.array([[0,0],[10,0],[10,10],[0,10]], dtype=float)
h = np.deg2rad(30)
H = np.array([[np.cos(h), -np.sin(h), 10],
              [np.sin(h),  np.cos(h),  5],
              [0, 0, 1]])
hom = np.c_[way, np.ones(len(way))]
world = (hom @ H.T)[:, :2]
print("Waypoints (drone frame):\n", way)
print("Waypoints (world frame):\n", np.round(world, 3))
print("Side length preserved:", np.round(np.linalg.norm(world[1]-world[0]), 3), "m")
