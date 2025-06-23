
import random
import copy 

def mutate(solution, mutation_probability):
    # Eh feita uma copia do individuo...
    # Sorteamos se a mutação pode ou não acontecer
    # Quando acontece, nos invertemos aleatoriamente 
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
        
        
# Example usage:
original_solution =[(99, 100), (2, 50), (1, 71), (3, 80), (8, 120)]
mutation_probability = 1

mutated_solution = mutate(original_solution, mutation_probability)
print("Original Solution:", original_solution)
print("Mutated Solution:", mutated_solution)