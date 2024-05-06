class Node:
    def __init__(self, number, percentajes, incoming_edges, outgoing_edges):
        self.__number = number
        self.__percentajes = percentajes
        self.__incoming_edges = incoming_edges
        self.__outgoing_edges = outgoing_edges

    def get_number(self):
        return self.__number

    def get_percentajes(self):
        return self.__percentajes

    def get_incoming_edges(self):
        return self.__incoming_edges

    def get_outgoing_edges(self):
        return self.__outgoing_edges

    def set_number(self, number):
        self.__number = number

    def set_percentsajes(self, percentajes):
        self.__percentajes = percentajes

    def set_incoming_edges(self, incoming_edges):
        self.__incoming_edges = incoming_edges

    def set_outgoing_edges(self, outgoing_edges):
        self.__outgoing_edges = outgoing_edges

    def __str__(self):
        return ("Node " + str(self.__number) + " { Percentajes: " + str(self.__percentajes) +
                ", Edges In: " + str(len(self.__incoming_edges)) +
                ", Edges Out: " + str(len(self.__outgoing_edges)) + " }")
