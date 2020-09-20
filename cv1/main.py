import pandas as pd
import itertools
import numpy as np

## 16.9.2020
result = list()

data = pd.read_csv("cv1/dataset.csv", ";")

playDelimiter = "yes"

# we should find this combination of values where is probability 100%
# actually i can try to dynamic split for values in play


data_NO = data[data["Play"] != playDelimiter]
data_YES = data[data["Play"] == playDelimiter]


class Tree:
    def __init__(self, children):
        self.children = [Node(None, "root", [])]


class Node:
    def __init__(self, parent, id, children):
        self.parent = parent
        self.id = id
        self.children = []


data_WITHOUT_PLAY = data.drop(["Play"], axis=1)


def generate_combs_tree(data):
    tree = Tree([])
    uniques = {}
    for (columnName, columnData) in data.iteritems():
        uniques[columnName] = columnData.unique()
    # print(data)

    lastNodes = [tree.children]
    for key in uniques:
        newLastNodes = list()
        for item in lastNodes:  # pole(1-n) v poli
            for node in item:
                nodeChildrens = [Node(item, key, []) for i in uniques[key]]
                node.children = nodeChildrens
                newLastNodes.append(nodeChildrens)
        lastNodes = newLastNodes

    return tree


emptyString = "empty"


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
        combination_value = {"yes": [], "no": []}
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
            play_attribute = data.loc[rowIndexInDataset, "Play"]
            if add == len(combination):  ## all values are same as combination
                combination_value[play_attribute].append(rowIndexInDataset)
        result[combination] = combination_value
    return result


def get_all_rules(combs_results):
    all_rules = {}
    for combination in combs_results:
        combination_value = combs_results[combination]
        combination_value_yes = combination_value["yes"]  # list
        combination_value_no = combination_value["no"]  # list

        if len(combination_value_yes) == 0 and len(combination_value_no) == 0:
            # this combination not occured in dataset ;]
            continue
        if len(combination_value_yes) == 0:
            # no rule
            all_rules[combination] = {"value": combination_value, "play": "no"}
        elif len(combination_value_no) == 0:
            # yes rule
            all_rules[combination] = {"value": combination_value, "play": "yes"}
    return all_rules


def get_abstract_rules(all_rules, data):
    first_column = data.iloc[:, 0]
    uniques_in_column = first_column.unique().tolist()
    uniques_in_column.append(emptyString)
    abstract_rules_dict = {}  # dict where are specified for number of empty comb
    for unique_value_in_first_column in uniques_in_column:
        dict_empty = {0: [], 1: [], 2: [], 3: []}
        for combination in all_rules:
            if unique_value_in_first_column == combination[0]:
                empty_counter = 0
                for value_in_tuple in combination:
                    if value_in_tuple == emptyString:
                        empty_counter += 1

                dict_empty[empty_counter].append(combination)

        abstract_rules_dict[unique_value_in_first_column] = dict_empty

    list_of_abstract_rules = []
    for unique_value_in_first_column in uniques_in_column:
        abstract_rules_value = abstract_rules_dict[unique_value_in_first_column]
        value_len = len(abstract_rules_value)
        for key in reversed(range(value_len)):
            if len(abstract_rules_value[key]) != 0:
                for rule in abstract_rules_value[key]:
                    list_of_abstract_rules.append(rule)
                break

    return list_of_abstract_rules


tree_combs = generate_combs_tree(data_WITHOUT_PLAY)
combs_results = generate_combs_result(list(generate_combs(data_WITHOUT_PLAY)), data)
all_rules = get_all_rules(combs_results)
generated_abstract_rules = get_abstract_rules(all_rules, data)


with open("output_rules.txt", "w") as f:
    list_columns = data.columns
    number_of_rules = 0
    for rule in generated_abstract_rules:
        play_value = all_rules[rule]["play"]
        description_string = "If "
        for index, value in enumerate(rule):
            if value != emptyString:
                description_string += f"{list_columns[index]} == {value} "
        number_of_rules += 1
        f.write(
            f"RULE {number_of_rules} --> {description_string}then play == {play_value}\n"
        )
