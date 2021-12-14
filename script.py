#%%
import Coberny as cyb
import numpy as np
import pandas as pd
from download import download
#%%
#Téléchargement des dataframes 
url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/master/Document/Distance.csv'
path_target = "./Distance.csv"
download(url, path_target, replace = True)
Distance = pd.read_csv('Distance.csv', sep = ',')

url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/master/Document/Prix.csv'
path_target = "./Prix.csv"
download(url, path_target, replace = True)
Prix = pd.read_csv('Prix.csv', sep = ',')
Prix.fillna(0, inplace=True)
Prix.index=['St-Jean-de-Vedas','Sete','Agde Pezenas','Peage de Beziers-Cabrials','Beziers ouest','Narbonne est ',
'Narbonne sud','Sigean ','Leucate','Perpignan nord','Perpignan sud','Le Boulou  (peage sys ferme)','Peage du Perthus','Lezignan',
'Carcassonne est','Carcassonne ouest','Bram','Castelnaudary','Villefranche-de-Lauragais','Nailloux','Mazeres-Saverdun','Peage de pamiers','Montgiscard','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est']
Prix.drop('Unnamed: 0',1,inplace=True)

url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/master/Document/data.csv'
path_target = "./data.csv"
download(url, path_target, replace = True)
data = pd.read_csv('data.csv', sep = ',')

url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/master/Document/highway_price.csv'
path_target = "./highway_price.csv"
download(url, path_target, replace = True)
Price = pd.read_csv('highway_price.csv')
Price.fillna(0,inplace=True)

url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/master/Document/Prix_map.csv'
path_target = "./Prix_map.csv"
download(url, path_target, replace = True)
Prix_map = pd.read_csv('Prix_map.csv', sep = ',')

#%%
#Affichage de la carte intéractive
key='5b3ce3597851110001cf6248dfd20bf8793e4e978b4bb0ca383bfd55'
cyb.carte(np.column_stack([data['x'],data['y']]),data[' Nom gare '],key,Prix_map)

#Affichage de la distribution des prix 
cyb.distribution(Distance, Prix).Graph()

# %%
#Lancement de l'interface utilisateur 
# Lorsque la fenêtre de l'interface utilisateur s'ouvrira
# Il vous sera demandé de choisir un fichier csv.
# Il faut choisir le fichier csv des Prix c'est à dire le fichier intitulé "highway_price.csv"
app = cyb.AppFindBestPathForPrice.UI()
app.win.mainloop()
