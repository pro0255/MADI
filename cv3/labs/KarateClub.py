import numpy as np
import pandas as pd
from utils.graph.Matrix import AdjacencyList, AdjacencyMatrix

def matrix_list_histogram_for_karate_club(data):
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

    rc = True
    show_hist = False
    if show_hist:
        bins = list(range(1, np.max(matrix_list.all_degres)+2))
        weights = np.zeros_like(occurences) + 1 / len(occurences)
        bins = math.ceil(((np.max(occurences) - np.min(occurences)) + 1)/1)
        plt.hist(occurences, bins=bins, alpha=0.5, histtype='bar', ec='black', color="green", density=rc)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel(f"degrees (# of connections)")
        plt.ylabel(f"# of nodes")
        plt.title("Karate Club Degree Distribution")
        plt.show()

    return matrix
