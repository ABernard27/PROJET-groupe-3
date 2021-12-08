# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:35:17 2021

@author: olivi
"""

import pandas as pd
import networkx as nx
from networkx.algorithms import dijkstra_path
import itertools
import time
import datetime as dt
import matplotlib.pyplot as plt


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
                col_index = data.columns.get_loc(tup[elt+1])
                listOfEdges.append(
                    (tup[elt], tup[elt + 1], data.iloc[row_index,col_index])
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

# Cette fonction calcule la somme totale des poids du chemin
def weight(data, n_uplet):
        cities = data.columns[0]
        listOfWeights = []
        for i in range(len(n_uplet) - 1):
            row_index = int(data[data[cities] == n_uplet[i]].index[0])
            col_index = data.columns.get_loc(n_uplet[i+1])
            w = df_price.iloc[row_index, col_index]
            listOfWeights.append(w)
        return sum(listOfWeights)

# Cette fonction retourne le chemin optimal dans un n-uplet    
def FindBestPathForPriceV2(data, listOfTuple):
    tupWeights = []
    for tup in listOfTuple:
        tp_w = weight(data, tup)
        tupWeights.append(tp_w)
    min_w = min(tupWeights)
    min_w_index = tupWeights.index(min_w)
    bestPathForPrice = listOfTuple[min_w_index]
    return bestPathForPrice

# Retourne le couple composé du chemin optimal et du prix final (minimal)
# que l'on va payer en empruntant ce cheminpour aller de la ville de 
# départ à celle d'arrivée

def FindBestPathForPrice(data, entrance, outlet, k):
    """affiche la liste composé des sommets du chemin optimal 
    (le chemin qui revient le moins cher entre la ville de départ et celle d'arrivée)
    et le prix total (minimal) que
    l'utilisateur va payer en empruntant ce chemin
    
    :param pandas.core.frame.DataFrame data: Le dataframe donnant le prix
    du trajet direct entre 2 villes. Chaque case du dataframe correspond au prix que l'on va payer 
    entre la ville associée à l'indice de la ligne et la ville associée à
    l'indice de la colonne dans le dataframe.

    ..warning::

        Attention! le dataframe doit avoir un format adéquat pour que l'algorithme
        fonctionne, une rubrique détaillant le format attendu pour le dataframe
        est diposnible

    :param str entrance: La ville de départ
    :param str outlet: La ville de sortie
    :param int k: Contrainte du nombre de sorties maximales imposées par l'utilisateur
    
    returns: Un couple. Le 1er element du couple est la liste des sommets du
    chemin optimal. Le 2ème élément du couple est le prix total (minimal) que
    l'utilisateur va payer en empruntant ce chemin'
    """
    if k > GetKMaxConstraint(data, entrance, outlet):
        ans = 'La contrainte k est supérieure au nombre maximal de sorties possibles'
        return ans
    else:
        listOfSP = []
        listOfSPWeight = []
        for i in range(k+1):
            G = CreateGraphOfPath(data, entrance, outlet, i)
            listOfSP.append(FindShortestPath(G, entrance, outlet))
            listOfSPWeight.append(ShortestPathWeight(G, entrance, outlet))
        best_price = min(listOfSPWeight)
        best_price_index = listOfSPWeight.index(best_price)
        bestPathForPrice = listOfSP[best_price_index]
        if len(bestPathForPrice) <= 2+k:
            return (bestPathForPrice, best_price)
        else:
            listOfTuple = GetListOfPath(data, entrance, outlet, k)
            bestTupleForPrice = FindBestPathForPriceV2(data, listOfTuple)
            best_price = weight(data, bestTupleForPrice)
            bestPathForPrice = list(bestTupleForPrice)
            return (bestPathForPrice, best_price)

# Retourne le graph du chemin optimal ie le chemin qui revient le moins cher
# entre la ville de départ et celle d'arrivée
# Les sorties intermédiraires sont coloriées en orange
# La ville de départ et d'arrivée sont coloriées en bleu
def CreateGraphOfBestPathForPrice(data, entrance, outlet, k):
    """Trace le graph du chemin optimal ie le chemin qui revient le moins cher
    entre la ville de départ et celle d'arrivée


    :param pandas.core.frame.DataFrame data: Le dataframe donnant le prix
    du trajet direct entre 2 villes. Chaque case du dataframe correspond au prix que l'on va payer 
    entre la ville associée à l'indice de la ligne et la ville associée à
    l'indice de la colonne dans le dataframe.

    ..warning::

        Attention! le dataframe doit avoir un format adéquat pour que l'algorithme
        fonctionne, une rubrique détaillant le format attendu pour le dataframe
        est diposnible

    :param str entrance: La ville de départ
    :param str outlet: La ville de sortie
    :param int k: Contrainte du nombre de sorties maximales imposées par l'utilisateur

    returns: Le graphe du chemin optimal entre la ville de départ et celle d'arrivée
    """
    if k > GetKMaxConstraint(data, entrance, outlet):
        ans = 'La contrainte k est supérieure au nombre maximal de sorties possibles'
        return ans
    else:
        cities = data.columns[0]
        listOfNodesColors = []
        listOfEdges = []
    #    d_edges_labels = {}
        G_bestPath = nx.DiGraph()
        couple = FindBestPathForPrice(data, entrance, outlet, k)
        bestPathForPrice = couple[0]
        for node in bestPathForPrice:
            if (node != entrance) and (node != outlet):
                listOfNodesColors.append('tab:orange')
            else:
                listOfNodesColors.append('tab:blue')
        G_bestPath.add_nodes_from(bestPathForPrice)
        for vx in range(len(bestPathForPrice)-1):
            row_index = int(data[data[cities] == bestPathForPrice[vx]].index[0])
            col_index = data.columns.get_loc(bestPathForPrice[vx+1])
            listOfEdges.append(
                (bestPathForPrice[vx], bestPathForPrice[vx+1], data.iloc[row_index,col_index])
                )
            # d_edges_labels[(str(bestPathForPrice[vx]), str(bestPathForPrice[vx+1]))] = str(
            #     data.iloc[row_index,col_index]
            #     )
        G_bestPath.add_weighted_edges_from(listOfEdges)
        nx.draw(G_bestPath, node_color = listOfNodesColors, with_labels = True)
        plt.show()
        # nx.draw_networkx_edge_labels(G_bestPath, nx.spring_layout(G_bestPath, seed=3113794652),
        #                               edge_labels = d_edges_labels)


if __name__ == '__main__':
    df_price = pd.read_csv('prix.csv')
    df_price = df_price.fillna(0)
    startTime = time.time()
    print('Couple meilleur chemin et prix: ', FindBestPathForPrice(df_price,
                                            'Sete', 'Montgiscard', 5))
    CreateGraphOfBestPathForPrice(df_price, 'Sete', 'Montgiscard', 5)
    runTime = time.time() - startTime
    roundRunTime = str(dt.timedelta(seconds=runTime))
    print("Le temps d'execution du programme vaut: ", runTime, ' secondes.\n cad '
          , roundRunTime, " dans le format heures minutes secondes")
         
