import random

from service.FitnessService import FitnessService
from service.crossover.CrossoverServiceBase import CrossoverServiceBase


class RandomCrossoverServiceOr(CrossoverServiceBase):

    def __init__(self, parents):
        self.__parents = parents

    def cross_parents(self):
        children = []
        fitness_service = FitnessService()
        for index in range(0, len(self.__parents), 2):
            parent1 = self.__parents[index]
            parent2 = self.__parents[index + 1]

            child1 = self.__create_child(parent1, parent2)
            child2 = self.__create_child(parent2, parent1)

            self.recalculate_fitness(child1, fitness_service)
            self.recalculate_fitness(child2, fitness_service)

            children.append(child1)
            children.append(child2)

        return children

    def __create_child(self, parent1, parent2):
        chromosome1 = parent1.get_chromosome()
        chromosome2 = parent2.get_chromosome()

        child_chromosome = [random.choice([chromosome1[i], chromosome2[i]]) for i in range(len(chromosome1))]

        child = parent1.copy()
        child.set_chromosome(child_chromosome)

        return child
