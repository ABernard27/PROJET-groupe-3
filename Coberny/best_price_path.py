# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:35:17 2021

@author: olivi
"""

import pandas as pd
import networkx as nx
from networkx.algorithms import dijkstra_path
import itertools

df_price = pd.read_csv('prix.csv')
df_price = df_price.fillna(0)

# Retourne la liste de toutes les villes du dataframe
def GetListOfcolnames(data):
    listofColnames = list(data.columns)[1:]
    return listofColnames

# Retourne la liste de tous les sommets des chemins possibles entre
# la ville de départ (entrance) et la ville d'arrivée (outlet)
def GetListOfVertexPath(data, entrance, outlet):
    listofColnames = GetListOfcolnames(data)
    outlet_index = listofColnames.index(outlet)
    listOfVertexPath = listofColnames[0:outlet_index+1]
    return listOfVertexPath

# Retourne la liste de toutes les sorties possibles entre
# la ville de départ (entrance) et la ville d'arrivée (outlet)
def GetListOfPossibleExit(data, entrance, outlet):
    listOfVertexPath = GetListOfVertexPath(data, entrance, outlet)
    listOfExit = [e for e in listOfVertexPath if (e != entrance and e != outlet)]
    return listOfExit

# Retourne la contrainte K qui correspond au nombre total de sorties
# qu'on peut emprunter entre la ville de départ (entrance) et 
# la ville d'arrivée (outlet)
def GetKMaxConstraint(data, entrance, outlet):
    k = len(GetListOfPossibleExit(data, entrance, outlet))
    return k

# Retourne la liste de tous les chemins qu'on peut emprunter en fonction
# du nombre de sorties (nbr_exit) utilisé entre la ville de départ
# et celle d'arrivée
def GetListOfPath(data, entrance, outlet, nbr_exit):
    listOfExit = GetListOfPossibleExit(data, entrance, outlet)
    listOfPath = list(itertools.combinations(listOfExit, nbr_exit))
    for i in range(len(listOfPath)):
        listOfPath[i] = (entrance,) + listOfPath[i] + (outlet,)
    return listOfPath

# Création du graph représentant tous les itinéraires qu'on peut 
# emprunter (entre la ville de départ et celle d'arrivée)
# en fonction du nombre de sorties (nbr_exit) utilisé 
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
        listOfVertexPath = GetListOfVertexPath(data, entrance, outlet)
        G_nbr_exit.add_nodes_from(listOfVertexPath)
        listOfEdges = []
        listOfPath = GetListOfPath(data, entrance, outlet, nbr_exit)
        for tup in listOfPath:
            for elt in range(len(tup) - 1):
                row_index = int(data[data[cities] == tup[elt]].index[0])
                col_index = df_price.columns.get_loc(tup[elt+1])
                listOfEdges.append(
                    (tup[elt], tup[elt + 1], df_price.iloc[row_index,col_index])
                    )
        G_nbr_exit.add_weighted_edges_from(listOfEdges)
    return G_nbr_exit

# Retourne la liste des noeuds du plus court chemin trouvé dans le graph G
def FindShortestPath(G, entrance, outlet):
    listOfSPNodes = dijkstra_path(G, entrance, outlet)
    return listOfSPNodes

# Retourne la somme des poids du plus court chemin
def ShortestPathWeight(G, entrance, outlet):
    listOfSPNodes = FindShortestPath(G, entrance, outlet)
    w = 0
    for elt in range(len(listOfSPNodes)-1):
        d = G.get_edge_data(listOfSPNodes[elt], listOfSPNodes[elt+1])
        w += d['weight']
    return w

def FindBestPathForPrice(data, entrance, outlet):
    K = GetKMaxConstraint(data, entrance, outlet)
    listOfSP = []
    listOfSPWeight = []
    for i in range(K+1):
        G = CreateGraphOfPath(data, entrance, outlet, i)
        listOfSP.append(FindShortestPath(G, entrance, outlet))
        listOfSPWeight.append(ShortestPathWeight(G, entrance, outlet))
    best_price = min(listOfSPWeight)
    best_price_index = listOfSPWeight.index(best_price)
    bestPathForPrice = listOfSP[best_price_index]
    return (bestPathForPrice, best_price)