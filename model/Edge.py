from model.enum.Status import Status


class Edge:

    __status = Status.PENDING

    def __init__(self, number, input_node, max_capacity, min_capacity, outgoing_quantity, edge_type):
        self.__number = number
        self.__input_node = input_node
        self.__max_capacity = max_capacity
        self.__min_capacity = min_capacity
        self.__outgoing_quantity = outgoing_quantity
        self.__edge_type = edge_type

    def get_number(self):
        return self.__number

    def get_input_node(self):
        return self.__input_node

    def get_max_capacity(self):
        return self.__max_capacity

    def get_min_capacity(self):
        return self.__min_capacity

    def get_outgoing_quantity(self):
        return self.__outgoing_quantity

    def get_edge_type(self):
        return self.__edge_type

    def get_status(self):
        return self.__status

    def set_number(self, number):
        self.__number = number

    def set_input_node(self, input_node):
        self.__input_node = input_node

    def set_max_capacity(self, max_capacity):
        self.__max_capacity = max_capacity

    def set_min_capacity(self, min_capacity):
        self.__min_capacity = min_capacity

    def set_outgoing_quantity(self, outgoing_quantity):
        self.__outgoing_quantity = outgoing_quantity

    def set_edge_type(self, edge_type):
        self.__edge_type = edge_type

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return ("Edge: { Input Node: " + str(self.__input_node) +
                ", Max Capacity: " + str(self.__max_capacity) + ", Min Capacity: " + str(self.__min_capacity) +
                ", Outgoing Quantity: " + str(self.__outgoing_quantity) + ", Edge Type: " +
                str(self.__edge_type) + " }")

    def copy(self):
        new_edge = Edge(self.__number, self.__input_node, self.__max_capacity, self.__min_capacity,
                        self.__outgoing_quantity, self.__edge_type)
        new_edge.set_status(self.__status)
        return new_edge
