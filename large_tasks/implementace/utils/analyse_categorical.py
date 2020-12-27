from collections import Counter
import matplotlib.pyplot as plt
from utils.graph_props import run_plot_props
plt.figure(figsize=(10,8))

def absolute(keys, values):
    plt.bar(keys, values, ec="black", color="g")
    run_plot_props()
    plt.show()

def relative(keys, values):
    s = sum(values)
    tranformed_values = [v/s for v in values]
    plt.bar(keys, tranformed_values, ec="black", color="g")
    run_plot_props()
    plt.show()


def analyse_categorial(data_set, name):
    feature = data_set.loc[:, name]
    c = Counter(feature)
    values = list(c.values())
    keys = list(c.keys())

    print(f'attribute with name = {name}')
    for i in range(len(values)):
        v = values[i]
        k = keys[i]
        print(f'{v} -> {k}')

    print(f'\n')
    absolute(keys, values)
    relative(keys, values)


