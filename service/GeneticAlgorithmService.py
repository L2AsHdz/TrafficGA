from service.InitialPopulationService import InitialPopulationService
from service.ScrambleMutationService import ScrambleMutationService
from service.crossover.SinglePointCrossoverService import SinglePointCrossoverService
from service.selection.RankingSelectionService import RankingSelectionService


class GeneticAlgorithmService:

    __current_generation = 1
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

    def start(self):
        # Generar poblacion inicial
        population_service = InitialPopulationService(self.__population_size, self.__chromosome, self.__edges)
        population = population_service.generate_population()

        for index, individual in enumerate(population):
            print("Individuo " + str(index + 1))
            print(individual)
            print("")

        # Iterar hasta cumplir alguna condicion de salida
        while self.__current_generation < self.__limit_generations:
            if self.__best_individual and self.__best_individual.get_aptitude() > self.__minimum_aptitude:
                break

            print("Generacion " + str(self.__current_generation))

            # Seleccionar padres
            selection_service = RankingSelectionService(population, self.__population_size)
            parents = selection_service.select_parents()

            for index, individual in enumerate(population):
                print("Padre " + str(index + 1))
                print(individual)
                print("")

            # Cruce
            crossover_service = SinglePointCrossoverService(parents)
            children = crossover_service.cross_parents()

            for index, individual in enumerate(children):
                print("Hijo " + str(index + 1))
                print(individual)
                print("")

            # Mutacion
            mutation_service = ScrambleMutationService(children, self.__no_mutations)
            mutated_population = mutation_service.mutate_population()

            for index, individual in enumerate(mutated_population):
                print("Mutado " + str(index + 1))
                print(individual)
                print("")

            # get best and worst individual
            self.__best_individual = max(mutated_population, key=lambda x: x.get_aptitude())
            self.__worst_individual = min(mutated_population, key=lambda x: x.get_aptitude())

            self.__view.add_row(self.__current_generation,
                            self.__best_individual.get_aptitude(), str(self.__best_individual))

            self.__current_generation += 1

        print("Generacion " + str(self.__current_generation))
        print("")

        print("Mejor individuo")
        print(str(self.__best_individual) + " - " + str(self.__best_individual.get_aptitude()))
        print("")

        print("Peor individuo")
        print(self.__worst_individual)
        print("")
