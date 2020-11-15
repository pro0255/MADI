import numpy as np
from collections import Counter

def degree_distribution(matrix, verbose=False):
    de = []
    for i, row in enumerate(matrix):
        vertex_index = i + 1
        degree = len(row[row == 1])
        # if verbose:
        #     print(f'ID {vertex_index} - Degree {degree}')
        de.append(degree)

    c = Counter(de)
    maximal = max(c.keys())
    minimal = min(c.keys())
    average = sum(de)/len(de)
    if verbose:
        print(f'Max - {maximal}')
        print(f'Min - {minimal}')
        print(f'Avg - {average}')
    return (maximal, minimal, average)





