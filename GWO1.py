import pygmo as pg

# The problem
prob = pg.problem(pg.rosenbrock(dim = 10))
# The initial population
pop = pg.population(prob, size = 20)
# The algorithm (a self-adaptive form of Differential Evolution (sade - jDE variant)
algo = pg.algorithm(pg.sade(gen = 1000))
 # The actual optimization process
pop = algo.evolve(pop)
# Getting the best individual in the population
best_fitness = pop.get_f()[pop.best_idx()]
print(best_fitness)