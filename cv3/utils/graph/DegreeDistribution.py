import numpy as np
from collections import Counter

def degree_distribution(matrix, verbose=False):
    de = []
    output = '\n========================\nDegree Distribution\n========================\n'
    for i, row in enumerate(matrix):
        vertex_index = i + 1
        degree = len(row[row == 1])
        o = f'ID {vertex_index} - Degree {degree}'
        output += f'{o}\n'
        if verbose:
            print(o)
        de.append(degree)

    c = Counter(de)
    maximal = max(c.keys())
    minimal = min(c.keys())
    average = sum(de)/len(de)
    maxo = f'Maximalni stupen - {maximal}'
    mino = f'Minimalni stupen - {minimal}'
    avgo = f'Prumerny stupen - {average}' 

    output += f'{maxo}\n'
    output += f'{mino}\n'
    output += f'{avgo}\n'

    if verbose:
        print(maxo)
        print(mino)
        print(avgo)
    return (output, (maximal, minimal, average))





