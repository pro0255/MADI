from parse_gmail.GmailParser import GmailParser
from constants.CONSTANTS import PATH_TO_FILE, INSPECTION_OUTPUT, GEPHI_OUTPUT
from utils.graph.GraphProperties import make_graph_inspection
from printer.GraphInspectionPrinter import write_graph_inspection_to_file
import networkx as nx

parser = GmailParser()
emails, emails_adj_matrix, emails_dic = parser.parse(PATH_TO_FILE)


network_labels = {v:{"label":k} for k,v in emails_dic.items()}


inspection = make_graph_inspection(emails_adj_matrix)
write_graph_inspection_to_file(INSPECTION_OUTPUT, inspection)

G = nx.from_numpy_matrix(emails_adj_matrix)
nx.set_node_attributes(G, network_labels)
nx.write_gexf(G, GEPHI_OUTPUT)