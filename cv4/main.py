import pandas as pd
import numpy as np
import math

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
    return mean


def calculate_variance_attribute(data, i):
    attribute_name = data.columns[i]
    casted_column = data.iloc[:, i]
    mean = calculate_mean_attribute(data, i, False)

    suma = 0
    n = len(casted_column)

    for row_i in range(n):
        number = float(casted_column[row_i].replace(',', '.'))
        distance = math.sqrt(pow(number - mean, 2))
        suma += pow(distance, 2)


    var = suma/n
    print(f'atrribute[{attribute_name}]-variance is[{var}]')
    return var
    

def calculate_global_mean(data, p=True):
    average_instance = []

    for col_i in range(len(data.columns)):
        average_instance.append(calculate_mean_attribute(data, col_i, False))

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
    for index in range(len(data.columns)):
        method(data, index)







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





data_without_class = data.drop(['variety'], axis=1)


lab_info()
run(data_without_class, calculate_mean_attribute, 'ATTRIBUTE MEAN\n')
delimiter()
run(data_without_class, calculate_variance_attribute, 'ATTRIBUTE VARIANCE\n')
delimiter()
calculate_global_mean(data_without_class)
delimiter()
calculate_global_variance(data_without_class)
delimiter()



