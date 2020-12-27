import numpy as np

def calc_distance(a, b):
    d = 0
    for i in range(len(a)):
        valueA = a[i]
        valueB = b[i]
        if type(valueA) is tuple:
           result = np.linalg.norm(np.array(valueA)-np.array(valueB)) 
           d += result
        else:
            d += pow(valueA - valueB, 2)
    return d