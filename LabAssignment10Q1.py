import random
import numpy as np

NUM_JOBS = 6
NUM_MACHINES = 3
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
GENERATIONS = 50

JOB_TIMES = [random.randint(1, 10) for _ in range(NUM_JOBS)]

def initialize_population():
    return [np.random.randint(0, NUM_MACHINES, NUM_JOBS).tolist() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    machine_loads = [0] * NUM_MACHINES
    for job, machine in enumerate(chromosome):
        machine_loads[machine] += JOB_TIMES[job]
    return 1 / max(machine_loads)

def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    return population[np.random.choice(range(POPULATION_SIZE), p=probabilities)]

def crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(NUM_JOBS), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_JOBS - 1)
        chromosome[index] = random.randint(0, NUM_MACHINES - 1)

def genetic_algorithm():
    population = initialize_population()
    for generation in range(GENERATIONS):
        fitness_scores = [fitness(chrom) for chrom in population]
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = selection(population, fitness_scores), selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:POPULATION_SIZE]
    
    best_chromosome = max(population, key=fitness)
    return best_chromosome, fitness(best_chromosome)

best_schedule, best_fitness = genetic_algorithm()
print("Best Schedule:", best_schedule)
print("Best Fitness:", best_fitness)

