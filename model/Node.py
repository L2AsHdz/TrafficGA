class Node:

    __x = None
    __y = None
    def __init__(self, number, gene, incoming_edges, outgoing_edges):
        self.__number = number
        self.__gene = gene
        self.__incoming_edges = incoming_edges
        self.__outgoing_edges = outgoing_edges

    def get_number(self):
        return self.__number

    def get_gene(self):
        return self.__gene

    def get_incoming_edges(self):
        return self.__incoming_edges

    def get_outgoing_edges(self):
        return self.__outgoing_edges

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_number(self, number):
        self.__number = number

    def set_gene(self, gene):
        self.__gene = gene

    def set_incoming_edges(self, incoming_edges):
        self.__incoming_edges = incoming_edges

    def set_outgoing_edges(self, outgoing_edges):
        self.__outgoing_edges = outgoing_edges

    def __str__(self):
        return "N" + str(self.__number) + ": " + str(self.__gene)

    def copy(self):
        return Node(self.__number, self.__gene.copy(), self.__incoming_edges.copy(),
                    self.__outgoing_edges.copy())
