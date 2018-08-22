
from tree import build_graph
from graphGenerator import get_graph
from Graph import Graph
import Tkinter

def graph_builder(nombre, nivel):
    graph_nodes = get_graph(nombre, nivel)
    dic = {}
    from_g = []
    to_g = []
    values_g = []
    ids = []
    for l, v in enumerate(graph_nodes):
        dic.update(v)

    for key in dic.keys():
        ids.append(key)
        values_g.append(0)
        for l, v in enumerate(dic[key]):
            from_g.append(key)
            to_g.append(v.get("nombre"))
            values_g.append(v.get("relacion"))
            ids.append(key)

    graficar(from_g, to_g)
    #graph = Graph(dic)
    #print(graph.edges())

    return None

def graficar(from_g, to_g):
    # libraries
    import pandas as pd
    import numpy as np
    import networkx as nx
    import matplotlib.pyplot as plt

    # Build a dataframe with 4 connections
    df = pd.DataFrame({'from': from_g, 'to': to_g})
    df

    # Build your graph
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    nx.draw(G, with_labels=True, node_size=50, node_color="skyblue",cmap=plt.cm.Blues, node_shape="s", alpha=0.5, linewidths=40)
    plt.show()


NAME =  "Support_vector_machine"
BASE_RESOURCE = "http://dbpedia.org/resource/Mathematics"
graph_builder(NAME, 1)