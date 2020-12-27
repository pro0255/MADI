from utils.mean import calc_mean
from utils.distance import calc_distance
import numpy as np


def analyse_numeric(data_set, name):
    feature = data_set.loc[:, name]
    # global_mean(data_set)
    global_variance(data_set)
    # attribute_variance(feature)
    # print(attribute_mean(feature))

def attribute_mean(feature):
    return calc_mean(feature.values)

def attribute_variance(feature):
    aM = attribute_mean(feature)
    s = 0
    for value in feature:
        distance = calc_distance(value,aM)
        s += pow(distance,2)
    variance = s/len(feature)
    return variance


def global_mean(dS):
    average_instance = []
    for col in dS.columns:
        feature = dS.loc[:, col]
        average_instance.append(attribute_mean(feature))
    return np.array(average_instance)


def global_variance(dS):
    aI = global_mean(dS)
    total_var = 0
    s = 0
    n = len(dS)
    for index in range(n):
        instance_row = dS.iloc[index, :].values
        distance = calc_distance(instance_row, aI)
        s += pow(distance, 2)
    total_var = s/n
    return total_var






