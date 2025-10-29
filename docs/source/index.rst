Welcome to rocket_relations
===========================

This package provides formulas for evaluating ideal rocket flow relations,
including characteristic velocity (c*) and thrust coefficient (c_f) under
calorically perfect gas and isentropic nozzle assumptions.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   rocket_relations
   api

Usage Example
-------------

.. code-block:: python

    from rocket_relations import c_star, c_f

    gamma = 1.2
    R = 350
    T0 = 3500

    print(c_star(gamma, R, T0))

