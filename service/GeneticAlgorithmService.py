from service.InitialPopulationService import InitialPopulationService
from service.ScrambleMutationService import ScrambleMutationService
from service.crossover.ComplementaryMaskCrossoverService import ComplementaryOrMaskCrossoverService
from service.crossover.DoubleMaskCrossoverService import DoubleOrMaskCrossoverService
from service.crossover.MultiPointCrossoverService import MultiPointCrossoverService
from service.crossover.RandomCrossoverService import RandomCrossoverServiceOr
from service.crossover.SinglePointCrossoverService import SinglePointCrossoverService
from service.selection.RankingSelectionService import RankingSelectionService
from service.selection.RouletteSelectionService import RouletteSelectionService
from service.selection.TournamentSelectionService import TournamentSelectionService


class GeneticAlgorithmService:

    __current_generation = 0
    __best_individual = None
    __worst_individual = None

    def __init__(self, configuration, view):
        self.__view = view
        self.__population_size = configuration.get_population_size()
        self.__no_mutations = configuration.get_no_mutations()
        self.__mutated_generations = configuration.get_mutated_generations()
        self.__limit_generations = configuration.get_limit_generations()
        self.__minimum_aptitude = configuration.get_minimum_aptitude()
        self.__chromosome = [node.copy() for node in configuration.get_chromosome()]
        self.__edges = [edge.copy() for edge in configuration.get_edges()]
        self.__tournament_size = configuration.get_tournament_size()
        self.__mask = configuration.get_mask()
        self.__mask_2 = configuration.get_mask_2()
        self.__selection_type = configuration.get_selection_type()
        self.__crossover_type = configuration.get_crossover_type()

    def start(self):
        # Generar poblacion inicial
        population_service = InitialPopulationService(self.__population_size, self.__chromosome, self.__edges)
        population = population_service.generate_population()

        for index, individual in enumerate(population):
            print("Individuo " + str(index + 1))
            print(individual.to_string())

        # Iterar hasta cumplir alguna condicion de salida
        while self.__current_generation <= self.__limit_generations:
            if self.__best_individual and self.__best_individual.get_aptitude() > self.__minimum_aptitude:
                break

            # Seleccionar padres
            selection_service = None
            if self.__selection_type == "Ranking":
                selection_service = RankingSelectionService(population, self.__population_size)
            elif self.__selection_type == "Tournament":
                selection_service = TournamentSelectionService(population, self.__population_size,
                                                               self.__tournament_size)
            elif self.__selection_type == "Roulette":
                selection_service = RouletteSelectionService(population, self.__population_size)
            else:
                selection_service = RankingSelectionService(population, self.__population_size)

            parents = selection_service.select_parents()

            # for index, individual in enumerate(population):
            #     print("Padre " + str(index + 1))
            #     print(individual.to_string())

            # Cruce
            crossover_service = None
            if self.__crossover_type == "SinglePoint":
                crossover_service = SinglePointCrossoverService(parents)
            elif self.__crossover_type == "MultiPoint":
                crossover_service = MultiPointCrossoverService(parents)
            elif self.__crossover_type == "Random":
                crossover_service = RandomCrossoverServiceOr(parents)
            elif self.__crossover_type == "ComplementaryMask":
                crossover_service = ComplementaryOrMaskCrossoverService(parents, self.__mask)
            elif self.__crossover_type == "DoubleMask":
                crossover_service = DoubleOrMaskCrossoverService(parents, self.__mask, self.__mask_2)
            else:
                crossover_service = SinglePointCrossoverService(parents)
            children = crossover_service.cross_parents()

            # for index, individual in enumerate(children):
            #     print("Hijo " + str(index + 1))
            #     print(individual.to_string())

            # Mutacion
            mutation_service = ScrambleMutationService(children, self.__no_mutations)
            mutated_population = mutation_service.mutate_population()

            # for index, individual in enumerate(mutated_population):
            #     print("Mutado " + str(index + 1))
            #     print(individual.to_string())

            # get best and worst individual
            self.__best_individual = max(mutated_population, key=lambda x: x.get_aptitude())
            self.__worst_individual = min(mutated_population, key=lambda x: x.get_aptitude())

            if self.__view:
                # self.__view.after(0, lambda: self.__view.add_row(self.__current_generation,
                #                                                  self.__best_individual.get_aptitude(),
                #                                                  str(self.__best_individual)))
                self.__view.add_row(self.__current_generation,
                                    self.__best_individual.get_aptitude(),
                                    str(self.__best_individual))

            print("Generacion " + str(self.__current_generation))

            print(str(self.__best_individual) + " - " + str(self.__best_individual.get_aptitude()))

            self.__current_generation += 1

