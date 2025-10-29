import pytest 
import numpy as np
from rocket_relations import c_star, c_f

def test_c_star():
    gamma = 1.2
    R = 350
    T0 = 3500
    result = c_star(gamma, R, T0)
    assert np.isclose(result, 1706.6214, rtol=1e-5)

def test_c_f():
    gamma = 1.2
    pe_p0 = 0.0125
    pa_p0 = 0.02
    area_ratio = 10
    result = c_f(gamma, pe_p0, pa_p0, area_ratio)
    assert np.isclose(result, 1.5423079, rtol=1e-5)
