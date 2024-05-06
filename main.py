import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

from controller.PrincipalController import PrincipalController
from model.Configuration import Configuration
from model.Node import Node
from model.Edge import Edge
from model.Gene import Gene
from model.enum.EdgeType import EdgeType
from model.enum.Status import Status
from service.GeneticAlgorithmService import GeneticAlgorithmService
from view.PrincipalView import PrincipalView


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Traffic Genetic Algorithm')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        # create a model
        model = Configuration()

        # create a view and place it on the root window
        view = PrincipalView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = PrincipalController(model, view)

        # set the controller to view
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()




# Creacion de nodos y aristas
edges = []
nodes = []

# Aristas de entrada
input1 = Edge(1, None, None,
              None, 250, EdgeType.INPUT)
input1.set_status(Status.OPERATED)

input2 = Edge(2, None, None,
              None, 150, EdgeType.INPUT)
input2.set_status(Status.OPERATED)

# Nodos y aristas intermedias
node1 = Node(1, Gene([1]), [], [])
node2 = Node(2, Gene([0.6, 0.4]), [], [])
node1.get_incoming_edges().append(input1.get_number())
node2.get_incoming_edges().append(input2.get_number())

input1.set_input_node(node1.get_number())
input2.set_input_node(node2.get_number())

edge_node_1_node_3 = Edge(3, None, 175, 50,
                          None, EdgeType.INTERMEDIATE)

node3 = Node(3, Gene([1]), [], [])
edge_node_1_node_3.set_input_node(node3.get_number())
node1.get_outgoing_edges().append(edge_node_1_node_3.get_number())
node3.get_incoming_edges().append(edge_node_1_node_3.get_number())

edge_node_2_node_3 = Edge(4, node3.get_number(), 100, 25,
                          None, EdgeType.INTERMEDIATE)
node2.get_outgoing_edges().append(edge_node_2_node_3.get_number())
node3.get_incoming_edges().append(edge_node_2_node_3.get_number())

edge_node_2_node_4 = Edge(5, None, 50, 10,
                          None, EdgeType.INTERMEDIATE)

node4 = Node(4, Gene([0.2, 0.8]), [], [])
node2.get_outgoing_edges().append(edge_node_2_node_4.get_number())
node4.get_incoming_edges().append(edge_node_2_node_4.get_number())

edge_node_2_node_4.set_input_node(node4.get_number())

edge_node_4_node_3 = Edge(6, node3.get_number(), 50, 10,
                          None, EdgeType.INTERMEDIATE)

node4.get_outgoing_edges().append(edge_node_4_node_3.get_number())
node3.get_incoming_edges().append(edge_node_4_node_3.get_number())

# Aristas de salida
output1 = Edge(7, None, 85,
               30, None, EdgeType.OUTPUT)
node3.get_outgoing_edges().append(output1.get_number())

output2 = Edge(8, None, 100,
               30, None, EdgeType.OUTPUT)
node4.get_outgoing_edges().append(output2.get_number())

nodes.append(node1)
nodes.append(node2)
nodes.append(node3)
nodes.append(node4)
edges.append(input1)
edges.append(input2)
edges.append(edge_node_1_node_3)
edges.append(edge_node_2_node_3)
edges.append(edge_node_2_node_4)
edges.append(edge_node_4_node_3)
edges.append(output1)
edges.append(output2)

# Parametros iniciales
population_size = 100
no_mutations = 5
mutated_generations = 10
limit_generations = 200
minimum_aptitude = 0.35

config = Configuration()
config.set_population_size(population_size)
config.set_no_mutations(no_mutations)
config.set_mutated_generations(mutated_generations)
config.set_limit_generations(limit_generations)
config.set_minimum_aptitude(minimum_aptitude)
config.set_chromosome(nodes)
config.set_edges(edges)
config.set_tournament_size(4)
config.set_mask("XYXY")
config.set_mask_2("YYXX")
config.set_selection_type("Ranking")
config.set_crossover_type("DoubleMask")

for node in nodes:
    print(node.to_string())

for edge in edges:
    print(edge)

# ag_service = GeneticAlgorithmService(config, None)
# ag_service.start()