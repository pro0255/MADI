import pandas as pd
from utils.graph.Floyd import FloydAlgorithm
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient, calculcate_graph_transitivity
from utils.graph.DegreeDistribution import degree_distribution


verbose = False

def print_graph_properties(matrix):
    all_output = ''

    floyd = FloydAlgorithm()
    floyd_matrix = floyd.start(matrix)

    degree_output, degree_value = degree_distribution(matrix, verbose)
    average_output, average_distance_value = average_distance(floyd_matrix, verbose)
    graph_average_output, graph_average_value = graph_average(floyd_matrix, verbose)


    calculate_closness_centrality_sum_output = ''
    for i in range(len(floyd_matrix)):
        calculate_closness_centrality_output, calculate_closness_centrality_value = calculate_closness_centrality(floyd_matrix, i, verbose)
        calculate_closness_centrality_sum_output += f'{calculate_closness_centrality_output}'

    cluster_coefficient_output, suma  = run_calculate_cluster_coefficient(matrix, verbose) #it is ok


    transitivity = calculcate_graph_transitivity(matrix)
    transitivity_output = f'Graph transitivity - {transitivity}'
    
    all_output += f'{degree_output}\n'
    all_output += f'{average_output}\n'
    all_output += f'{graph_average_output}\n'
    all_output += f'{calculate_closness_centrality_sum_output}\n'
    all_output += f'Cluster coefficient - \n{cluster_coefficient_output}'
    all_output += f'{transitivity_output}\n'
    return all_output

