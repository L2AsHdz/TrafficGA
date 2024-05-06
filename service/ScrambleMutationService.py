import random


class ScrambleMutationService:

    def __init__(self, population, no_mutations):
        self.__population = population
        self.__no_mutations = no_mutations

    def mutate_population(self):

        indexes = random.sample(range(0, len(self.__population) - 1), self.__no_mutations)

        for index in indexes:
            individual = self.__population[index]
            individual.generate_genes()
            print("Individuo " + str(index + 1) + " mutado")

        return self.__population
