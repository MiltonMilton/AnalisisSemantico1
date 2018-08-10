
from tree import build_graph
from Graph import Graph
import Tkinter

def graph_builder(nombre, concepto, nivel):
    graph_nodes = build_graph(concept=concepto, name=nombre)
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
            to_g.append(v)
            values_g.append(1)
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
    G = nx.from_pandas_dataframe(df, 'from', 'to')

    nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)
    plt.show()


NAME =  "Support_vector_machine"
BASE_RESOURCE = "http://dbpedia.org/resource/Support_vector_machine"
graph_builder(NAME, BASE_RESOURCE, 5)
graficar()