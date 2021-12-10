
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import seaborn as sns
import time
from ipywidgets import interact
import Coberny as cyb



class distribution(object):
    """Après excution du code, c'est dans votre fenêtre interactive que vous trouverez les widgets (les menus déroulants) qui vous permettront qui modifier l'entrée et la sortie à votre souhait.\n 
    
    :param dataframe Distance: Le dataframe des distances entre chaque sortie.
    :param dataframe Prix: Le dataframe des prix entre chaque sortie.
    
    .. warning:: 
    
        Les dataframes Distance et Prix doivent avoir le même nombre de lignes que de colonnes.\n
        Le nom des colonnes et des lignes du dataframe Prix doivent être les noms des villes.\n
        Les colonnes du dataframe Distance doivent être le nom des villes, et les lignes doivent être indicées de 0 à n-1, avec n qui est égale au nombre de villes du dataframe.\n
    
    """
    def __init__(self,Distance,Prix):
        self.Distance = Distance
        self.Prix = Prix

    
    # Plot le KDE: la distribution
    def Graph(self):
        """ Trace le graphe du Kernel Density Estimate (KDE): l'estimation de la fonction de densité de la variable prix/kilomètre sur la portion d'autoroute entre l'entrée et la sortie choisie.\
Le bar plot des prix au kilomètre entre chaque portion de l'autoroute.

        .. warning::
        
            Il n'y a pas de paramètre à rentrer en entrée de la fonction Graph.
            
       
        .. code:: 
    
            Coberny.distribution(DISTANCE, prix).Graph()
        
        """
        villes = sorted(self.Prix.columns.unique())
        start4 = time.time()

        def kde_explore(bw=0.2, Entrée=villes, Sortie=villes):

            G = nx.Graph(self.Prix)
            G.add_nodes_from(self.Prix)
            G = nx.Graph(incoming_graph_data=self.Prix)
            a = nx.minimum_spanning_tree(G, ignore_nan=True)
            # Graphe du chemin le plus court
            A = nx.shortest_path(a, Entrée, Sortie)
            B = nx.subgraph(a, A)
            nx.draw(B,with_labels= True)

            DISTKM = np.zeros(len(A)-1)
            for i in range(len(A)-1):
                if(self.Distance[A[i]][cyb.indice(A[i+1],self.Distance)] != 0):
                    DISTKM[i] = (self.Prix[A[i]][A[i+1]])/(self.Distance[A[i]][cyb.indice(A[i+1],self.Distance)])
                else: DISTKM[i] = 0  
            fig, ax = plt.subplots(1, 1, figsize=(5, 5))
            sns.kdeplot(y=DISTKM, bw_adjust=bw, shade=True, vertical=True, cut=0, ax=ax, color='orange')
            plt.xlabel('Trajet')
            plt.ylabel('Prix au kilomètre')
            plt.title("Distribution des prix")
            plt.tight_layout()
            plt.show()
   
        interact(kde_explore, bw=(0.001, 2, 0.01), Entrée=villes, Sortie=villes)

        # Plot un diagramme en baton sur le prix/km par portion


        def barplot(Entrée=villes, Sortie=villes):
            G = nx.Graph(self.Prix)
            G.add_nodes_from(self.Prix)
            G = nx.Graph(incoming_graph_data=self.Prix)
            a = nx.minimum_spanning_tree(G, ignore_nan=True)
            # Graphe du chemin le plus court
            A = nx.shortest_path(a, Entrée , Sortie)
            B = nx.subgraph(a,A)

            DISTKM = np.zeros(len(A)-1)
            for i in range(len(A)-1):
                if(self.Distance[A[i]][cyb.indice(A[i+1],self.Distance)] != 0):
                    DISTKM[i] = (self.Prix[A[i]][A[i+1]])/(self.Distance[A[i]][cyb.indice(A[i+1],self.Distance)])
                elif(self.Distance[A[i]][cyb.indice(A[i+1],self.Distance)] == 0): 
                    DISTKM[i] = 0 
            height = DISTKM
            width = 1
            P = np.arange(len(A)-1)
            x = P
            plt.title("Prix au kilomètre")
            plt.bar(x, height, width, color='orange', alpha=0.3, align='edge', edgecolor='orange', linewidth=3)
            plt.xticks(np.arange(len(A)), A, rotation=75)

        interact(barplot, Entrée=villes, Sortie=villes)
        end4 = time.time()   
        print("Temps passé pour exécuter la commande: {0:.5f} s.".format(end4 - start4))
        return 


