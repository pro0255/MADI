from utils.mean import calc_mean
import numpy as np

def calc_average_instance(matrix_data, number_of_features):
    average_instance = [0] * number_of_features
    try:
        for i in range(len(average_instance)):
            average_instance[i] = calc_mean(matrix_data[:, i])
        return np.array(average_instance)
    except:
        return np.array(average_instance)
