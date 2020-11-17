
from utils.graph.Floyd import FloydAlgorithm
from utils.graph.ClosnessCentrality import calculate_closness_centrality
from utils.graph.AverageDistance import average_distance
from utils.graph.GraphAverage import graph_average
from utils.graph.ClusterCoefficient import calculate_cluster_coefficient, run_calculate_cluster_coefficient
from utils.graph.ClusterEffect import draw_cluster_effect

DRAW = True


def karate_club_floyd_and_graph_props(karate_club_matrix):
    print('\n=============CV3===========')
    floyd = FloydAlgorithm()
    floyd_matrix = floyd.start(karate_club_matrix)

    print(floyd_matrix)
    average_distance(floyd_matrix)
    print('==========================')
    graph_average(floyd_matrix)
    print('==========================')
    for i in range(len(floyd_matrix)):
        calculate_closness_centrality(floyd_matrix, i)
    print('==========================')
    def calculcate_graph_transitivity(suma, matrix):
        return suma/len(karate_club_matrix)
    def print_lab6_result(csv, transitivity):
        print('=========Cluster Coeficient===========')
        print(csv)
        print('=========Graph Transitivity===========')
        print(transitivity)
        print('======================================')
    print('==========================')
    csv, suma  = run_calculate_cluster_coefficient(karate_club_matrix) #it is ok
    transitivity = calculcate_graph_transitivity(suma, karate_club_matrix)


    if DRAW:
        draw_cluster_effect(karate_club_matrix)

    print_lab6_result(csv, transitivity)


    def write_to_file(path, text, des = ''):
        final = f'{des} \n {text}'
        with open(path, 'w') as f:
            f.write(final)    

    write_to_file('cluster_coefficient.csv', csv)

