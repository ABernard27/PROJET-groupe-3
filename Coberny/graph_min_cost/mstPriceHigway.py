# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:11:08 2021

@author: olivi
"""

import networkx as nx
import pandas as pd
from networkx.algorithms import tree

df_price = pd.read_csv('prix.csv')
df_price = df_price.fillna(0)
listofColnames = list(df_price.columns)[1:]

G = nx.Graph()
G.add_nodes_from(listofColnames)


for i in listofColnames:
    for j in listofColnames:
        if i != j:
            row_index = int(df_price[df_price["Unnamed: 0"] == i].index[0])
            col_index = df_price.columns.get_loc(j)
            G.add_weighted_edges_from([(i, j, df_price.iloc[row_index,col_index])])
            
#nx.draw(G, with_labels=True)

mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
edgelist = list(mst)
G_mst = nx.Graph()
G_mst.add_nodes_from(listofColnames)
G_mst.add_edges_from(edgelist)
nx.draw(G_mst, with_labels=True)

# listOfNodes = ["n"+str(i) for i in range(5)]

# G.add_edges_from([("n0","n1"), ("n0","n4"), ("n1","n2"), ("n2","n3"),
#                   ("n3","n4"), ("n4","n2"), ("n0", "n2")])
# G.add_edge(0,3,weight=2)
# G.add_nodes_from(listOfNodes)
# G.add_edges_from([(0, 1), (1, 3), (2, 4), (5, 0)])
# nx.draw(G, with_labels = True)