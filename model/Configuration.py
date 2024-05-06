class Configuration:

    # def __init__(self, population_size, no_mutations, mutated_generations, limit_generations,
    #              minimum_aptitude, chromosome, edges):
    #     self.__population_size = population_size
    #     self.__no_mutations = no_mutations
    #     self.__mutated_generations = mutated_generations
    #     self.__limit_generations = limit_generations
    #     self.__minimum_aptitude = minimum_aptitude
    #     self.__chromosome = [node.copy() for node in chromosome]
    #     self.__edges = [edge.copy() for edge in edges]

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

    def __str__(self):
        return "Population Size: " + str(self.__population_size) + "\n" + \
               "No Mutations: " + str(self.__no_mutations) + "\n" + \
               "Mutated Generations: " + str(self.__mutated_generations) + "\n" + \
               "Limit Generations: " + str(self.__limit_generations) + "\n" + \
               "Minimum Aptitude: " + str(self.__minimum_aptitude)

