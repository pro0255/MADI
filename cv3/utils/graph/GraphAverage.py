import numpy as np


def graph_average(floyd_matrix, verbose=False):
    max_excentricity = None

    for row in floyd_matrix:
        vertex_excentricity = np.max(row)

        if max_excentricity is None:
            max_excentricity = vertex_excentricity
        else:
            if vertex_excentricity > max_excentricity:
                max_excentricity = vertex_excentricity 
    if verbose:
        print(f'Prumer grafu - {max_excentricity}')
    return max_excentricity