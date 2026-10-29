"""Task 8 extension: (A) change boundaries & tolerance, (B) heat conduction in a 20-point rod."""
import os
import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, tol, max_iter=20000):
    D = np.diag(A); R = A - np.diagflat(D); x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        xn = (b - R @ x) / D
        if np.linalg.norm(xn - x, np.inf) < tol:
            return xn, k
        x = xn
    return x, max_iter

def gauss_seidel(A, b, tol, max_iter=20000):
    x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        if np.linalg.norm(x - old, np.inf) < tol:
            return x, k
    return x, max_iter

def rod_system(n, left, right):
    A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n); b[0] = left; b[-1] = right
    return A, b

print("=== PART A: change boundary temperatures (80 C, 30 C) and tolerance ===")
A, b = rod_system(5, 80.0, 30.0)
for tol in (1e-4, 1e-8):
    xj, kj = jacobi(A, b, tol); xg, kg = gauss_seidel(A, b, tol)
    print(f"tol={tol:.0e}: Jacobi {kj} its, Gauss-Seidel {kg} its, GS temps={np.round(xg, 3)}")
print("Direct solution:", np.round(np.linalg.solve(A, b), 3))

print("\n=== PART B: metal rod, 20 interior points, ends held at 150 C and 30 C ===")
n = 20
A, b = rod_system(n, 150.0, 30.0)
xj, kj = jacobi(A, b, 1e-6); xg, kg = gauss_seidel(A, b, 1e-6)
print(f"Jacobi iterations: {kj}; Gauss-Seidel iterations: {kg}")
print("Temperature at middle point (GS):", round(xg[n // 2], 3), "C")
print("Max difference from direct solution:", f"{np.max(np.abs(xg - np.linalg.solve(A, b))):.2e}")
pos = np.arange(1, n + 1)
plt.plot(pos, xg, "o-", label="Gauss-Seidel")
plt.plot(pos, 150 - (150 - 30) * pos / (n + 1), "--", label="Analytical straight line")
plt.xlabel("Interior grid point"); plt.ylabel("Temperature (C)")
plt.title("Steady-state temperature along a heated rod"); plt.legend(); plt.grid(True)
os.makedirs("images", exist_ok=True)
plt.savefig("images/task_08_rod_extension.png", dpi=150, bbox_inches="tight")
