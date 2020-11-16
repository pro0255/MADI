import pandas as pd
from utils.graph.Floyd import FloydAlgorithm
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient, calculcate_graph_transitivity
from utils.graph.DegreeDistribution import degree_distribution
from utils.graph.ConnectedComponents import connected_components
from collections import defaultdict, Counter
import numpy as np
from enum import Enum

verbose = False
DELIMITER = '=============================================================='


class GRAPH_PROPERTIES(Enum):
    GRAPH_AVERAGE = 'graph_average' ##prumer graf
    AVERAGE_DISTANCE = 'average_distance' ##prumarna vzdalenost v grafu
    MAX_DEGREE = 'max_degree' ##maximalni stupen v grafu
    MIN_DEGREE = 'min_degree' ##minimalni stupen v grafu
    AVG_DEGREE = 'avg_degree' ##prumerny stupen v grafu
    DEGREE_DISTRIBUTION = 'degree_distribution' ##distribuce stupnu v grafu (moznost histogramu)
    FLOYD_MATRIX = 'floyd_matrix' ##floyd matice - matice vzdalenosti
    ADJECENCY_MATRIX = 'adjecency_matrix' ##matice sousednosti
    GRAPH_TRANSITIVITY = 'graph_transitivity' ## ??
    CLOSSNES_CENTRALITY = 'clossnes_centrality' ## ??
    CLUSTER_COEFFICIENT = 'cluster_coefficient'

class GRAPH_CONNECTED_COMPONENTS_PROPERTIES(Enum):
    NUMBER_OF_CONNECTED_COMPONENTS: 'number_of_connected_components' ##pocet komponent souvislosti
    MAX_CONNECTED_COMPONENT: 'max_connected_component' ##velikost nejvetsi komponenty souvislosti
    MIN_CONNECTED_COMPONENT: 'min_connected_component' ##velikost nejmensi komponenty souvislosti
    COMPONENTS = 'components' ##pole GRAPH_PROPERTIES pro kazdou nelezenou komponentu
    COMPONENTS_PROPERTIES = 'components_properties'
    COMPONENTS_SIZES = 'component_sizes'
    COMPONENTS_COUNTER = 'components_counter'


class GRAPH_INSPECTION(Enum):
    WHOLE = 'whole' ##cely graf - GRAPH_PROPERTIES
    CONNECTED_COMPONENTS = 'connected_components' ##pole - GRAPH_PROPERTIES

def create_connected_components_dictionary_for_graph(matrix):
    result = {}
    components, matrix = connected_components(matrix)
    result[GRAPH_CONNECTED_COMPONENTS_PROPERTIES.COMPONENTS] = components
    result["number_of_connected_components"] = len(components.keys())
    sizes = [len(v) for k,v in components.items()]
    c = Counter(sizes)
    result[GRAPH_CONNECTED_COMPONENTS_PROPERTIES.COMPONENTS_SIZES] = sizes
    result[GRAPH_CONNECTED_COMPONENTS_PROPERTIES.COMPONENTS_COUNTER] = c
    result["max_connected_component"] = max(sizes)

    sorted_components_indicies = [sorted(value) for value in components.values()]
    subgraphs = []
    for subgraph_indicies in sorted_components_indicies:
        grid = np.ix_(subgraph_indicies, subgraph_indicies)
        subgraphs.append(matrix[grid])

    for sub_matrix in subgraphs:
        component_dic = create_graph_properties_dictionary(sub_matrix)
    return result


#!: Create output function for this dictionary
def create_graph_properties_dictionary(matrix):
    floyd = FloydAlgorithm()
    floyd_matrix = floyd.start(matrix)
    properties = {}
    properties[GRAPH_PROPERTIES.ADJECENCY_MATRIX] = matrix
    properties[GRAPH_PROPERTIES.FLOYD_MATRIX] = floyd_matrix
    properties[GRAPH_PROPERTIES.GRAPH_AVERAGE] = graph_average(floyd_matrix)[1]
    degree_value = degree_distribution(matrix)[1]
    properties[GRAPH_PROPERTIES.MAX_DEGREE] = degree_value[0]
    properties[GRAPH_PROPERTIES.MIN_DEGREE] = degree_value[1]
    properties[GRAPH_PROPERTIES.AVG_DEGREE] = degree_value[2]
    properties[GRAPH_PROPERTIES.DEGREE_DISTRIBUTION] = degree_value[3]
    properties[GRAPH_PROPERTIES.AVERAGE_DISTANCE] = average_distance(floyd_matrix)[1]

    closness_centrality_array = []
    for i in range(len(floyd_matrix)):
        calculate_closness_centrality_output, calculate_closness_centrality_value = calculate_closness_centrality(floyd_matrix, i, verbose)
        closness_centrality_array.append(calculate_closness_centrality_value)

    properties[GRAPH_PROPERTIES.CLOSSNES_CENTRALITY] = closness_centrality_array

    cluster_coefficient_array = []
    for i in range(len(matrix)):
        value = calculate_cluster_coefficient(matrix, i, verbose)
        cluster_coefficient_array.append(value)

    properties[GRAPH_PROPERTIES.CLUSTER_COEFFICIENT] = cluster_coefficient_array
    properties[GRAPH_PROPERTIES.GRAPH_TRANSITIVITY] = sum(cluster_coefficient_array)/len(matrix)

    return properties

def make_graph_inspection(matrix):
    dic = {}
    dic[GRAPH_INSPECTION.WHOLE] = create_graph_properties_dictionary(matrix)
    dic[GRAPH_INSPECTION.CONNECTED_COMPONENTS] = create_connected_components_dictionary_for_graph(matrix)
    return dic

def print_graph_properties(matrix):
    PROPERTIES_DIC = create_graph_properties_dictionary(matrix)

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
    return (all_output, PROPERTIES_DIC)





def inspect_graph(matrix, verbose=True):
    GRAPH_DIC = {}
    GRAPH_DIC[GRAPH_INSPECTION.CONNECTED_COMPONENTS] = []


    whole_graph_output, whole_graph_dic = print_graph_properties(matrix)
    GRAPH_DIC[GRAPH_INSPECTION.WHOLE] = whole_graph_dic

    components_output = f'\nCely graf\n{DELIMITER}{whole_graph_output}\n{DELIMITER}\n'
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
        distribution[len(v)] += 1
        if verbose:
            print(component_len_output)

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
        subgraph_output, subgraph_dic = print_graph_properties(subgraph)
        GRAPH_DIC[GRAPH_INSPECTION.CONNECTED_COMPONENTS].append(subgraph_dic)
        components_output += f'\n{DELIMITER}Komponenta ID {index} vlastnosti{DELIMITER}\n{subgraph_output}\n{DELIMITER}\n'

    graph_averages = [component_properties[GRAPH_PROPERTIES.GRAPH_AVERAGE] for component_properties in GRAPH_DIC[GRAPH_INSPECTION.CONNECTED_COMPONENTS]]
    average_over_components = sum(graph_averages)/len(graph_averages)



    return f'Prumer pres jednotlive komponenty souvislosti je {average_over_components}\n{components_output}'


    


    