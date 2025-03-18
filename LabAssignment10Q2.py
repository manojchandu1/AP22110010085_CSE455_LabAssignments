import random
import numpy as np

NUM_ITEMS = 10
BIN_CAPACITY = 15
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
GENERATIONS = 50
ITEM_SIZES = [random.randint(1, 10) for _ in range(NUM_ITEMS)]


def initialize_population():
    return [[random.randint(0, len(ITEM_SIZES) - 1) for _ in range(NUM_ITEMS)] for _ in range(POPULATION_SIZE)]


def fitness(chromosome):
    bins = {}
    for item, bin_index in enumerate(chromosome):
        if bin_index not in bins:
            bins[bin_index] = 0
        bins[bin_index] += ITEM_SIZES[item]
    overfilled = sum(max(0, bins[b] - BIN_CAPACITY) for b in bins)
    return 1 / (len(bins) + overfilled + 1)


def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    return population[np.random.choice(range(POPULATION_SIZE), p=probabilities)]


def crossover(parent1, parent2):
    point = random.randint(1, NUM_ITEMS - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]


def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_ITEMS - 1)
        chromosome[index] = random.randint(0, NUM_ITEMS - 1)


def genetic_algorithm():
    population = initialize_population()
    for _ in range(GENERATIONS):
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


best_packing, best_fitness = genetic_algorithm()
print("Best Packing:", best_packing)
print("Best Fitness:", best_fitness)

