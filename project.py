import numpy as np

def rosenbrock(x, y, a=1, b=100):
    return (a - x) ** 2 + b * (y - x ** 2) ** 2

def generate_population(size, bounds):
    population = np.random.rand(size, len(bounds))
    for i, (lower, upper) in enumerate(bounds):
        population[:, i] = lower + population[:, i] * (upper - lower)
    return population

def compute_fitness(population):
    fitness = -rosenbrock(population[:, 0], population[:, 1])
    return fitness

def select_parents(population, fitness, num_parents):
    parents = np.empty((num_parents, population.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[parent_num, :] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -np.inf
    return parents

def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1]/2)
    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 1] += random_value * 0.1
    return offspring_crossover

bounds = [(-2, 2), (-1, 3)]
population_size = 10
num_generations = 20
num_parents_mating = 4

population = generate_population(population_size, bounds)
for generation in range(num_generations):
    fitness = compute_fitness(population)
    parents = select_parents(population, fitness, num_parents_mating)
    offspring_crossover = crossover(parents, (population_size - parents.shape[0], population.shape[1]))
    offspring_mutation = mutation(offspring_crossover)
    population[0:parents.shape[0], :] = parents
    population[parents.shape[0]:, :] = offspring_mutation

print("Best fitness in Generation {}: {}".format(generation, np.max(fitness)))
best_match_idx = np.where(fitness == np.max(fitness))
print("Best solution: ", population[best_match_idx[0][0], :])
print("Best solution fitness: ", fitness[best_match_idx[0][0]])
