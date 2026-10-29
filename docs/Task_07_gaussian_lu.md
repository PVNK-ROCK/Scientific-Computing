# Task 7: Gaussian Elimination and LU Decomposition

**Concept:** LU decomposition factors A = LU (with pivoting, PA = LU). Once A is factored, each new right-hand side b is solved cheaply by forward and back substitution.

**Files:** [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py) (given program) · [`code/Task_07_extension.py`](../code/Task_07_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** a 3 × 3 coefficient matrix A and three measurement vectors b.
- **Mathematical operations:** `lu_factor(A)` once, then `lu_solve` for each b; residual b − Ax checks accuracy; `np.linalg.solve` gives a comparison.

## 2. Output of the program

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## 3. Interpretation of the output

For the first measurement set the solution is x = [5, 5, 5], identical to the direct solver. The other two sets give different x (for example [5.317, 5.268, 4.756]) using the *same* factorisation. All residual norms are about 10⁻¹⁵ (machine precision), so each solution is accurate. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** the matrix size n (200, 800) and the number of right-hand sides m (50, 200) were increased, and the times for solving from scratch each time vs. LU-once were compared.

```text
n=200, 50 right-hand sides: repeated solve=0.019 s, LU once=0.002 s, ratio=12.9x
n=800, 50 right-hand sides: repeated solve=0.537 s, LU once=0.027 s, ratio=19.6x
n=800, 200 right-hand sides: repeated solve=2.574 s, LU once=0.072 s, ratio=36.0x
```

**How the result changes:** LU-once is faster in every case, and its advantage rises from roughly **11× to about 40×** as the matrix size and the number of right-hand sides grow (exact ratios vary slightly between runs and computers). Factorisation costs about n³ operations but is paid once; each extra solve costs only about n². Solving from scratch repeats the n³ work every time.

## 5. Modified program for a different but related real-world case

**Case:** Displacements of a spring-mass structure under three load cases

**New assumptions**

- A chain of 4 masses connected by springs with stiffness 50 N/mm and fixed at both ends, giving the stiffness matrix K = 50·tridiag(−1, 2, −1).
- Equation K·u = F, where u = displacements (mm) and F = loads (N).
- Three load cases: a light end load, a mid-span load and a heavy end load.

**Input data:** Loads: [10,0,0,0], [0,40,40,0], [0,0,0,100] N in `code/Task_07_extension.py`.

**Output**

```text
Light      load [10, 0, 0, 0]: displacements (mm) = [0.16 0.12 0.08 0.04], max = 0.1600 mm
Mid-span   load [0, 40, 40, 0]: displacements (mm) = [0.8 1.6 1.6 0.8], max = 1.6000 mm
Heavy end  load [0, 0, 0, 100]: displacements (mm) = [0.4 0.8 1.2 1.6], max = 1.6000 mm
```

**Interpretation:** K is factored **once** and reused for the three load cases, which is how structural software handles many load combinations. The mid-span load of 40 N on each middle mass produces displacements up to 1.6 mm in the middle; the 100 N end load produces displacements that grow linearly toward the loaded end (0.4, 0.8, 1.2, 1.6 mm). Doubling a load would exactly double the displacement, because the system is linear.
