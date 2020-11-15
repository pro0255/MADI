import pandas as pd
from utils.graph.Floyd import FloydAlgorithm
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient, calculcate_graph_transitivity
from utils.graph.DegreeDistribution import degree_distribution


verbose = False

def print_graph_properties(matrix):
    floyd = FloydAlgorithm()
    floyd_matrix = floyd.start(matrix)
    degree_distribution(matrix, True)
    average_distance(floyd_matrix, verbose)
    graph_average(floyd_matrix, verbose)

    for i in range(len(floyd_matrix)):
        calculate_closness_centrality(floyd_matrix, i, verbose)

    csv, suma  = run_calculate_cluster_coefficient(matrix, verbose) #it is ok
    transitivity = calculcate_graph_transitivity(matrix)
    print(f'Graph transitivity - {transitivity}')

