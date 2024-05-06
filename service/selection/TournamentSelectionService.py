import random


class TournamentSelectionService:

    def __init__(self, population, num_parents, tournament_size):
        self.__population = population
        self.__num_parents = num_parents
        self.__tournament_size = tournament_size

    def select_parents(self):
        selected_parents = []

        for _ in range(self.__num_parents):
            tournament = random.sample(self.__population, self.__tournament_size)
            winner = max(tournament, key=lambda x: x.get_aptitude())
            selected_parents.append(winner)

        return selected_parents
