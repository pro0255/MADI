from utils.graph.GraphProperties import make_graph_inspection
from printer.GraphInspectionPrinter import write_graph_inspection_to_file
from utils.graph.GenerateGraph import generate_random_graph


###############################################################
###############################################################
###############################################################
def run_lab_where_generating_graphs():
    """ Vygenerujte 3 náhodné grafy s parametry n=5550 (počet vrcholů) a pravděpodobností p,
        kterou nastavíte tak, aby Vám průměrný stupeň vyšel menší než 1, roven 1 a větší než 1. Na
        těchto sítích určete všechny vlastnosti, které v tuto chvíli určit umíte (tj. souvislost (počet
        komponent souvislosti (distribuce velikosti komponent souvislosti) a velikost největší
        komponenty souvislosti), průměr, průměrná vzdálenost (průměr přes jednotlivé komponenty
        souvislosti), shlukovací koeficient a distribuce stupňů).
    """
    print('==========GRAPH OUTPUTS===========')
    N = 200
    p1 = 0.00501
    p2 = 0.1
    p3 = 0.000501

    g1 = generate_random_graph(N, p1) #degree == 1
    g2 = generate_random_graph(N, p2) #degree > 1
    g3 = generate_random_graph(N, p3) #degree < 1

    g1_i = make_graph_inspection(g1)
    g2_i =  make_graph_inspection(g2)
    g3_i = make_graph_inspection(g3)

    write_graph_inspection_to_file('graph_equal_1.txt', g1_i, f'N={N} p={p1}\n========================\n')
    write_graph_inspection_to_file('graph_equal_2.txt', g2_i, f'N={N} p={p2}\n========================\n')
    write_graph_inspection_to_file('graph_equal_3.txt', g3_i, f'N={N} p={p3}\n========================\n')

    return ((g1, g1_i), (g2, g2_i), (g3, g3_i))
###############################################################
###############################################################
###############################################################