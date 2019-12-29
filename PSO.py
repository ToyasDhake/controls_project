import pyswarms as ps
import test

def costFunction(x):

    j = []
    for i in x:
        j.append(test.test(i[0], i[1], i[2]))
    return j
def runPSO(val):
    options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=3, options=options)
    cost, pos = optimizer.optimize(costFunction, iters=val)
    return optimizer.cost_history, pos
runPSO(5)