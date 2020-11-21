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
from utils.graph.GraphProperties import make_graph_inspection
from printer.GraphInspectionPrinter import print_graph_inspection, write_graph_inspection_to_file
from labs.RandomGraphGenerate import run_lab_where_generating_graphs
from labs.KarateClub import matrix_list_histogram_for_karate_club
from labs.KarateClubFloydAndGraphProps import karate_club_floyd_and_graph_props
from utils.graph.Matrix import Vertex, AdjacencyList, AdjacencyMatrix
from graph_api.GraphMaker import GraphMaker
from graph_api.GraphMakerRun import run_graph_maker


################################
"""Csv with graph"""
data = pd.read_csv("KarateClub.csv", ';', header=None)
################################

################################
"""Old labs"""
karate_club_matrix = matrix_list_histogram_for_karate_club(data)
# karate_club_floyd_and_graph_props(karate_club_matrix.matrix)
karate_club_inspection = make_graph_inspection(karate_club_matrix.matrix)
name = "karate_club"
write_graph_inspection_to_file(f'{name}.txt', name, karate_club_inspection, "Karate club\n")
run_graph_maker(karate_club_inspection, name)
################################

################################
"""Cv8"""
# g1, g2, g3 = run_lab_where_generating_graphs()
# run_graph_maker(g1[1], 'g1')
# run_graph_maker(g2[1], 'g2')
# run_graph_maker(g3[1], 'g3')
################################













