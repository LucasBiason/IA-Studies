import random
import itertools
import math
import copy
import numpy as np
from typing import List, Tuple

from pygame_ga_base import PyGameGA


class GeneticAlgorithm(PyGameGA):
    """
    A class to represent a Genetic Algorithm for solving optimization problems.
    """

    def __init__(self, population_size: int, mutation_probability: float, number_generations: int = None):
        """
        Initialize the Genetic Algorithm with population size and mutation probability.

        Parameters:
        - population_size (int): The size of the population.
        - mutation_probability (float): The probability of mutation for each individual.
        """
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.number_generations = number_generations
        self.cities_locations = [
            (
                random.randint(self.NODE_RADIUS + self.PLOT_X_OFFSET, self.WIDTH - self.NODE_RADIUS),
                random.randint(self.NODE_RADIUS, self.HEIGHT - self.NODE_RADIUS)
            )
            for _ in range(self.N_CITIES)
        ]
        self.initialize_pygame_display()

    def generate_initial_population(self) -> List[List[Tuple[float, float]]]:
        """
        Generate a random population of routes for a given set of cities.

        Returns:
        List[List[Tuple[float, float]]]: A list of routes, where each route is represented as a list of city locations.
        """
        return [
            random.sample(self.cities_locations, len(self.cities_locations))
            for _ in range(self.population_size)
        ]

    def calculate_distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """
        Calculate the Euclidean distance between two points.

        Parameters:
        - point1 (Tuple[float, float]): The coordinates of the first point.
        - point2 (Tuple[float, float]): The coordinates of the second point.

        Returns:
        float: The Euclidean distance between the two points.
        Nota: existe uma maneiroa melhor: Matriz de Distância
        """
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def calculate_fitness(self, path: List[Tuple[float, float]]) -> float:
        """
        Calculate the fitness of a given path based on the total Euclidean distance.

        Parameters:
        - path (List[Tuple[float, float]]): A list of tuples representing the path,
        where each tuple contains the coordinates of a point.

        Returns:
        float: The total Euclidean distance of the path.
        """
        distance = 0
        n = len(path)
        for i in range(n):
            distance += self.calculate_distance(path[i], path[(i + 1) % n])

        return distance

    def sort_population(self, population: List[List[Tuple[float, float]]], fitness: List[float]) -> Tuple[
        List[List[Tuple[float, float]]], List[float]]:
        """
        Sort a population based on fitness values.

        Parameters:
        - population (List[List[Tuple[float, float]]]): The population of solutions, where each solution is represented as a list.
        - fitness (List[float]): The corresponding fitness values for each solution in the population.

        Returns:
        Tuple[List[List[Tuple[float, float]]], List[float]]: A tuple containing the sorted population and corresponding sorted fitness values.
        """
        # Combine lists into pairs
        combined_lists = list(zip(population, fitness))

        # Sort based on the values of the fitness list
        sorted_combined_lists = sorted(combined_lists, key=lambda x: x[1])

        # Separate the sorted pairs back into individual lists
        sorted_population, sorted_fitness = zip(*sorted_combined_lists)

        return sorted_population, sorted_fitness

    def crossover(self, parent1: List[Tuple[float, float]], parent2: List[Tuple[float, float]]) -> List[
        Tuple[float, float]]:
        """
        Perform order crossover (OX) between two parent sequences to create a child sequence.

        Parameters:
        - parent1 (List[Tuple[float, float]]): The first parent sequence.
        - parent2 (List[Tuple[float, float]]): The second parent sequence.

        Returns:
        List[Tuple[float, float]]: The child sequence resulting from the order crossover.
        """
        length = len(parent1)

        # Choose two random indices for the crossover
        start_index = random.randint(0, length - 1)
        end_index = random.randint(start_index + 1, length)

        # Initialize the child with a copy of the substring from parent1
        child = parent1[start_index:end_index]

        # Fill in the remaining positions with genes from parent2
        remaining_positions = [i for i in range(length) if i < start_index or i >= end_index]
        remaining_genes = [gene for gene in parent2 if gene not in child]

        for position, gene in zip(remaining_positions, remaining_genes):
            child.insert(position, gene)

        return child

    def mutate(self, solution: List[Tuple[float, float]], mutation_probability: float) -> List[Tuple[float, float]]:
        """
        Mutate a solution by inverting a segment of the sequence with a given mutation probability.

        Parameters:
        - solution (List[int]): The solution sequence to be mutated.
        - mutation_probability (float): The probability of mutation for each individual in the solution.

        Returns:
        List[int]: The mutated solution sequence.
        """
        mutated_solution = copy.deepcopy(solution)

        # Check if mutation should occur
        if random.random() < mutation_probability:

            # Ensure there are at least two cities to perform a swap
            if len(solution) < 2:
                return solution

            # Select a random index (excluding the last index) for swapping
            index = random.randint(0, len(solution) - 2)

            # Swap the cities at the selected index and the next index
            mutated_solution[index], mutated_solution[index + 1] = solution[index + 1], solution[index]

        return mutated_solution

    def run(self):
        """
        Run the Genetic Algorithm to evolve the population over a number of generations.
        This method will implement the steps of selection, crossover, mutation, and fitness evaluation.
        """
        best_fitness_values = []
        best_solutions = []

        # Gera População Inicial
        population = self.generate_initial_population()

        # Loop principal do algoritmo genético
        generation_counter = itertools.count(start=1)
        running = True
        while running:
            running = self.update_pygame_running(running)
            generation = next(generation_counter)

            # Avalia Aptidão dos Individuos
            population_fitness = [self.calculate_fitness(individual) for individual in population]
            population, population_fitness = self.sort_population(population, population_fitness)
            best_fitness = self.calculate_fitness(population[0])
            best_solution = population[0]
            best_fitness_values.append(best_fitness)
            best_solutions.append(best_solution)
            print(f"Generation {generation}: Best fitness = {round(best_fitness, 2)}")
            self.update_pygame_display(best_fitness_values, best_solution, population)

            # Seleção da Nova População
            new_population = [population[0]]  # Keep the best individual: ELITISMO
            while len(new_population) < self.population_size: # Gerar individuos ate ter o tamanho da população.
                probability = 1 / np.array(population_fitness)
                parent1, parent2 = random.choices(population, weights=probability, k=2)
                child1 = self.crossover(parent1, parent1)  # Cruzamento
                child1 = self.mutate(child1, self.mutation_probability)  # Mutação
                new_population.append(child1)

            # Substitui a população atual pela nova população
            population = new_population

            self.flip_pygame_display()

        self.close_pygame_display()
