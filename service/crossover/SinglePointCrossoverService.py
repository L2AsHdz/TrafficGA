import random
from service.FitnessService import FitnessService


class SinglePointCrossoverService:

    def __init__(self, parents):
        self.__parents = parents

    def cross_parents(self):
        children = []
        fitness_service = FitnessService()
        for index in range(0, len(self.__parents), 2):
            parent1 = self.__parents[index]
            parent2 = self.__parents[index + 1]

            crossover_point = random.randint(1, len(parent1.get_chromosome()) - 1)

            child1 = self.__create_child(parent1, parent2, crossover_point)
            child2 = self.__create_child(parent2, parent1, crossover_point)

            self.__recalculate_fitness(child1, fitness_service)
            self.__recalculate_fitness(child2, fitness_service)

            children.append(child1)
            children.append(child2)

        return children

    def __create_child(self, parent1, parent2, crossover_point):
        chromosome1 = parent1.get_chromosome()
        chromosome2 = parent2.get_chromosome()

        child_chromosome = chromosome1[:crossover_point] + chromosome2[crossover_point:]

        child = parent1.copy()
        child.set_chromosome(child_chromosome)

        return child

    def __recalculate_fitness(self, child, fitness_service):
        in_total, out_total, fitness = fitness_service.calculate_fitness(child)
        child.set_incoming_total(in_total)
        child.set_outgoing_total(out_total)
        child.set_aptitude(fitness)
