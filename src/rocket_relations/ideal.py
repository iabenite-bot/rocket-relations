"""
ideal.py

Ideal rocket equations from part (c) of HW5, computing c* and C_F under
the assumptions: calorically perfect gas,isentropic flow, steady quasi-1D nozzle expansion,
and choked throat conditions.

Functions
---------
c_star(gamma, R, T0)
    Computes the ideal characteristic velocity c* [m/s]

c_f(gamma, pe_p0, pa_p0, Ae_Astar)
    Computes the ideal thrust coefficient C_F (dimensionless)
"""

import numbers
import numpy as np


def c_star(gamma, R, T0):
    """
    Compute the ideal characteristic velocity c*

    Parameters
    ----------
    gamma : float or numpy.ndarray
        Ratio of specific heats (must be > 1)
    R : float or numpy.ndarray
        Specific gas constant [J/(kg*K)] (must be > 0)
    T0 : float or numpy.ndarray
        Stagnation (total) temperature [K] (must be > 0)

    Returns
    -------
    float or numpy.ndarray
        Characteristic velocity c* [m/s]

    Notes
    -----
    Formula (PDF Eq. 1):
        c* = sqrt( (1/gamma) * ((gamma+1)/2)^((gamma+1)/(gamma-1)) * R * T0 )
    """

    # Type checking
    for x in (gamma, R, T0):
        if not isinstance(x, numbers.Number) and not isinstance(x, np.ndarray):
            raise TypeError("All inputs must be numeric (float, int, or numpy array).")

    # Domain validation
    if np.any(gamma <= 1):
        raise ValueError("gamma must be > 1.")
    if np.any(R <= 0):
        raise ValueError("R must be > 0.")
    if np.any(T0 <= 0):
        raise ValueError("T0 must be > 0.")

    exponent = (gamma + 1) / (gamma - 1)
    term = ((gamma + 1) / 2) ** exponent

    return np.sqrt((1 / gamma) * term * R * T0)


def c_f(gamma, pe_p0, pa_p0, Ae_Astar):
    """
    Compute the ideal thrust coefficient C_F

    Parameters
    ----------
    gamma : float or numpy.ndarray
        Ratio of specific heats (must be > 1)
    pe_p0 : float or numpy.ndarray
        Exit-to-chamber pressure ratio p_e/p_0 (must be in [0, 1))
    pa_p0 : float or numpy.ndarray
        Ambient-to-chamber pressure ratio p_a/p_0 (must be in [0, 1))
    Ae_Astar : float or numpy.ndarray
        Nozzle area ratio A_e/A* (must be >= 1)

    Returns
    -------
    float or numpy.ndarray
        Thrust coefficient C_F (dimensionless)

    Notes
    -----
    Formula (PDF Eq. 2):
        C_F = sqrt( (2*gamma^2/(gamma-1)) * (2/(gamma+1))^((gamma+1)/(gamma-1))
                     * (1 - (p_e/p_0)^((gamma-1)/gamma)) ) + (p_e/p_0 - p_a/p_0)*(A_e/A*)
    """

    # Type checking
    for x in (gamma, pe_p0, pa_p0, Ae_Astar):
        if not isinstance(x, numbers.Number) and not isinstance(x, np.ndarray):
            raise TypeError("All inputs must be numeric (float, int, or numpy array).")

    # Domain validation
    if np.any(gamma <= 1):
        raise ValueError("gamma must be > 1.")
    if np.any((pe_p0 < 0) | (pe_p0 >= 1)):
        raise ValueError("pe/p0 must be in the range [0, 1).")
    if np.any((pa_p0 < 0) | (pa_p0 >= 1)):
        raise ValueError("pa/p0 must be in the range [0, 1).")
    if np.any(Ae_Astar < 1):
        raise ValueError("A_e/A* must be >= 1.")

    exponent = (gamma + 1) / (gamma - 1)

    term1 = np.sqrt(
        (2 * gamma**2 / (gamma - 1))
        * (2 / (gamma + 1)) ** exponent
        * (1 - pe_p0 ** ((gamma - 1) / gamma))
    )

    term2 = (pe_p0 - pa_p0) * Ae_Astar

    return term1 + term2

