"""Task 7 extension: (A) change problem size and compare timing, (B) spring-mass structure."""
import numpy as np, timeit
from scipy.linalg import lu_factor, lu_solve

print("=== PART A: change the matrix size n and the number of right-hand sides ===")
rng = np.random.default_rng(0)
for n, m in ((200, 50), (800, 50), (800, 200)):
    A = rng.random((n, n)) + n * np.eye(n)
    B = rng.random((n, m))
    t_solve = min(timeit.repeat(lambda: [np.linalg.solve(A, B[:, j]) for j in range(m)], number=1, repeat=3))
    def lu_way():
        lu, piv = lu_factor(A)
        return [lu_solve((lu, piv), B[:, j]) for j in range(m)]
    t_lu = min(timeit.repeat(lu_way, number=1, repeat=3))   # best of 3 runs reduces timing noise
    print(f"n={n}, {m} right-hand sides: repeated solve={t_solve:.3f} s, LU once={t_lu:.3f} s, ratio={t_solve/t_lu:.1f}x")

print("\n=== PART B: chain of 4 masses joined by springs (3 load cases) ===")
# Stiffness matrix K (N/mm) for a fixed-end chain; unknown = displacements u (mm); K u = F
K = 50.0 * np.array([[ 2., -1.,  0.,  0.],
                     [-1.,  2., -1.,  0.],
                     [ 0., -1.,  2., -1.],
                     [ 0.,  0., -1.,  2.]])
loads = {"Light": [10, 0, 0, 0], "Mid-span": [0, 40, 40, 0], "Heavy end": [0, 0, 0, 100]}
lu, piv = lu_factor(K)
for name, F in loads.items():
    u = lu_solve((lu, piv), np.array(F, dtype=float))
    print(f"{name:10s} load {F}: displacements (mm) = {np.round(u, 4)}, max = {u.max():.4f} mm")
