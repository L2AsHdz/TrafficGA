class Configuration:

    __population_size = 0
    __no_mutations = 0
    __mutated_generations = 0
    __limit_generations = 0
    __minimum_aptitude = 0
    __chromosome = []
    __edges = []
    __crossover_type = 0
    __selection_type = 0
    __tournament_size = 0
    __mask = ""
    __mask_2 = ""

    def get_population_size(self):
        return self.__population_size

    def get_no_mutations(self):
        return self.__no_mutations

    def get_mutated_generations(self):
        return self.__mutated_generations

    def get_limit_generations(self):
        return self.__limit_generations

    def get_minimum_aptitude(self):
        return self.__minimum_aptitude

    def get_chromosome(self):
        return self.__chromosome

    def get_edges(self):
        return self.__edges

    def get_crossover_type(self):
        return self.__crossover_type

    def get_selection_type(self):
        return self.__selection_type

    def get_tournament_size(self):
        return self.__tournament_size

    def get_mask(self):
        return self.__mask

    def get_mask_2(self):
        return self.__mask_2

    def set_population_size(self, population_size):
        self.__population_size = population_size

    def set_no_mutations(self, no_mutations):
        self.__no_mutations = no_mutations

    def set_mutated_generations(self, mutated_generations):
        self.__mutated_generations = mutated_generations

    def set_limit_generations(self, limit_generations):
        self.__limit_generations = limit_generations

    def set_minimum_aptitude(self, minimum_aptitude):
        self.__minimum_aptitude = minimum_aptitude

    def set_chromosome(self, chromosome):
        self.__chromosome = chromosome

    def set_edges(self, edges):
        self.__edges = edges

    def set_crossover_type(self, crossover_type):
        self.__crossover_type = crossover_type

    def set_selection_type(self, selection_type):
        self.__selection_type = selection_type

    def set_tournament_size(self, tournament_size):
        self.__tournament_size = tournament_size

    def set_mask(self, mask):
        self.__mask = mask

    def set_mask_2(self, mask_2):
        self.__mask_2 = mask_2

    def __str__(self):
        return "Population Size: " + str(self.__population_size) + "\n" + \
               "No Mutations: " + str(self.__no_mutations) + "\n" + \
               "Mutated Generations: " + str(self.__mutated_generations) + "\n" + \
               "Limit Generations: " + str(self.__limit_generations) + "\n" + \
               "Minimum Aptitude: " + str(self.__minimum_aptitude)

