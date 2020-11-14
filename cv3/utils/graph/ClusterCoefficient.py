import numpy as np


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
    suma = 0
    for vertex_index, _ in enumerate(current_matrix):
        tranformed_vertex_index = vertex_index + 1
        result = calculate_cluster_coefficient(current_matrix, vertex_index)
        suma += result 
        csv += f'{tranformed_vertex_index};{result}\n'
    return (csv, suma)