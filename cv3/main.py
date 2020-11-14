import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from utils.graph.Floyd import FloydAlgorithm 
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient
from utils.graph.ClusterEffect import draw_cluster_effect

data = pd.read_csv("KarateClub.csv", ';', header=None)

class Vertex():
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.degree = 0

    def __str__(self):
        return f'Vertex id [{self.id}], degree [{self.degree}], edges [{self.edges}]'

class AdjacencyMatrix():
    def __init__(self, size, data):
        self.matrix = np.zeros((size, size))
        self.create(data)
    

    def create(self, data):
        for row_index in range(data.shape[0]):
            row = data.iloc[row_index, :]
            self.matrix[row[0]-1, row[1]-1] += 1
            self.matrix[row[1]-1, row[0]-1] += 1


    def __str__(self):
        output = ""
        for index, row in enumerate(self.matrix):
            degree = np.sum(row == 1)
            vertex_id = index + 1
            output += f"Id: {vertex_id} - stupen {degree}\n" 
        return output

class AdjacencyList():
    def __init__(self, data):
        self.dic = {}
        self.create()
        self.all_degres = []
        for vertex in self.dic.values():
            self.all_degres.append(vertex.degree)

    def add_to_dict(self, tuple):
        if tuple[0] in self.dic:
            vertex = self.dic[tuple[0]]
            vertex.degree += 1
            vertex.edges.append(tuple[1])
        else:
            new_vertex = Vertex(tuple[0])
            new_vertex.degree += 1
            new_vertex.edges.append(tuple[1])
            self.dic[tuple[0]] = new_vertex


    def create(self):
        for row_index in range(data.shape[0]):
            row = data.iloc[row_index, :]
            self.add_to_dict((row[0], row[1]))
            self.add_to_dict((row[1], row[0]))

    def find_max(self):
        vertex_max = Vertex(-1)
        for item in self.dic.items():
            if vertex_max.degree < item[1].degree:
                vertex_max = item[1]
        return f'Max degree is {vertex_max.degree}'

    def find_min(self):
        vertex_min = None
        for item in self.dic.items():
            if not vertex_min:
                vertex_min = item[1]
                continue
            if vertex_min.degree > item[1].degree:
                vertex_min = item[1]
        return f'Min degree is {vertex_min.degree}'

    def find_average(self):
        degree_count = 0
        for item in self.dic.items():
            degree_count += item[1].degree

        return f'Average is {degree_count/len(self.dic)}'

    def print_values(self):
        print(self.find_min())
        print(self.find_max())
        print(self.find_average())

    def __str__(self):
        output = ""
        for vertex in self.dic.values():
            output += f'{vertex}\n'
        return output


first_column = data.iloc[:, 0]
second_column = data.iloc[:, 1]

max_index_first = np.max(first_column)
max_index_second = np.max(second_column)
max_value = max_index_first if max_index_first > max_index_second else max_index_second  

matrix = AdjacencyMatrix(max_value, data)
matrix_list = AdjacencyList(data)

print('\n=============CV2===========')
print(matrix_list)
print('==========================')
matrix_list.print_values()

occurences = matrix_list.all_degres
# print(occurences)

rc = True
show_hist = False
if show_hist:
    # print(np.max(matrix_list.all_degres))
    bins = list(range(1, np.max(matrix_list.all_degres)+2))
    # print(bins)


    weights = np.zeros_like(occurences) + 1 / len(occurences)

    bins = math.ceil(((np.max(occurences) - np.min(occurences)) + 1)/1)

    plt.hist(occurences, bins=bins, alpha=0.5, histtype='bar', ec='black', color="green", density=rc)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(f"degrees (# of connections)")
    plt.ylabel(f"# of nodes")
    plt.title("Karate Club Degree Distribution")
    plt.show()


print('\n=============CV3===========')
floyd = FloydAlgorithm()
floyd_matrix = floyd.start(matrix.matrix)

print(floyd_matrix)
average_distance(floyd_matrix)
print('==========================')
# graph_average(floyd_matrix)
print('==========================')
for i in range(len(floyd_matrix)):
    calculate_closness_centrality(floyd_matrix, i)
print('==========================')

def calculcate_graph_transitivity(suma, matrix):
    return suma/len(matrix)

def print_lab6_result(csv, transitivity):
    print('=========Cluster Coeficient===========')
    print(csv)
    print('=========Graph Transitivity===========')
    print(transitivity)
    print('======================================')


print('==========================')
csv, suma  = run_calculate_cluster_coefficient(matrix) #it is ok
transitivity = calculcate_graph_transitivity(suma,matrix.matrix)
draw_cluster_effect(matrix.matrix)
print_lab6_result(csv, transitivity)


with open('cluster_coefficient.csv', 'w') as f:
    f.write(csv)
print('==========================')














