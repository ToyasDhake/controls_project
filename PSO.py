import pyswarms as ps
import test


# calculate distance from expected value for each position by forward kinematic, sum it and return
def costFunction(x):
    """Sphere objective function.

    Has a global minimum at :code:`0` and with a search domain of
        :code:`[-inf, inf]`

    Parameters
    ----------
    x : numpy.ndarray
        set of inputs of shape :code:`(n_particles, dimensions)`

    Returns
    -------
    numpy.ndarray
        computed cost of size :code:`(n_particles, )`
    """
    j = []
    for i in x:
        j.append(test.test(i[0], i[1], i[2]))
    return j
def runPSO(val):
    options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=3, options=options)
    cost, pos = optimizer.optimize(costFunction, iters=val)
    return optimizer.cost_history, pos
