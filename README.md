# rocket_relations

This is a python package that can be used for computing characteristic velocity (c_star) and thrust coefficient (c_f) under ideal rocket metrics and assumptions (Calorically perfect gas, isentropic flow, steady quasi-1D nozzle expansion, and choked throat conditions)

## Installation

Create or activate your conda environment:

```bash
conda create -n rocketenv python=3.14
conda activate rocketenv
pip install -e .
```
After installing, run:

```python 
import rocket_relations
help(rocket_relations)
```
## Quickstart 

```python
from rocket_relations import c_star, c_f

# c*
gamma, R, T0 = 1.2, 350, 3500
print(c_star(gamma, R, T0)) # should be around 1706.6214

# C_F
gamma = 1.2
pe_p0, pa_p0, Ae_Astar = 0.0125, 0.02, 10
print(c_f(gamma, pe_p0, pa_p0, Ae_Astar)) # should be around 1.5423079
```

## Docs

Each function has a NumPy-stle docstring with types, units, and constraints 

```python 
help(rocket_relations.c_star)
help(rocket_relations.c_f)
```

## Tests

Run tests from the project root:

```bash 
pytest -q
```

Expected:

2 passed
