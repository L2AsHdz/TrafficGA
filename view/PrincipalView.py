import tkinter as tk
from tkinter import ttk, simpledialog
from model.Configuration import Configuration
from model.Edge import Edge
from model.Gene import Gene
from model.Node import Node
from model.enum.EdgeType import EdgeType
from model.enum.Status import Status


class PrincipalView(ttk.Frame):

    __configuration = Configuration()

    def __init__(self, parent):
        super().__init__(parent)

        self.current_node = None
        self.adding_node = False
        self.adding_input = False
        self.adding_output = False
        self.adding_edge = False
        self.count_nodes = 1
        self.count_edges = 1
        self.nodes = []
        self.edges = []

        # Population Size
        self.label = ttk.Label(self, text='Population Size:')
        self.label.grid(row=0, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.population_var = tk.IntVar(value=100)
        self.population_entry = ttk.Entry(self, textvariable=self.population_var, width=15)
        self.population_entry.grid(row=0, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # No Mutations
        self.label_1 = ttk.Label(self, text='No Mutations:')
        self.label_1.grid(row=1, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.no_mutations_var = tk.IntVar(value=5)
        self.no_mutations_entry = ttk.Entry(self, textvariable=self.no_mutations_var, width=15)
        self.no_mutations_entry.grid(row=1, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # Each Generations
        self.label_2 = ttk.Label(self, text='Each Generations:')
        self.label_2.grid(row=2, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.each_generations_var = tk.IntVar(value=10)
        self.each_generations_entry = ttk.Entry(self, textvariable=self.each_generations_var, width=15)
        self.each_generations_entry.grid(row=2, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # Limit Generations
        self.label_3 = ttk.Label(self, text='Limit Generations:')
        self.label_3.grid(row=3, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.limit_generations_var = tk.IntVar(value=400)
        self.limit_generations_entry = ttk.Entry(self, textvariable=self.limit_generations_var, width=15)
        self.limit_generations_entry.grid(row=3, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # Minimum Aptitude
        self.label_4 = ttk.Label(self, text='Minimum Aptitude:')
        self.label_4.grid(row=4, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.min_aptitude_var = tk.DoubleVar(value=0.4)
        self.min_aptitude_entry = ttk.Entry(self, textvariable=self.min_aptitude_var, width=15)
        self.min_aptitude_entry.grid(row=4, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # Selection Type
        self.label_5 = ttk.Label(self, text='Tipo Seleccion:')
        self.label_5.grid(row=5, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        options_selection = [
            "Ranking",
            "Tournament",
            "Roulette"
        ]

        self.selection_type_var = tk.StringVar()
        self.selection_type_entry = ttk.Combobox(self, textvariable=self.selection_type_var, width=15,
                                                 values=options_selection)
        self.selection_type_entry.current(0)
        self.selection_type_entry.grid(row=5, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # get_tournament_size
        self.label_6 = ttk.Label(self, text='Tournament Size:')
        self.label_6.grid(row=6, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.tournament_size_var = tk.IntVar(value=3)
        self.tournament_size_entry = ttk.Entry(self, textvariable=self.tournament_size_var, width=15)
        self.tournament_size_entry.grid(row=6, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # Crossover Type
        self.label_7 = ttk.Label(self, text='Tipo Cruce:')
        self.label_7.grid(row=7, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        options_crossover = [
            "SinglePoint",
            "MultiPoint",
            "Random",
            "ComplementaryMask",
            "DoubleMask"
        ]

        self.crossover_type_var = tk.StringVar()
        self.crossover_type_entry = ttk.Combobox(self, textvariable=self.crossover_type_var, width=15,
                                                 values=options_crossover)
        self.crossover_type_entry.current(0)
        self.crossover_type_entry.grid(row=7, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # mask 1
        self.label_8 = ttk.Label(self, text='MASK 1:')
        self.label_8.grid(row=8, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.mask_var = tk.StringVar(value="XYYX")
        self.mask_entry = ttk.Entry(self, textvariable=self.mask_var, width=15)
        self.mask_entry.grid(row=8, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        # mask 2
        self.label_9 = ttk.Label(self, text='MASK 2:')
        self.label_9.grid(row=9, column=0, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.mask_2_var = tk.StringVar(value="XYXY")
        self.mask_2_entry = ttk.Entry(self, textvariable=self.mask_2_var, width=15)
        self.mask_2_entry.grid(row=9, column=1, columnspan=1, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Add Input', command=self.enable_add_input)
        self.save_button.grid(row=1, column=3, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Add Node', command=self.enable_add_node)
        self.save_button.grid(row=1, column=4, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Add Edge', command=self.enable_add_edge)
        self.save_button.grid(row=2, column=3, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Add Output', command=self.enable_add_output)
        self.save_button.grid(row=2, column=4, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Start', command=self.save_button_clicked)
        self.save_button.grid(row=3, column=3, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.save_button = ttk.Button(self, text='Clean', command=self.limpiar_treeview)
        self.save_button.grid(row=3, column=4, columnspan=2, sticky='N,E,S,W,NE,NW,SE,SW')

        self.canvas = tk.Canvas(self, width=1000, height=600, bg='white')
        self.canvas.grid(row=10, column=0, columnspan=4, pady=15, sticky='E,S,W,NE,NW,SE,SW')

        # bold_font = ("Helvetica", 24, "bold")
        #
        # self.lbl_fitness = ttk.Label(parent, text="Fitness", font=bold_font)
        # self.lbl_fitness.grid(row=6, column=2, padx=10)

        self.tree = ttk.Treeview(self)
        self.tree['columns'] = ('column1', 'column2', 'column3')

        # Configurar las columnas
        self.tree.heading('column1', text='Generacion')
        self.tree.heading('column2', text='Eficiencia')
        self.tree.heading('column3', text='Porcentajes')

        # Ajustar el ancho de las columnas
        self.tree.column('#0', width=50)
        self.tree.column('column1', width=100)
        self.tree.column('column2', width=100)
        self.tree.column('column3', width=600)

        self.tree.grid(row=10, column=5, columnspan=6, pady=15, sticky='E,S,W,NE,NW,SE,SW')

        self.canvas.bind('<Button-1>', self.canvas_on_click)

    def add_row(self, gen, aptitude, percentages):
        self.tree.insert('', 'end', values=(gen, aptitude, percentages))

    def limpiar_treeview(self):
        self.tree.delete(*self.tree.get_children())

    def set_controller(self, controller):
        self.controller = controller

    def update_lbl_fitness(self, text):
        self.lbl_fitness.config(text=text)

    def save_button_clicked(self):
        if self.controller:
            self.__configuration.set_population_size(self.population_var.get())
            self.__configuration.set_no_mutations(self.no_mutations_var.get())
            self.__configuration.set_mutated_generations(self.each_generations_var.get())
            self.__configuration.set_limit_generations(self.limit_generations_var.get())
            self.__configuration.set_minimum_aptitude(self.min_aptitude_var.get())
            self.__configuration.set_chromosome(self.nodes)
            self.__configuration.set_edges(self.edges)
            self.__configuration.set_selection_type(self.selection_type_var.get())
            self.__configuration.set_tournament_size(self.tournament_size_var.get())
            self.__configuration.set_crossover_type(self.crossover_type_var.get())
            self.__configuration.set_mask(self.mask_var.get())
            self.__configuration.set_mask_2(self.mask_2_var.get())
            self.controller.save(self.__configuration)

    def enable_add_input(self):
        self.adding_input = True

    def enable_add_output(self):
        self.adding_output = True

    def enable_add_node(self):
        self.adding_node = True

    def enable_add_edge(self):
        self.adding_edge = True

    def canvas_on_click(self, event):
        if self.adding_node:
            x = event.x
            y = event.y
            node_id = self.add_node(x, y)
            new_node = Node(node_id, Gene([]), [], [])
            new_node.set_x(x)
            new_node.set_y(y)
            self.nodes.append(new_node)
            self.adding_node = False
            self.show_label(x, y+30, str(node_id))
        elif self.adding_input:
            x = event.x
            y = event.y
            input_count = self.ask_input_count()
            if input_count is not None:
                self.add_input_arrow(x, y, input_count)
            self.adding_input = False
        elif self.adding_output:
            x = event.x
            y = event.y
            max_capacity = self.ask_max_capacity()
            min_capacity = self.ask_min_capacity()
            if max_capacity is not None and min_capacity is not None:
                self.add_output_arrow(x, y, max_capacity, min_capacity)
            self.adding_output = False
        elif self.adding_edge:
            x = event.x
            y = event.y
            node = self.find_node__at_position(x, y)
            max_capacity = self.ask_max_capacity()
            min_capacity = self.ask_min_capacity()
            if max_capacity is not None and min_capacity is not None:
                self.add_edge(max_capacity, min_capacity, node)
            self.adding_edge = False
        else:
            node = self.find_node__at_position(event.x, event.y)
            self.highlight_node(node)

        for node in self.nodes:
            print(node.to_string())

        for edge in self.edges:
            print(edge)

        print("")

    def find_node__at_position(self, x, y):
        clicked_item = self.canvas.find_closest(x, y)
        if clicked_item:
            clicked_node_id = clicked_item[0]
            for node in self.nodes:
                if node.get_number() == clicked_node_id:
                    return node

    def add_node(self, x, y):
        radius = 20
        node_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='blue')
        return node_id

    def highlight_node(self, node):
        if self.current_node:
            self.canvas.itemconfig(self.current_node.get_number(), fill='blue')
        self.current_node = node
        self.canvas.itemconfig(node.get_number(), fill='red')

    def ask_input_count(self):
        input_count = simpledialog.askinteger("Cantidad de Entrada", "Ingrese la cantidad de entrada:")
        return input_count

    def ask_max_capacity(self):
        input_count = simpledialog.askinteger("Max Capacity", "Ingrese capacidad maxima:")
        return input_count

    def ask_min_capacity(self):
        input_count = simpledialog.askinteger("Min Capacity", "Ingrese capacidad minima:")
        return input_count

    def add_input_arrow(self, x, y, input_count):
        if self.current_node:
            start_x = self.current_node.get_x()
            start_y = self.current_node.get_y()
            arrow_id = self.canvas.create_line(start_x, start_y, x, y, arrow=tk.FIRST, fill='green', width=5)
            new_edge = Edge(arrow_id, None, None, None, input_count, EdgeType.INPUT)
            new_edge.set_status(Status.OPERATED)
            self.edges.append(new_edge)
            self.current_node.get_incoming_edges().append(arrow_id)
            new_edge.set_input_node(self.current_node.get_number())
            self.show_label(x-25, y, str(input_count))
        else:
            print("No hay un nodo seleccionado para conectar.")

    def add_output_arrow(self, x, y, max_capacity, min_capacity):
        if self.current_node:
            start_x = self.current_node.get_x()
            start_y = self.current_node.get_y()
            arrow_id = self.canvas.create_line(start_x, start_y, x, y, arrow=tk.LAST, fill='red', width=5)
            new_edge = Edge(arrow_id, None, max_capacity, min_capacity, None, EdgeType.OUTPUT)
            self.edges.append(new_edge)
            self.current_node.get_outgoing_edges().append(arrow_id)
            self.show_label(x+25, y, "MAX: " + str(max_capacity))
            self.show_label(x+25, y+25, "MIN: " + str(min_capacity)+ "%")
        else:
            print("No hay un nodo seleccionado para conectar.")

    def add_edge(self, max_capacity, min_capacity, node):
        if self.current_node:
            start_x = self.current_node.get_x()
            start_y = self.current_node.get_y()
            end_x = node.get_x()
            end_y = node.get_y()
            arrow_id = self.canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, fill='gray', width=5)
            new_edge = Edge(arrow_id, None, max_capacity, min_capacity, None,
                            EdgeType.INTERMEDIATE)
            self.edges.append(new_edge)

            self.current_node.get_outgoing_edges().append(arrow_id)
            x_medio, y_medio = self.calcular_punto_medio(start_x, start_y, end_x, end_y)
            self.show_label(x_medio, y_medio+20, "MAX: " + str(max_capacity))
            self.show_label(x_medio, y_medio+45, "MIN: " + str(min_capacity) + "%")

            node.get_incoming_edges().append(arrow_id)
            new_edge.set_input_node(node.get_number())
        else:
            print("No hay un nodo seleccionado para conectar.")

    def show_label(self, x, y, text):
        # Mostrar una etiqueta en las coordenadas (x, y)
        label_id = self.canvas.create_text(x, y, text=text, anchor=tk.W, fill='black')
        return label_id

    def add_output(self):
        print("Add output")

    def calcular_punto_medio(self, x1, y1, x2, y2):
        medio_x = (x1 + x2) / 2
        medio_y = (y1 + y2) / 2
        return medio_x, medio_y