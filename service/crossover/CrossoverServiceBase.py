class CrossoverServiceBase:

    def cross_parents(self):
        pass

    def __create_child(self, parent1, parent2):
        pass

    def recalculate_fitness(self, child, fitness_service):
        in_total, out_total, fitness = fitness_service.calculate_fitness(child)
        child.set_incoming_total(in_total)
        child.set_outgoing_total(out_total)
        child.set_aptitude(fitness)
