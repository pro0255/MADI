

def create_graph_inspections_string(graph_inspection):
    print(graph_inspection)


def print_graph_inspection(graph_inspection):
    print(create_graph_inspections_string(graph_inspection))


def write_graph_inspection_to_file(path, graph_inspection, des):
    final = f'{des} \n {graph_inspection}'
    with open(path, 'w') as f:
        f.write(final)    