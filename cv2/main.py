import pandas as pd
import itertools
import numpy as np



data = pd.read_csv("dataset.csv", ",")

empty_string = "empty"


unique_outlook = data['Outlook'].unique()
unique_temperature = data['Temperature'].unique()
unique_humidity = data['Humidity'].unique()
unique_windy = data['Windy'].unique()

def calculate_support(X, Y, input_data):
    filtered_data = input_data
    if X.Outlook != empty_string:
        filtered_data = filtered_data[filtered_data['Outlook'] == X.Outlook]
    if X.Temperature != empty_string:
        filtered_data = filtered_data[filtered_data['Temperature'] == X.Temperature]
    if X.Humidity != empty_string:
        filtered_data = filtered_data[filtered_data['Humidity'] == X.Humidity]
    if X.Windy != empty_string:
        filtered_data = filtered_data[filtered_data['Windy'] == X.Windy]


    total_number_of_transactions = input_data.shape[0]
    transactions_containing_both_x_and_y = filtered_data[filtered_data['Play'] == Y]['Play'].count()
    # print(total_number_of_transactions, transactions_containing_both_x_and_y)
    return transactions_containing_both_x_and_y / total_number_of_transactions


def calculate_confidence(X, Y, input_data):
    filtered_data = input_data
    if X.Outlook != empty_string:
        filtered_data = filtered_data[filtered_data['Outlook'] == X.Outlook]
    if X.Temperature != empty_string:
        filtered_data = filtered_data[filtered_data['Temperature'] == X.Temperature]
    if X.Humidity != empty_string:
        filtered_data = filtered_data[filtered_data['Humidity'] == X.Humidity]
    if X.Windy != empty_string:
        filtered_data = filtered_data[filtered_data['Windy'] == X.Windy]


    transaction_containing_x = filtered_data.shape[0]
    transactions_containing_both_x_and_y = filtered_data[filtered_data['Play'] == Y]['Play'].count()
    if transaction_containing_x == 0:
        return 0
    return transactions_containing_both_x_and_y / transaction_containing_x



class Instance():
    def __init__(self, outlook, temperature, humidity, windy):
        self.Outlook = outlook
        self.Temperature = temperature
        self.Humidity = humidity
        self.Windy = windy
        self.support = {
            'yes': 0,
            'no': 0
        }
        self.confidence = {
            'yes': 0,
            'no': 0
        }
        
        self.calc_confidence()
        self.calc_support()

    def calc_support(self, input_data = data):
        self.support['no'] = calculate_support(self, 'no', input_data) 
        self.support['yes'] = calculate_support(self, 'yes', input_data)

    def calc_confidence(self, input_data = data):
        self.confidence['no'] = calculate_confidence(self, 'no', input_data) 
        self.confidence['yes'] = calculate_confidence(self, 'yes', input_data)

    def __str__(self):
        return f'Instance of {self.Outlook} {self.Temperature} {self.Humidity} {self.Windy} \n Support: [{self.support}] \n Confidence [{self.confidence}] \n'


class Node:
    def __init__(self, parent, children, key, level = 0):
        self.parent = parent
        self.combs_values = []
        self.children = []
        self.key = key
        self.level = level
        self.rules = []
        self.instances_of_rule = []

    def generate_combs(self):
        self.combinations = list(itertools.product(*self.combs_values))
        self.get_max_rules()

    def get_max_rules(self):
        for item in self.combinations:
            vector = construct_vector(item)
            self.instances_of_rule.append(Instance(vector[0], vector[1], vector[2], vector[3]))
            self.rules.append(vector)

    def __str__(self):
        string = f'\nNode on level {self.level}'
        for instance in self.instances_of_rule:
            string += f'\n\t{instance}'
        return string

def construct_vector(vector):
    result = [empty_string] * 4
    for value in vector:
        if(value == "overcast" or value == "rainy" or value == "sunny"):
            result[0] = value
        elif(value == "hot" or value == "cool" or value == "mild"):
            result[1] = value
        elif(value == "high" or value == "normal"):
            result[2] = value
        else:
            result[3] = value
    return result


    
def generate_tree(input_data, input_set, parent):
    children = []

    for index,_ in enumerate(input_set):
        node_last_value_index = index 
        if parent.key >= 0:
            node_last_value_index += parent.key + 1
        new_node = Node(parent, [], node_last_value_index, parent.level + 1)
        if node_last_value_index < len(input_set):
            new_array_combs = parent.combs_values.copy()
            new_array_combs.append(input_set[node_last_value_index])
            new_node.combs_values = new_array_combs
            new_node.generate_combs()
            children.append(new_node)
        if node_last_value_index + 1 < len(input_set):
            generate_tree(input_data, input_set, new_node)
    parent.children = children


root = Node(None, [], -1)

generate_tree(data, [unique_outlook, unique_temperature, unique_humidity, unique_windy], root)




def BFS(root):
    output_string = ''
    queue = []
    queue.append(root)
    number_of_rules = 0
    while queue:
        node = queue.pop(0)
        for child in node.children:
            queue.append(child)
        if node != root:
            number_of_rules += len(node.instances_of_rule)
            output_string += f'{node} \n'
            print(node)

    return output_string
    
out = BFS(root)





with open('output.txt', 'w+') as f:
    f.write(out)