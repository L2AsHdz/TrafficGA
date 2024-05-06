import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from model.Node import Node
from model.Edge import Edge
from model.enum.EdgeType import EdgeType
from model.enum.Status import Status

edges = []
nodes = []

# Aristas de entrada
input1 = Edge(None, None, None,
              None, 250, EdgeType.INPUT)
input1.set_status(Status.OPERATED)

input2 = Edge(None, None, None,
              None, 150, EdgeType.INPUT)
input2.set_status(Status.OPERATED)

#Nodos y aristas intermedias
node1 = Node(1, [1], [], [])
node2 = Node(2, [0.6, 0.4], [], [])
node1.get_incoming_edges().append(input1)
node2.get_incoming_edges().append(input2)

input1.set_input_node(node1)
input2.set_input_node(node2)

edge_node_1_node_3 = Edge(node1, None, 175, 50,
                          None, EdgeType.INTERMEDIATE)

node3 = Node(3, [1], [], [])
edge_node_1_node_3.set_input_node(node3)
node1.get_outgoing_edges().append(edge_node_1_node_3)
node3.get_incoming_edges().append(edge_node_1_node_3)

edge_node_2_node_3 = Edge(node2, node3, 100, 25,
                          None, EdgeType.INTERMEDIATE)
node2.get_outgoing_edges().append(edge_node_2_node_3)
node3.get_incoming_edges().append(edge_node_2_node_3)

edge_node_2_node_4 = Edge(node2, None, 50, 10,
                          None, EdgeType.INTERMEDIATE)

node4 = Node(4, [0.2, 0.8], [], [])
node2.get_outgoing_edges().append(edge_node_2_node_4)
node4.get_incoming_edges().append(edge_node_2_node_4)

edge_node_2_node_4.set_input_node(node4)

edge_node_4_node_3 = Edge(node4, node3, 50, 10,
                          None, EdgeType.INTERMEDIATE)

node4.get_outgoing_edges().append(edge_node_4_node_3)
node3.get_incoming_edges().append(edge_node_4_node_3)

# Aristas de salida
output1 = Edge(node3, None, 40,
               None, None, EdgeType.OUTPUT)
node3.get_outgoing_edges().append(output1)

output2 = Edge(node4, None, 50,
               None, None, EdgeType.OUTPUT)
node4.get_outgoing_edges().append(output2)

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

initial_edges = list(filter(lambda e: e.get_edge_type() == EdgeType.INPUT, edges))
nodes_to_operate = list(map(lambda e: e.get_input_node(), initial_edges))

while len(nodes_to_operate) > 0:
    # Obtener primer nodo de la lista
    node = nodes_to_operate.pop(0)

    # Operar si todas las aristas de entrada ya han sido operadas
    if all(e.get_status() == Status.OPERATED for e in node.get_incoming_edges()):
        # Calcular cantidad de flujo entrante
        incoming_total = sum(map(lambda e: e.get_outgoing_quantity(), node.get_incoming_edges()))

        # Recorrer aristas de salida
        for index, edge in enumerate(node.get_outgoing_edges()):
            # Calcular cantidad de flujo saliente
            outgoing_quantity = int(incoming_total * node.get_percentajes()[index])

            # Actualizarcantidad de flujo saliente tomando en cuenta la capacidad máxima de la arista
            edge.set_outgoing_quantity(outgoing_quantity if outgoing_quantity <= edge.get_max_capacity()
                                       else edge.get_max_capacity())

            # Marcar arista como operada
            edge.set_status(Status.OPERATED)

            if edge.get_input_node():
                if not any(n.get_number() == edge.get_input_node().get_number() for n in nodes_to_operate):
                    nodes_to_operate.append(edge.get_input_node())

        print("Nodo " + str(node.get_number()) + " operado")
    # Si no, agregar nodo al final de la lista
    else:
        nodes_to_operate.append(node)

incoming_total = sum(map(lambda e: e.get_outgoing_quantity(), initial_edges))

final_edges = list(filter(lambda e: e.get_edge_type() == EdgeType.OUTPUT, edges))
outgoing_total = sum(map(lambda e: e.get_outgoing_quantity(), final_edges))

print("Flujo total de entrada: " + str(incoming_total))
print("Flujo total de salida: " + str(outgoing_total))
print("Diferencia: " + str(incoming_total - outgoing_total))
print("Porcentaje de eficiencia: " + str(outgoing_total / incoming_total * 100) + "%" if incoming_total > 0 else "0%")



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
