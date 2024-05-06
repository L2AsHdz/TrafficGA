from model.Individual import Individual
from service.FitnessService import FitnessService


class InitialPopulationService:

    def __init__(self, population_size, chromosome, edges):
        self.__population_size = population_size
        self.__chromosome = [node.copy() for node in chromosome]
        self.__edges = [edge.copy() for edge in edges]

    def generate_population(self):
        fitness_service = FitnessService()

        population = []
        for i in range(self.__population_size):
            individual = Individual(self.__chromosome, self.__edges)
            individual.generate_genes()
            in_total, out_total, fitness = fitness_service.calculate_fitness(individual)
            individual.set_incoming_total(in_total)
            individual.set_outgoing_total(out_total)
            individual.set_aptitude(fitness)
            population.append(individual)
        return population
