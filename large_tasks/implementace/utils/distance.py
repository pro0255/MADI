import numpy as np
import math

def type_calculation(valueA, valueB):
    if type(valueA) is tuple:
        castedA = np.array(valueA)
        castedB = np.array(valueB)
        return np.linalg.norm(castedA - castedB)
        # result = calc_distance(castedA, castedB) 
        return result
    else:
        return pow(valueA - valueB, 2)

def calc_distance(a, b):
    try:
        if type(a) is list or type(a) is np.ndarray:
            d = 0
            for i in range(len(a)):
                valueA = a[i]
                valueB = b[i]
                d += type_calculation(valueA, valueB)
            return math.sqrt(d)
        return math.sqrt(type_calculation(a, b))
    except Exception as e:
        print(e)
        return 0