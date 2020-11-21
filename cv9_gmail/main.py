from parse_gmail.GmailParser import GmailParser
from constants.CONSTANTS import PATH_TO_FILE, INSPECTION_OUTPUT
from utils.graph.GraphProperties import make_graph_inspection
from printer.GraphInspectionPrinter import write_graph_inspection_to_file


parser = GmailParser()
emails, emails_adj_matrix, emails_dic = parser.parse(PATH_TO_FILE)

inspection = make_graph_inspection(emails_adj_matrix)
write_graph_inspection_to_file(INSPECTION_OUTPUT, inspection)

