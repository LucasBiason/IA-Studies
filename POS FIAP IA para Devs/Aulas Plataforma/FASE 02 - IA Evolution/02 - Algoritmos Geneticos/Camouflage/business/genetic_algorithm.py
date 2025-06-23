import random
import itertools
import numpy as np

from .pygamega_base import PyGameGA


class GeneticAlgorithm(PyGameGA):
        
    def __init__(self, population_size, mutation_probability, number_generations, target_color):
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        #self.mutation_intensity = mutation_intensity
        self.number_generations = number_generations
        self.target_color = target_color
        self.initialize_pygame_display()

    def generate_initial_population(self):
        return [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(self.population_size)
        ]
            
    # Function to calculate the fitness of an individual color
    def calculate_fitness(self, color):
        # Fitness is the sum of the absolute differences from the target color
        return sum(abs(color[i] - self.target_color[i]) for i in range(3))
    
    # Perform one-point crossover
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    # Perform mutation by changing colors with a specified intensity
    def mutate(self, color, sigma=1):
        mutated_color = list(color)
        for i in range(3):
            if random.random() < self.mutation_probability:
                # mutated_color[i] = int(color[i] * (1 + (random.choice([-1, 1])) * mutation_intensity)) ## percentage mutation
                mutated_color[i] += round(np.random.normal(0, sigma)) # Gaussian mutation
        return tuple(mutated_color)

    def run(self):
        # Gera População Inicial
        population = self.generate_initial_population()
        
        # Lists to store best fitness and generation for plotting
        best_fitness_values = []
        best_colors = []
        
        # Loop principal do algoritmo genético
        generation_counter = itertools.count(start=1)
        running = True
        while running:
            running = self.update_pygame_running(running)
            generation = next(generation_counter)
                    
            self.screen.fill(self.target_color)
            population = sorted(population, key=self.calculate_fitness)
        
            # Avalia Aptidão dos Individuos
            best_fitness = self.calculate_fitness(population[0])
            best_color = population[0]
            best_fitness_values.append(best_fitness)
            best_colors.append(best_color)
            print(f"Generation {generation}: Best fitness = {best_fitness}, Best color = {best_color}, Target = {self.target_color}")
        
            # Seleção da Nova População
            new_population = [population[0]]  # Keep the best individual: ELITISMO
            while len(new_population) < self.population_size: # Gerar individuos ate ter o tamanho da população.
                parent1, parent2 = random.choices(population[:10], k=2)  # Select parents from the top 10 individuals
                child1, child2 = self.crossover(parent1, parent2) # Cruzamento
                child1 = self.mutate(child1)  # Mutação
                child2 = self.mutate(child2)  # Mutação
                new_population.extend([child1, child2])
                
            # Substitui a população atual pela nova população
            population = new_population
                    
            self.draw_plot(list(range(len(best_fitness_values))), best_fitness_values)
            self.draw_squares(population)
            self.draw_text(
                f'Best Solution: {best_color}', 
                450, 
                self.window_size[1]-50, 
                font_size=15, 
                font='Courier New'
            )
            self.draw_text(
                f'Target       : {tuple(self.target_color)}', 
                450, 
                self.window_size[1]-50+15, 
                font_size=15, 
                font='Courier New'
            )
            
            self.flip_pygame_display()
        
        self.close_pygame_display()
        # Print the best color found
        best_color = population[0]
        print(f"Best Color: {best_color}")
        
