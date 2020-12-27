from utils.mean import calc_mean
from utils.distance import calc_distance
import numpy as np
import matplotlib.pyplot as plt
import math


def describe_graph(ax, sigma, mean, name):
    title = name.upper().replace('_', ' ')
    ax.title.set_text('%s  m = %.2f,  s = %.2f' % (title, mean, sigma))
    ax.grid()


def draw_distribution(data, mean, variance, name):
    f, ax = plt.subplots(1, figsize=(8,6))
    val = data.values
    sigma = math.sqrt(variance)
    minimum = min(val) - 2 
    maximum = max(val) + 2
    samples = 1000
    populated_array_x = np.linspace(minimum-2, maximum+2, samples)
    populated_array_y = [(1/math.sqrt(2*math.pi*variance))*math.exp(-(math.pow(value-mean,2)/(2*variance))) for value in populated_array_x]

    describe_graph(ax, sigma, mean, name)
    ax.hist(val, bins=10,  density=True, alpha=0.6, color='g', histtype='bar', ec='black')
    ax.plot(populated_array_x, populated_array_y, linewidth=2, c="b")
    return f, ax


def draw_cdf(data, mean, variance, name):
    f, ax = plt.subplots(1, figsize=(8,6))
    samples = 10
    val = data.values
    sigma = math.sqrt(variance)
    minimum = min(val)
    maximum = max(val)
    describe_graph(ax, sigma, mean, name)

    populated_array = np.linspace(minimum-1, maximum+1, samples)
    probability_array = [len(val[val <= value])/len(val) for value in populated_array]
    populated_array_y = [(1/math.sqrt(2*math.pi*variance))*math.exp(-(math.pow(value-mean,2)/(2*variance))) for value in populated_array]

    cumsum_populated_array_y = list()
    cumsum = 0
    for y in populated_array_y:
        cumsum += y
        cumsum_populated_array_y.append(cumsum/sum(populated_array_y))
    ax.plot(populated_array, cumsum_populated_array_y, c="r")
    ax.plot(populated_array, probability_array, c='g')
    return f,ax






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






