import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sys


data = pd.read_csv("KarateClub.csv", ';', header=None)


class Vertex():
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.degree = 0

    def __str__(self):
        return f'Vertex id [{self.id}], degree [{self.degree}], edges [{self.edges}]'


class FloydAlgorithm():
    def __init__(self):
        pass

    def start(self, adjacency_matrix):
        print('Starting FloydAlgorithm')
        number_of_vertecies = len(adjacency_matrix)

        floyd_matrix = np.full(adjacency_matrix.shape, np.inf)
        for i in range(len(floyd_matrix)):
            floyd_matrix[i][i] = 0

        for i in range(len(floyd_matrix)):
            for j in range(len(floyd_matrix)):
                if adjacency_matrix[i][j] != 0:
                    floyd_matrix[i][j] = adjacency_matrix[i][j]


        for k in range(number_of_vertecies):
            for i in range(number_of_vertecies):
                for j in range(number_of_vertecies):
                    first = floyd_matrix[i][j]
                    second = floyd_matrix[i][k]
                    third = floyd_matrix[k][j]

                    if first > second + third:
                        floyd_matrix[i][j] = second + third

        return floyd_matrix


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

    

def calculate_closness_centrality(floyd_matrix,i):
    result = len(floyd_matrix[i])/np.sum(floyd_matrix[i])
    print(f'ID {i+1} - clossnes centraility {result}')
    return result

def average_distance(floyd_matrix):
    n = len(floyd_matrix)
    sum = 0
    for i in range(n):
        for j in range(i, n):
            sum += floyd_matrix[i][j]
    result = (2/(n*(n-1)))*sum
    print(f'Prumerna vzdalenost - {result}')
    return result


def graph_average(floyd_matrix):
    max_excentricity = None

    for row in floyd_matrix:
        vertex_excentricity = np.max(row)

        if max_excentricity is None:
            max_excentricity = vertex_excentricity
        else:
            if vertex_excentricity > max_excentricity:
                max_excentricity = vertex_excentricity 

    print(f'Prumer grafu - {max_excentricity}')
    return max_excentricity





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





print('\n=============CV6==========')



def calculate_cluster_coefficient(a_matrix, vi):
    cluster_coefficient = 0
    current_matrix = a_matrix
    current_row = current_matrix[vi]

    indeces = np.concatenate(np.argwhere(current_row == 1)) 
    number_of_neighbours = len(indeces)
    maximum_number_of_edges = number_of_neighbours * (number_of_neighbours - 1) 



    if number_of_neighbours < 2:
        return 0
    
    number_of_edges = 0

    for index, j in enumerate(indeces):
        vj =  current_matrix[j]
        for k in indeces[index:]:
            if vj[k]:
                number_of_edges += 1

    cluster_coefficient = (2*number_of_edges) / maximum_number_of_edges
    return cluster_coefficient

def run_calculate_cluster_coefficient(matrix):
    current_matrix = matrix.matrix
    csv=""
    for vertex_index, _ in enumerate(current_matrix):
        tranformed_vertex_index = vertex_index + 1
        result = calculate_cluster_coefficient(current_matrix, vertex_index)
        csv += f'{tranformed_vertex_index};{result}\n'
    return csv

print('==========================')
csv =run_calculate_cluster_coefficient(matrix) #it is ok

with open('cluster_coefficient.csv', 'w') as f:
    f.write(csv)
print('==========================')












