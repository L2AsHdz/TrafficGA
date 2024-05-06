import random

from model.Gene import Gene


class Individual:

    __incoming_total = 0
    __outgoing_total = 0
    __aptitude = 0

    def __init__(self, chromosome, edges):
        self.__chromosome = [node.copy() for node in chromosome]
        self.__edges = [edge.copy() for edge in edges]

    def get_chromosome(self):
        return self.__chromosome

    def get_edges(self):
        return self.__edges

    def get_incoming_total(self):
        return self.__incoming_total

    def get_outgoing_total(self):
        return self.__outgoing_total

    def get_aptitude(self):
        return round((self.__aptitude / 100), 2)

    def generate_genes(self):
        for node in self.__chromosome:
            outgoing_indexes = list(map(lambda e: e, node.get_outgoing_edges()))
            outgoing_edges = [edge for edge in self.__edges if edge.get_number() in outgoing_indexes]
            minimum_total = sum(e.get_min_capacity() for e in outgoing_edges)
            remaining_percent = 100 - minimum_total
            percents = []

            for edge in outgoing_edges:
                max_percent = min(100, edge.get_min_capacity() + remaining_percent)
                generated_percent = random.randint(edge.get_min_capacity(), max_percent)
                percents.append(generated_percent)
                remaining_percent -= generated_percent - edge.get_min_capacity()

            if remaining_percent > 0:
                random_index = random.randint(0, len(percents) - 1)
                percents[random_index] += remaining_percent

            percents = list((map(lambda p: round((p / 100), 2), percents)))
            node.set_gene(Gene(percents))

    def set_chromosome(self, nodes):
        self.__chromosome = nodes

    def set_edges(self, edges):
        self.__edges = edges

    def set_incoming_total(self, incoming_total):
        self.__incoming_total = incoming_total

    def set_outgoing_total(self, outgoing_total):
        self.__outgoing_total = outgoing_total

    def set_aptitude(self, aptitude):
        self.__aptitude = aptitude

    def __str__(self):
        string = ""

        for node in self.__chromosome:
            string += " " + str(node)
        return string

    def to_string(self):
        string = ""

        for node in self.__chromosome:
            string += " " + str(node.to_string())
        return string

    def copy(self):
        new_individual = Individual(self.__chromosome, self.__edges)
        new_individual.set_incoming_total(self.__incoming_total)
        new_individual.set_outgoing_total(self.__outgoing_total)
        new_individual.set_aptitude(self.__aptitude)
        return new_individual
