import numpy as np

def type_calculation(valueA, valueB):
    if type(valueA) is tuple:
        result = np.linalg.norm(np.array(valueA)-np.array(valueB)) 
        return result
    else:
        return pow(valueA - valueB, 2)

def calc_distance(a, b):
    if type(a) is list or type(a) is np.ndarray:
        d = 0
        for i in range(len(a)):
            valueA = a[i]
            valueB = b[i]
            d += type_calculation(valueA, valueB)
        return d
    return type_calculation(a, b)
