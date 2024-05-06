import random


class RouletteSelectionService:

    def __init__(self, population, num_parents):
        self.__population = population
        self.__num_parents = num_parents

    def select_parents(self):
        total_aptitude = sum([x.get_aptitude() for x in self.__population])

        selection_probabilities = [x.get_aptitude() / total_aptitude for x in self.__population]

        selected_parents = random.choices(self.__population, selection_probabilities, k=self.__num_parents)

        return selected_parents