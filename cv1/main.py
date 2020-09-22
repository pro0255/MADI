import pandas as pd
import itertools
import numpy as np

## 16.9.2020
result = list()

data = pd.read_csv("C:\\Users\\Vojta\\Desktop\\own\\university\\ing\\00\\mad\\cv1\\dataset.csv", ",")

playDelimiter = "yes"

# we should find this combination of values where is probability 100%
# actually i can try to dynamic split for values in play


data_NO = data[data["Play"] != playDelimiter]
data_YES = data[data["Play"] == playDelimiter]




data_WITHOUT_PLAY = data.drop(["Play"], axis=1)



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
        if combination == ("sunny", "cool", emptyString, emptyString):
            print(combination_value)

        if len(combination_value_yes) == 0 and len(combination_value_no) == 0:
            # this combination not occured in dataset ;]
            continue
        elif len(combination_value_yes) == 0:
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
        print(abstract_rules_value)
        value_len = len(abstract_rules_value)
        for key in reversed(range(value_len)):
            if len(abstract_rules_value[key]) != 0:
                for rule in abstract_rules_value[key]:
                    list_of_abstract_rules.append(rule)
                break


    # print(list_of_abstract_rules)
    return list_of_abstract_rules


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

















# unique_outlook = data['Outlook'].unique()
# unique_temperature = data['Temperature'].unique()
# unique_humidity = data['Humidity'].unique()
# unique_windy = data['Windy'].unique()


# rules_yes = []
# rules_no = []

# def write_rule(attributes_dict, play_value, number_of_times):
#     description_string = "If "
#     for k,v in attributes_dict.items():
#         if v != emptyString: 
#             description_string += f"{k} == {v} "
#     output = f" [{number_of_times}] ---> {description_string}then play == {play_value}\n"
#     if play_value == 'yes':
#         rules_yes.append(output)
#     else:
#         rules_no.append(output)
#     # print(output)


# def add_ignore_to_unique(unique):
#     return np.append(unique, emptyString)

# def check_rule(outlook = emptyString, temperature = emptyString, humidity = emptyString, windy = emptyString):
#     filtered_data = data
#     if outlook != emptyString:
#         filtered_data = filtered_data[filtered_data['Outlook'] == outlook]
#     if temperature != emptyString:
#         filtered_data = filtered_data[filtered_data['Temperature'] == temperature]
#     if humidity != emptyString:
#         filtered_data = filtered_data[filtered_data['Humidity'] == humidity]
#     if windy != emptyString:
#         filtered_data = filtered_data[filtered_data['Windy'] == (windy == "True")]
#     number_of_no = filtered_data[filtered_data['Play'] == 'no']['Play'].count()
#     number_of_yes =  filtered_data[filtered_data['Play'] == 'yes']['Play'].count()

    
#     if humidity == 'normal' and outlook == emptyString and temperature == emptyString:
#         print(filtered_data, number_of_no, number_of_yes)
#         print(outlook, temperature, humidity, windy)
#         print('==================')

#     if number_of_no == 0 and number_of_yes == 0:
#         return False
#     elif number_of_no == 0:
#         write_rule({'outlook': outlook, 'temperature': temperature, 'humidity': humidity, 'windy': windy}, 'yes', number_of_yes)
#         return True
#     elif number_of_yes == 0:
#         write_rule({'outlook': outlook, 'temperature': temperature, 'humidity': humidity, 'windy': windy}, 'no', number_of_no)
#         return True
#     return False


# class Node:
#     def __init__(self, parent, children, key):
#         self.parent = parent
#         self.combs_values = []
#         self.children = []
#         self.key = key

#     def generate_combs(self):
#         self.combinations = list(itertools.product(*self.combs_values))
#         self.get_max_rules()

#     def get_max_rules(self):
#         self.rules = []
#         for item in self.combinations:
#             print(item)



# def generate_tree(input_data, input_set, parent):
#     children = []

#     for index,_ in enumerate(input_set):
#         node_last_value_index = index 
#         if parent.key >= 0:
#             node_last_value_index += parent.key + 1
#         new_node = Node(parent, [], node_last_value_index)
#         if node_last_value_index < len(input_set):
#             new_array_combs = parent.combs_values.copy()
#             new_array_combs.append(input_set[node_last_value_index])
#             new_node.combs_values = new_array_combs
#             new_node.generate_combs()
#             children.append(new_node)
#         if node_last_value_index + 1 < len(input_set):
#             generate_tree(input_data, input_set, new_node)
#     parent.children = children


# root = Node(None, [], -1)

# generate_tree(data, [unique_outlook, unique_temperature, unique_humidity, unique_windy], root)


# for item in root.children:
#     pass










# for outlook_value in add_ignore_to_unique(unique_outlook):
#     if(check_rule(outlook_value)):
#         continue
#     for temperature_value in add_ignore_to_unique(unique_temperature):
#         if(check_rule(outlook_value, temperature_value)):
#             continue
#         for humidity_value in add_ignore_to_unique(unique_humidity):
#             if(check_rule(outlook_value, temperature_value, humidity_value)):
#                 continue
#             for windy_value in add_ignore_to_unique(unique_windy):
#                 if(check_rule(outlook_value, temperature_value, humidity_value, windy_value)):
#                     continue



# with open("output_rules.txt", "w") as f:
#     list_columns = data.columns
#     number_of_rules = 0
#     for index, rule in enumerate(rules_yes):
#         f.write(
#             f"RULE {index}{rule}"
#         )

#     f.write('=================== \n')
#     f.write('=================== \n')
#     f.write('=================== \n')

#     for index, rule in enumerate(rules_no):
#         f.write(
#             f"RULE {index}{rule}"
#         )

