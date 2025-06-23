from business.genetic_algorithm import GeneticAlgorithm


if __name__ == "__main__":
    ga = GeneticAlgorithm(
        population_size=100,
        mutation_probability=0.5,
        number_generations=None,
        target_color = (100, 150, 200)
    )
    ga.run()