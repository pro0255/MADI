import pandas as pd
import itertools
import numpy as np

## 16.9.2020
result = list()

data = pd.read_csv("dataset.csv", ",")

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
    # print(output)


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
#         filtered_data = filtered_data[filtered_data['Windy'] == windy]
#     number_of_no = filtered_data[filtered_data['Play'] == 'no']['Play'].count()
#     number_of_yes =  filtered_data[filtered_data['Play'] == 'yes']['Play'].count()


    # if outlook == 'rainy' and windy != emptyString:
    #     print(outlook, temperature, humidity, windy, number_of_no, number_of_yes)
    #     print(windy)
    #     x = data[data['Outlook'] == outlook]
    #     x = x[x['Windy'] == windy]
    #     print(x)


#     if number_of_no == 0 and number_of_yes == 0:
#         return False
#     elif number_of_no == 0:
#         write_rule({'outlook': outlook, 'temperature': temperature, 'humidity': humidity, 'windy': windy}, 'yes', number_of_yes)
#         return True
#     elif number_of_yes == 0:
#         write_rule({'outlook': outlook, 'temperature': temperature, 'humidity': humidity, 'windy': windy}, 'no', number_of_no)
#         return True
#     return False



# def construct_vector(vector):
#     result = [emptyString] * 4
#     for value in vector:
#         if(value == "overcast" or value == "rainy" or value == "sunny"):
#             result[0] = value
#         elif(value == "hot" or value == "cool" or value == "mild"):
#             result[1] = value
#         elif(value == "high" or value == "normal"):
#             result[2] = value
#         else:
#             result[3] = value
#     return result
            


# class Node:
#     def __init__(self, parent, children, key, level = 0):
#         self.parent = parent
#         self.combs_values = []
#         self.children = []
#         self.key = key
#         self.level = level
#         self.rules = []

#     def generate_combs(self):
#         self.combinations = list(itertools.product(*self.combs_values))
#         self.get_max_rules()

#     def get_max_rules(self):
#         for item in self.combinations:
#             vector = construct_vector(item)
#             self.rules.append(vector)







# def generate_tree(input_data, input_set, parent):
#     children = []

#     for index,_ in enumerate(input_set):
#         node_last_value_index = index 
#         if parent.key >= 0:
#             node_last_value_index += parent.key + 1
#         new_node = Node(parent, [], node_last_value_index, parent.level + 1)
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

# black_list = []
# def check_black_list(input_value):
#     isAbstract = True
#     #subset smaller or equal
#     for item in black_list:
#         counter = 0
#         for i in range(len(item)):
#             if item[i] == emptyString:
#                 counter += 1
#             elif item[i] == input_value[i]:
#                 counter += 1
#         if counter == len(item):
#             return False
#     return isAbstract

    
# def iterate_rules_in_node(node):
#     # print(node.level)
#     for rule in node.rules:
#         if(check_black_list(rule) and check_rule(rule[0], rule[1], rule[2], rule[3]) ):
#             black_list.append(rule)


# queue = []
# def BFS(root):
#     queue.append(root)

#     while queue:
#         node = queue.pop(0)
#         for child in node.children:
#             queue.append(child)
#         if node != root:
#             iterate_rules_in_node(node)
        



# BFS(root)
# print(black_list)




# def iterate_node(node):
#     for item in node.children:
#         print(item.level)
#         for rule in item.rules:
#             if(check_rule(rule[0], rule[1], rule[2], rule[3]) and check_black_list(rule)):
#                 black_list.append(rule)
#         iterate_node(item)






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















# def fuck_find(vector):
#     for enum_index,column_unique in enumerate(vector):
#         for value_in_vector in column_unique:
#             values = construct_vector([value_in_vector])
#             if check_rule(values[0], values[1], values[2], values[3]):
#                 continue
#             for i in range(enum_index + 1, len(vector)):
#                 vector_for_combination = vector[i]
#                 combinations = list(itertools.product(*[[value_in_vector], vector_for_combination]))
#                 for combination in combinations:
#                     values2 = construct_vector(combination)
#                     check_rule(values2[0], values2[1], values2[2], values2[3])
#                Kk # print(value_in_vector, vector_for_combination)
#             #  print(index_unique, column_unique)




# fuck_find([unique_outlook, unique_temperature, unique_humidity, unique_windy])

# print(len(rules_yes))
# for yes in rules_yes: 
#     print(yes)
# print('=================')
# for no in rules_no:
#     print(no)


# print('=================')
# for i, item in enumerate(black_list):
#     print(i, item)


