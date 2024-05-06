import random


class RankingSelectionService:

    def __init__(self, population, num_parents):
        self.__population = population
        self.__num_parents = num_parents

    def select_parents(self):
        sorted_population = sorted(self.__population, key=lambda x: x.get_aptitude(), reverse=True)

        total_rank = sum(range(1, len(sorted_population) + 1))

        selection_probabilities = [i / total_rank for i in range(1, len(sorted_population) + 1)]

        selected_parents = random.choices(sorted_population, selection_probabilities, k=self.__num_parents)

        return selected_parents
