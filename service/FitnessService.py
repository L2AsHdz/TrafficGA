from model.enum.EdgeType import EdgeType
from model.enum.Status import Status


class FitnessService:

    def calculate_fitness(self, individual):
        initial_edges = list(filter(lambda e: e.get_edge_type() == EdgeType.INPUT, individual.get_edges()))
        nodes_index_to_operate = list(map(lambda e: e.get_input_node(), initial_edges))
        nodes_to_operate = [node for node in individual.get_chromosome() if node.get_number() in nodes_index_to_operate]

        while len(nodes_to_operate) > 0:
            # Obtener primer nodo de la lista
            node = nodes_to_operate.pop(0)

            # Operar si todas las aristas de entrada ya han sido operadas
            incoming_indexes = list(map(lambda e: e, node.get_incoming_edges()))
            incoming_edges = [edge for edge in individual.get_edges() if edge.get_number() in incoming_indexes]
            if all(e.get_status() == Status.OPERATED for e in incoming_edges):
                # Calcular cantidad de flujo entrante
                incoming_total = sum(map(lambda e: e.get_outgoing_quantity(), incoming_edges))

                # Recorrer aristas de salida
                outgoing_indexes = list(map(lambda e: e, node.get_outgoing_edges()))
                outgoing_edges = [edge for edge in individual.get_edges() if edge.get_number() in outgoing_indexes]
                for index, edge in enumerate(outgoing_edges):
                    # Calcular cantidad de flujo saliente
                    outgoing_quantity = int(incoming_total * node.get_gene().get_percents()[index])

                    # Actualizarcantidad de flujo saliente tomando en cuenta la capacidad máxima de la arista
                    edge.set_outgoing_quantity(outgoing_quantity if outgoing_quantity <= edge.get_max_capacity()
                                               else edge.get_max_capacity())

                    # Marcar arista como operada
                    edge.set_status(Status.OPERATED)

                    if edge.get_input_node():
                        if not any(n.get_number() == edge.get_input_node() for n in nodes_to_operate):
                            result = list(filter(lambda n: n.get_number() == edge.get_input_node(),
                                                 individual.get_chromosome()))
                            nodes_to_operate.append(result[0])

                print("Nodo " + str(node.get_number()) + " operado")
            # Si no, agregar nodo al final de la lista
            else:
                nodes_to_operate.append(node)

        incoming_total = sum(map(lambda e: e.get_outgoing_quantity(), initial_edges))

        final_edges = list(filter(lambda e: e.get_edge_type() == EdgeType.OUTPUT, individual.get_edges()))
        outgoing_total = sum(map(lambda e: e.get_outgoing_quantity(), final_edges))
        fitness = round((outgoing_total / incoming_total * 100), 2) if incoming_total > 0 else 0

        return incoming_total, outgoing_total, fitness
