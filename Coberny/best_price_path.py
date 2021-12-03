# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:35:17 2021

@author: olivi
"""

import pandas as pd
import networkx as nx
import itertools

df_price = pd.read_csv('prix.csv')
df_price = df_price.fillna(0)

# Retourne la liste de toutes les villes du dataframe
def GetListOfcolnames(data):
    listofColnames = list(data.columns)[1:]
    return listofColnames

# Retourne la liste de tous les sommets des chemins possibles entre
# la ville de départ (entrance) et la ville d'arrivée (outlet)
def GetListOfVertexPath(entrance, outlet):
    listofColnames = GetListOfcolnames(df_price)
    outlet_index = listofColnames.index(outlet)
    listOfVertexPath = listofColnames[0:outlet_index+1]
    return listOfVertexPath

# Retourne la liste de toutes les sorties possibles entre
# la ville de départ (entrance) et la ville d'arrivée (outlet)
def GetListOfPossibleExit(entrance, outlet):
    listOfVertexPath = GetListOfVertexPath(entrance, outlet)
    listOfExit = [e for e in listOfVertexPath if (e != entrance and e != outlet)]
    return listOfExit

# Retourne la contrainte K qui correspond au nombre total de sorties
# qu'on peut empreinter entre la ville de départ (entrance) et 
# la ville d'arrivée (outlet)
def GetKMaxConstraint(entrance, outlet):
    k = len(GetListOfPossibleExit(entrance, outlet))
    return k

# Retourne la liste de tous les chemins qu'on peut empreinter en fonction
# du nombre de sorties (nbr_exit) utilisées entre la ville de départ
# et celle d'arrivée
def GetListOfPath(entrance, outlet, nbr_exit):
    listOfExit = GetListOfPossibleExit(entrance, outlet)
    listOfPath = list(itertools.combinations(listOfExit, nbr_exit))
    for i in range(len(listOfPath)):
        listOfPath[i] = (entrance,) + listOfPath[i] + (outlet,)
    return listOfPath

def CreateGraphOfPath(data, entrance, outlet, nbr_exit):
    G_nbr_exit = nx.DiGraph()
    cities = data.columns[0]
    if nbr_exit == 0:
        G_nbr_exit.add_nodes_from([entrance, outlet])
        row_index = int(data[data[cities] == entrance].index[0])
        col_index = data.columns.get_loc(outlet)
        G_nbr_exit.add_weighted_edges_from(
            [(entrance, outlet, data.iloc[row_index,col_index])]
            )
    else:
        listOfVertexPath = GetListOfVertexPath(entrance, outlet)
        G_nbr_exit.add_nodes_from(listOfVertexPath)
        listOfEdges = []
        listOfPath = GetListOfPath(entrance, outlet, nbr_exit)
        for tup in listOfPath:
            for elt in range(len(tup) - 1):
                row_index = int(data[data[cities] == tup[elt]].index[0])
                col_index = df_price.columns.get_loc(tup[elt+1])
                listOfEdges.append(
                    (tup[elt], tup[elt + 1], df_price.iloc[row_index,col_index])
                    )
        G_nbr_exit.add_weighted_edges_from(listOfEdges)
    return G_nbr_exit
    