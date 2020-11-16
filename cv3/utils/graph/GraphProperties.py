import pandas as pd
from utils.graph.Floyd import FloydAlgorithm
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient, calculcate_graph_transitivity
from utils.graph.DegreeDistribution import degree_distribution
from utils.graph.ConnectedComponents import connected_components
from collections import defaultdict
import numpy as np

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




def inspect_graph(matrix, verbose=True):
    components_output = ""
    components, matrix = connected_components(matrix)
    number_of_connected_components = len(components.keys())
    
    number_of_components_output = f'Pocet komponent souvislosti je {number_of_connected_components}'
    components_output += f'{number_of_components_output}\n'

    if verbose:
        print(number_of_components_output)

    distribution = defaultdict(int)
    for k,v in components.items():
        component_len_output = f'Komponenta ID {k} je velka {len(v)}'
        components_output += f'{component_len_output}\n'
        if verbose:
            print(component_len_output)
            distribution[len(v)] += 1

    components_output += '\nDitrubuce\n'

    for k,v in distribution.items():
        components_distribution_output = f'Komponent s velikosti {k} je {v}'
        components_output += f'{components_distribution_output}\n'

        if verbose:
            print(components_distribution_output)


    components_output += '\nDitrubuce relativni cetnost\n'
    for k,v in distribution.items():
        components_distribution_output = f'Komponent s velikosti {k} je {(v/sum(distribution.values()) * 100)}%'
        components_output += f'{components_distribution_output}\n'

        if verbose:
            print(components_distribution_output)

    components_output += f'\n'



    max_len_component = max([len(value) for value in components.values()])
    max_len_component_output = f'Velikost nejvetsi komponenty je {max_len_component}'
    components_output += f'{max_len_component_output}\n'
    if verbose:
        print(max_len_component_output)
    sorted_components_indicies = [sorted(value) for value in components.values()]


    subgraphs = []
    for subgraph_indicies in sorted_components_indicies:
        grid = np.ix_(subgraph_indicies, subgraph_indicies)
        subgraphs.append(matrix[grid])

    
    for index,subgraph in enumerate(subgraphs):
        subgraph_output = print_graph_properties(subgraph)
        components_output += f'\n====================Komponenta ID {index} vlastnosti===================\n{subgraph_output}\n=========================================\n'

    return components_output


    


    