import pandas as pd
import itertools
import numpy as np

## 16.9.2020
result = list()

data = pd.read_csv('cv1/dataset.csv', ';')

playDelimiter = 'yes'

#we should find this combination of values where is probability 100%
#actually i can try to dynamic split for values in play


data_NO = data[data['Play'] != playDelimiter]
data_YES = data[data['Play'] == playDelimiter]


class Tree: 
    def __init__(self, children):
        self.children = [Node(None, 'root', [])];

class Node:
    def __init__(self, parent, id, children):
        self.parent = parent
        self.id = id
        self.children = []



data_WITHOUT_PLAY = data.drop(['Play'], axis=1)

def generate_combs_tree(data):
    tree = Tree([])
    uniques = {}
    for (columnName, columnData) in data.iteritems():
        uniques[columnName] = columnData.unique() 
    # print(data)

    lastNodes = [tree.children]
    for key in uniques:
        newLastNodes = list()
        for item in lastNodes: #pole(1-n) v poli
            for node in item:
                nodeChildrens = [Node(item, key, []) for i in uniques[key]]
                node.children = nodeChildrens
                newLastNodes.append(nodeChildrens)
        lastNodes = newLastNodes     
    
    return tree

emptyString = 'empty'


def generate_combs(data):
    unique_lists = []
    for (_, columnData) in data.iteritems():
        unique = columnData.unique().tolist()
        unique.append(emptyString)
        unique_lists.append(unique)

    return itertools.product(*unique_lists)
    

def generate_combs_result(combs, data):
    result = {}
    for combination in combs:
        combination_value = []
        for rowIndexInDataset in range(len(data)):
            add = 0
            for i in range(len(combination)):
                valueCombinationColumn = combination[i]
                if valueCombinationColumn == emptyString:
                    add += 1
                    continue
                valueRowColumn = data.iloc[rowIndexInDataset, i] 
                if valueRowColumn == valueCombinationColumn:
                    add += 1 

            if add == len(combination):
                combination_value.append(rowIndexInDataset)
        result[combination] = combination_value
    return result
                




tree_combs = generate_combs_tree(data_WITHOUT_PLAY)


results = generate_combs_result(list(generate_combs(data_WITHOUT_PLAY)),data)


for key in results:
    print(len(results[key]), len(data), key, results[key])
    if len(results[key]) == len(data):
        print(results[key])



# dic = generate_combs_result(combs)











