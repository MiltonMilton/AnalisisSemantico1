

from graphGenerator import get_graph
from Graph import find_path, find_all_paths, find_shortest_path
import Tkinter
#NAME = "SciPy"

def graph_builder(nombre, nivel):
    graph_nodes = get_graph(nombre, nivel)
    dic = {}
    from_g = []
    to_g = []
    values_g = []
    ids = []
    for l, v in enumerate(graph_nodes):
        dic.update(v)

    #print(find_path(dic, NAME, "Machine_learning"))
    for key in dic.keys():
        ids.append(key)
        values_g.append(0)
        for l, v in enumerate(dic[key]):
            from_g.append(key)
            to_g.append(v.get("nombre"))

    #graficar(from_g, to_g, nombre)

    return dic

def graficar(from_g, to_g, nombre):
    # libraries
    import pandas as pd
    import networkx as nx
    import matplotlib.pyplot as plt

    # Build a dataframe with 4 connections
    df = pd.DataFrame({'from': from_g, 'to': to_g})
    df

    # Build your graph
    G = nx.from_pandas_dataframe(df, 'from', 'to')

    nx.draw(G, with_labels=True, node_size=50, node_color="skyblue",cmap=plt.cm.Blues, node_shape="s", alpha=0.5, linewidths=40)
    plt.savefig("{0}.png".format(nombre), format="PNG")

#BASE_RESOURCE = "http://dbpedia.org/resource/Support_vector_machine"
#graph_builder(NAME, 3)