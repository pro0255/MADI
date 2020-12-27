import random
import pandas as pd
from utils.accuracy import accuracy_score
import numpy as np

def partition(i, X, y, n_float):
    ##X_train, y_train, X_test, y_test
    start_test = int(i*n_float) 
    end_test = int((i+1)*n_float)

    X_test = X[start_test:end_test]
    y_test = y[start_test:end_test]


    start_train_part_one = 0 
    end_train_part_one = int((i)*n_float)
    start_train_part_two = int((i+1)*n_float)


    # print(start_test, end_test)
    # print(start_train_part_one, end_train_part_one, start_train_part_two)

    X_parts = [X[start_train_part_one:end_train_part_one], X[start_train_part_two:]]
    y_parts = [y[start_train_part_one:end_train_part_one], y[start_train_part_two:]]

    X_train = pd.concat(X_parts)
    y_train = pd.concat(y_parts)


    return (X_train, y_train, X_test, y_test)


def fold_validation(model, X, y, k):
    n = int(len(X) / k)
    n_float = len(X)/k

    seed = random.randint(0, 100)
    shuffled_X = X.sample(frac=1, random_state=seed) 
    shuffled_y = y.sample(frac=1, random_state=seed)

    cells = [partition(i, shuffled_X, shuffled_y, n_float) for i in range(k)] #tuple (x against y)
    accuracies = []

    print('whole:', len(shuffled_X))

    for X_train, y_train, X_test, y_test in cells:
        model.fit(X_train, y_train)
        labels, _ = model.predict(X_test)
        accuracy = accuracy_score(labels, y_test.values)
        accuracies.append(accuracy)

    print(accuracies)
    average = np.sum(accuracies)/len(accuracies)
    print(f'average: {average}')