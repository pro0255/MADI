from graph_api.GraphMaker import GraphMaker 

def run_graph_maker(graph_inspection, directory, prefix=""):
    graph_maker = GraphMaker(graph_inspection)
    graph_maker.plot_components_distribution(directory)
    graph_maker.plot_degree_distribution(directory)
    graph_maker.plot_graph(directory)