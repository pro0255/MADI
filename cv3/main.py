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

################################
"""Csv with graph"""
data = pd.read_csv("KarateClub.csv", ';', header=None)
################################

################################
"""Old labs"""
karate_club_matrix = matrix_list_histogram_for_karate_club(data)
# karate_club_floyd_and_graph_props(karate_club_matrix.matrix)
################################

################################
"""Cv8"""
g1, g2, g3 = run_lab_where_generating_graphs()
graph_maker = GraphMaker(g1[1])
graph_maker.plot_components_distribution()
################################













