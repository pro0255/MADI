import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
from collections import Counter
from utils.k_means import k_means
from vizualization.draw2d import draw2d



data = pd.read_csv('iris.csv', ';')

def calculate_mean_attribute(data, i, p=True):
    attribute_name = data.columns[i]
    casted_column = data.iloc[:, i]

    n = len(casted_column)

    mean = 0
    suma = 0

    for row_i in range(n):
        number = float(casted_column[row_i].replace(',', '.'))
        suma += number

    mean = suma/n
    if p:
        print(f'atrribute[{attribute_name}]-mean is[{mean}]')
    return (mean, attribute_name)

def calculate_variance_attribute(data, i):
    attribute_name = data.columns[i]
    casted_column = data.iloc[:, i]
    mean = calculate_mean_attribute(data, i, False)

    suma = 0
    n = len(casted_column)

    for row_i in range(n):
        number = float(casted_column[row_i].replace(',', '.'))
        distance = math.sqrt(pow(number - mean[0], 2))
        suma += pow(distance, 2)


    var = suma/n
    print(f'atrribute[{attribute_name}]-variance is[{var}]')
    return (var, attribute_name)
    
def calculate_global_mean(data, p=True):
    average_instance = []

    for col_i in range(len(data.columns)):
        average_instance.append(calculate_mean_attribute(data, col_i, False)[0])

    if p:
        print(f'average instance-[{average_instance}]')
    return average_instance

def calculate_global_variance(data):
    total_var = 0
    average_instance = calculate_global_mean(data, False)

    suma = 0

    n = len(data)
    for index in range(n):
        row_vector = data.iloc[index, :]
        casted = [float(x.replace(',','.')) for x in row_vector]
        distance = eucladian_distance(casted, average_instance)
        suma += pow(distance, 2)

    total_var = suma/n
    print(f'total variance-[{total_var}]')
    return total_var

def run(data, method, info):
    print(info)
    result=[]
    for index in range(len(data.columns)):
        var = method(data, index)
        result.append(var)
    return result

def eucladian_distance(v_x, v_y):
    suma = 0
    n = len(v_x)
    for i in range(n):
        suma += pow((v_x[i] - v_y[i]), 2)
    return math.sqrt(suma)


def delimiter():
    print('==========================')

def lab_info():
    delimiter()
    print('\nALGEBRAICKÝ A GEOMETRICKÝ POHLED NA DATA\n\tlab n. 4\n')
    delimiter()

def describe_graph(ax, sigma, mean, name):
    ax.set_ylabel('probability')
    title = name.upper().replace('_', ' ')
    ax.title.set_text('%s  m = %.2f,  s = %.2f' % (title, mean, sigma))
    ax.grid()


def draw_distribution(data, data_set):
    f, axes = plt.subplots(1, len(data), figsize=(18,6))

    for index, ax in enumerate(axes):
        item_data = data[index]
        variance = item_data[1][0]
        name = item_data[0][1]
        column = data_set[name]
        mean = item_data[0][0]
        sigma = math.sqrt(variance)
        series_casted = [float(value.replace(',', '.')) for value in column.values]

        minimum = min(series_casted) - 2 
        maximum = max(series_casted) + 2

        samples = 1000


        populated_array_x = np.linspace(minimum-2, maximum+2, samples)
        populated_array_y = [(1/math.sqrt(2*math.pi*variance))*math.exp(-(math.pow(value-mean,2)/(2*variance))) for value in populated_array_x]

        describe_graph(ax, sigma, mean, name)
        # Plot the histogram.



        ax.hist(series_casted, bins=10,  density=True, alpha=0.6, color='g', histtype='bar', ec='black')
        ax.plot(populated_array_x, populated_array_y, linewidth=2, c="b")




data_without_class = data.drop(['variety'], axis=1)

def draw_cdf(data, data_set):
    f, axes = plt.subplots(1, 4, figsize=(18,6))
    samples = 10

    for index, column_name in enumerate(data_set):
        item_data = data[index]
        variance = item_data[1][0]
        name = item_data[0][1]
        mean = item_data[0][0]
        sigma = math.sqrt(variance)

        ax = axes[index]
        column = data_set[column_name]
        series_casted = np.array([float(value.replace(',', '.')) for value in column.values])

        minimum = min(series_casted)
        maximum = max(series_casted)

        describe_graph(ax, sigma, mean, name)


        populated_array = np.linspace(minimum-1, maximum+1, samples)
        probability_array = [len(series_casted[series_casted <= value])/len(series_casted) for value in populated_array]
        populated_array_y = [(1/math.sqrt(2*math.pi*variance))*math.exp(-(math.pow(value-mean,2)/(2*variance))) for value in populated_array]
        cumsum_populated_array_y = list()
        cumsum = 0
        for y in populated_array_y:
            cumsum += y
            cumsum_populated_array_y.append(cumsum/sum(populated_array_y))
        ax.plot(populated_array, cumsum_populated_array_y, c="r")
        ax.plot(populated_array, probability_array, c='g')



lab_info()
means = run(data_without_class, calculate_mean_attribute, 'ATTRIBUTE MEAN\n')
delimiter()
variances = run(data_without_class, calculate_variance_attribute, 'ATTRIBUTE VARIANCE\n')
delimiter()
calculate_global_mean(data_without_class)
delimiter()
calculate_global_variance(data_without_class)
delimiter()

means_and_variances  = list(zip(means, variances))


#draw normal gaussian distribution for every column
#calc real distrubution
#draw real distribution to histograms


# draw_distribution(means_and_variances, data_without_class)
# draw_cdf(means_and_variances, data_without_class)
# plt.show()



k_means_data = data.drop(['variety'], axis=1) 
for index, value in k_means_data.items():
     k_means_data.loc[:, index] = value.str.replace(',', '.').astype(float)
draw2d(*k_means(k_means_data, 3), (2,3))


