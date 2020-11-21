import matplotlib.pyplot as plt
from utils.graph.GraphProperties import GRAPH_INSPECTION, GRAPH_CONNECTED_COMPONENTS_PROPERTIES, GRAPH_PROPERTIES
import os
import networkx as nx

GRAPH_OUTPUTS = 'graph_outputs'

class GraphMaker():
    def __init__(self, graph_inspection):
        self.path = GRAPH_OUTPUTS
        self.graph_inspection = graph_inspection
    #!: todo make graphs dependent on dictionary

    def create_directory(self, directory):
        if not os.path.exists(f'{self.path}//{directory}'):
            os.makedirs(f'{self.path}//{directory}')

    def create_prefix(self, prefix):
        return f'{prefix}-' if prefix else ""

    def plot_components_distribution(self, directory="",prefix=""):
        connected_components = self.graph_inspection[GRAPH_INSPECTION.CONNECTED_COMPONENTS]
        counter = connected_components[GRAPH_CONNECTED_COMPONENTS_PROPERTIES.COMPONENTS_COUNTER]
        s = sorted(counter.items())
        size, occurences = zip(*s)
        plt.bar(size, height=occurences)
        plt.title('Rozlozeni komponent souvislosti')
        plt.xlabel('Velikost')
        plt.ylabel('Pocet krat')
        plt.grid()
        plt.xticks(size, size)
        self.create_directory(directory)
        plt.savefig(f'{self.path}//{directory}//{self.create_prefix(prefix)}components_distribution.png')
        plt.clf()
        # plt.show()


    def plot_degree_distribution(self, directory="",prefix=""):
        graph = self.graph_inspection[GRAPH_INSPECTION.WHOLE]
        degree_distribution = graph[GRAPH_PROPERTIES.DEGREE_DISTRIBUTION]
        s = sorted(degree_distribution.items())
        degree, occurences = zip(*s)
        plt.bar(degree, height=occurences)
        plt.title('Distribuce stupnu')
        plt.xlabel('Stupen')
        plt.ylabel('Pocet krat')
        plt.grid()
        plt.xticks(degree, degree)
        self.create_directory(directory)
        plt.savefig(f'{self.path}//{directory}//{self.create_prefix(prefix)}degree_distribution.png')
        plt.clf()
        # plt.show()

    def plot_graph(self, directory="", prefix=""):
        graph = self.graph_inspection[GRAPH_INSPECTION.WHOLE]
        matrix = graph[GRAPH_PROPERTIES.ADJECENCY_MATRIX]
        G = nx.from_numpy_matrix(matrix)
        nx.draw(G, with_labels=True)
        plt.savefig(f'{self.path}//{directory}//{self.create_prefix(prefix)}graph_vizualization.png')
        plt.clf()