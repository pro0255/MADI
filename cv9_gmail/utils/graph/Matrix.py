import numpy as np

class Vertex():
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.degree = 0

    def __str__(self):
        return f'Vertex id [{self.id}], degree [{self.degree}], edges [{self.edges}]'


class AdjacencyMatrix():
    def __init__(self, size, data):
        self.matrix = np.zeros((size, size))
        self.create(data)
    
    def create(self, data):
        for row_index in range(data.shape[0]):
            row = data.iloc[row_index, :]
            self.matrix[row[0]-1, row[1]-1] += 1
            self.matrix[row[1]-1, row[0]-1] += 1


    def __str__(self):
        output = ""
        for index, row in enumerate(self.matrix):
            degree = np.sum(row == 1)
            vertex_id = index + 1
            output += f"Id: {vertex_id} - stupen {degree}\n" 
        return output



class AdjacencyList():
    def __init__(self, data):
        self.dic = {}
        self.create(data)
        self.all_degres = []
        for vertex in self.dic.values():
            self.all_degres.append(vertex.degree)

    def add_to_dict(self, tuple):
        if tuple[0] in self.dic:
            vertex = self.dic[tuple[0]]
            vertex.degree += 1
            vertex.edges.append(tuple[1])
        else:
            new_vertex = Vertex(tuple[0])
            new_vertex.degree += 1
            new_vertex.edges.append(tuple[1])
            self.dic[tuple[0]] = new_vertex


    def create(self, data):
        for row_index in range(data.shape[0]):
            row = data.iloc[row_index, :]
            self.add_to_dict((row[0], row[1]))
            self.add_to_dict((row[1], row[0]))

    def find_max(self):
        vertex_max = Vertex(-1)
        for item in self.dic.items():
            if vertex_max.degree < item[1].degree:
                vertex_max = item[1]
        return f'Max degree is {vertex_max.degree}'

    def find_min(self):
        vertex_min = None
        for item in self.dic.items():
            if not vertex_min:
                vertex_min = item[1]
                continue
            if vertex_min.degree > item[1].degree:
                vertex_min = item[1]
        return f'Min degree is {vertex_min.degree}'

    def find_average(self):
        degree_count = 0
        for item in self.dic.items():
            degree_count += item[1].degree

        return f'Average is {degree_count/len(self.dic)}'

    def print_values(self):
        print(self.find_min())
        print(self.find_max())
        print(self.find_average())

    def __str__(self):
        output = ""
        for vertex in self.dic.values():
            output += f'{vertex}\n'
        return output