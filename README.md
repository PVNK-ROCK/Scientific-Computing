# BIT 2118: Scientific Computing: Group Work (Tasks 7 and 8)


Each task contains: (1) the inputs and mathematical operation, (2) the program output, (3) an interpretation in words
(including the graph where there is one), (4) a change of at least one input/parameter with an explanation of how the
result changes, and (5) a modified program solving a different, related real-world case with its assumptions,
input data, output and interpretation.

| Task | Documentation | Given program | Modified program | New real-world case |
|---|---|---|---|---|
| 7 | [Gaussian Elimination and LU Decomposition](docs/Task_07_gaussian_lu.md) | `code/Task_07_gaussian_lu.py` | `code/Task_07_extension.py` | Displacements of a spring-mass structure under three load cases |
| 8 | [Iterative Methods for Linear Systems](docs/Task_08_iterative_linear.md) | `code/Task_08_iterative_linear.py` | `code/Task_08_extension.py` | Steady-state heat conduction along a metal rod |

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── code/     # given programs and extension programs for Tasks 7 and 8
├── docs/     # write-ups for Tasks 7 and 8
└── images/   # graphs produced by the Task 8 programs
```

## How to run

```bash
pip install -r requirements.txt
# run from the repository root so graphs are saved in ./images
python code/Task_07_gaussian_lu.py
python code/Task_07_extension.py
python code/Task_08_iterative_linear.py
python code/Task_08_extension.py
```

Timings in Task 7 vary between computers.
