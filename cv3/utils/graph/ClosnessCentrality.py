import numpy as np

def calculate_closness_centrality(floyd_matrix, i, verbose=False):
    result = len(floyd_matrix[i])/np.sum(floyd_matrix[i])
    o = f'ID {i+1} - clossnes centraility {result}'
    output = f'{o}\n'
    if verbose:
        print(o)
    return (output, result)