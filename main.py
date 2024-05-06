import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from model.Node import Node
from model.Edge import Edge
from model.Gene import Gene
from model.enum.EdgeType import EdgeType
from model.enum.Status import Status
from service.InitialPopulationService import InitialPopulationService
from service.ScrambleMutationService import ScrambleMutationService
from service.crossover.MultiPointCrossoverService import MultiPointCrossoverService
from service.crossover.SinglePointCrossoverService import SinglePointCrossoverService
from service.selection.RankingSelectionService import RankingSelectionService

edges = []
nodes = []

# Aristas de entrada
input1 = Edge(1, None, None,
              None, 250, EdgeType.INPUT)
input1.set_status(Status.OPERATED)

input2 = Edge(2, None, None,
              None, 150, EdgeType.INPUT)
input2.set_status(Status.OPERATED)

#Nodos y aristas intermedias
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
population_size = 200
no_mutations = 30
mutated_generations = 40
limit_generations = 1000
minimum_aptitude = 0.35

current_generation = 1
best_individual = None
worst_individual = None

# Generar poblacion inicial
population_service = InitialPopulationService(population_size, nodes, edges)
population = population_service.generate_population()

for index, individual in enumerate(population):
    print("Individuo " + str(index + 1))
    print(individual)
    print("")

# Iterar hasta cumplir alguna condicion de salida

while current_generation < limit_generations:
    if best_individual and best_individual.get_aptitude() >= minimum_aptitude:
        break

    print("Generacion " + str(current_generation))

    # Seleccionar padres
    selection_service = RankingSelectionService(population, population_size)
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
    mutation_service = ScrambleMutationService(children, no_mutations)
    mutated_population = mutation_service.mutate_population()

    for index, individual in enumerate(mutated_population):
        print("Mutado " + str(index + 1))
        print(individual)
        print("")

    # get best and worst individual
    best_individual = max(mutated_population, key=lambda x: x.get_aptitude())
    worst_individual = min(mutated_population, key=lambda x: x.get_aptitude())
    current_generation += 1

print("Generacion " + str(current_generation))
print("")

print("Mejor individuo")
print(best_individual)
print("")

print("Peor individuo")
print(worst_individual)
print("")

# G = nx.DiGraph()
# for node in nodes:
#     G.add_node(node.get_number())
#
#
# for edge in edges:
#     if edge.get_input_node() and edge.get_output_node():
#         G.add_edge(edge.get_output_node().get_number(), edge.get_input_node().get_number(), weight=edge.get_max_capacity())
#     elif edge.get_input_node():
#         G.add_edge('In ' + str(edge.get_input_node().get_number()), edge.get_input_node().get_number(), weight=edge.get_outgoing_quantity())
#     elif edge.get_output_node():
#         G.add_edge(edge.get_output_node().get_number(), 'Out ' + str(edge.get_output_node().get_number()), weight=edge.get_max_capacity())
#
# pos = nx.spring_layout(G)
#
# nx.draw_networkx_nodes(G, pos, node_size=600)
# nx.draw_networkx_edges(G, pos, arrowsize=20, width=2)
# nx.draw_networkx_labels(G, pos)
#
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# window = Tk()
#
# window.title = "Grafo de trafico"
# window.geometry("500x500")
#
#
# plot_button = Button(master = window,
#                      height = 2,
#                      width = 10,
#                     text = "Plot")
#
# plot_button.pack()
#
# window.mainloop()

# plt.show()
