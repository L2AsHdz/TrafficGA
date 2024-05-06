import random
from service.FitnessService import FitnessService
from service.crossover.CrossoverServiceBase import CrossoverServiceBase


class MultiPointCrossoverService(CrossoverServiceBase):

    def __init__(self, parents):
        self.__parents = parents

    def cross_parents(self):
        children = []
        fitness_service = FitnessService()
        for index in range(0, len(self.__parents), 2):
            parent1 = self.__parents[index]
            parent2 = self.__parents[index + 1]

            crossover_points = self.__get_crossover_points(parent1)

            child1 = self.__create_child_(parent1, parent2, crossover_points)
            child2 = self.__create_child_(parent2, parent1, crossover_points)

            self.recalculate_fitness(child1, fitness_service)
            self.recalculate_fitness(child2, fitness_service)

            children.append(child1)
            children.append(child2)

        return children

    def __get_crossover_points(self, parent):
        chromosome_length = len(parent.get_chromosome())
        crossover_points = sorted(random.sample(range(1, chromosome_length), 2))
        while crossover_points[0] == crossover_points[1]:
            crossover_points = sorted(random.sample(range(1, chromosome_length), 2))
        return crossover_points

    def __create_child_(self, parent1, parent2, crossover_points):
        chromosome1 = parent1.get_chromosome()
        chromosome2 = parent2.get_chromosome()

        child_chromosome = (chromosome1[:crossover_points[0]] + chromosome2[crossover_points[0]:crossover_points[1]]
                            + chromosome1[crossover_points[1]:])

        child = parent1.copy()
        child.set_chromosome(child_chromosome)

        return child
