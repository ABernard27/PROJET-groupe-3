#%%
from dataclasses import replace
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from download import download
from pyproj import Proj, transform

pd.options.display.max_rows = 50
#%%
url= 'https://static.data.gouv.fr/resources/gares-de-peage-du-reseau-routier-national-concede/20210224-175626/gares-peage-2019.csv'
path_target = './gares-peage-2019.csv'
download(url, path_target, replace=False)
#%%

data = pd.read_csv("gares-peage-2019.csv",sep=';',usecols=["route","x","y"," Nom gare "])
data=data.loc[(data['route'] == 'A0009') | (data['route']=='A0061') | (data['route']=='A0062')| (data['route']=='A0066')| (data['route']=='A0075')| (data['route']=='A0709')]

data = data.loc[(data['x']=='767254,1') | (data[" Nom gare "]=='SETE                                    ') | (data[" Nom gare "]=='AGDE') | (data[" Nom gare "]=='BEZIERS CABRIALS (ENTReE)') | 
(data[" Nom gare "]=='BEZIERS OUEST') | (data[" Nom gare "]=='NARBONNE EST') | (data[" Nom gare "]=='NARBONNE SUD') | (data[" Nom gare "]=='SIGEAN')
| (data[" Nom gare "]=='LEUCATE') | (data[" Nom gare "]=='PERPIGNAN SUD') | 
(data[" Nom gare "]=='BOULOU (FERMe)') | (data[" Nom gare "]=='LE PERTHUS-LE BOULOU') | (data[" Nom gare "]=='LEZIGNAN') | 
(data[" Nom gare "]=='CARCASSONNE EST') | (data[" Nom gare "]=='CARCASSONNE OUEST') | (data[" Nom gare "]=='BRAM') | (data[" Nom gare "]=='CASTELNAUDARY') | (data[" Nom gare "]=='VILLEFRANCHE DE LAURAGAIS') | 
(data[" Nom gare "]=='NAILLOUX') | (data[" Nom gare "]=='MAZERES') | (data[" Nom gare "]=='PAMIER') | (data[" Nom gare "]=='TOULOUSE SUD-OUEST (ENTREE)') | (data[" Nom gare "]=='TOULOUSE SUD-EST (SORTIE )')
| (data[" Nom gare "]=='PERPIGNAN NORD                          ')]
#%%
data.info(verbose=True)
data.select_dtypes(include=['float64'])
data = data.stack().str.replace(',','.').unstack()
data = data.set_index(np.arange(len(data)))

# transformation des coordonnées lambert93 en coordonnées WGS84

inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')
L93 = np.array([data['x'],data['y']]).T

coord = transform(inProj,outProj,L93[:,0],L93[:,1])
print(coord)
A = list(coord[0])
B = list(coord[1])
A2 = np.asarray(A).reshape(-1,1)
B2 = np.asarray(B).reshape(-1,1)
Coord=np.column_stack([A2,B2])

# source : https://moonbooks.org/Articles/Convertir-des-coordonnees-Lambert-93-en-longitude-et-latitude-avec-python-3/

data['x']=data['x'].replace(np.asarray(data['x']).reshape(-1,1),A2)
data['y']=data['y'].replace(np.asarray(data['y']).reshape(-1,1),B2)

# ajout de Montgiscard qui n'existe pas
L=len(data)
data.loc[L]=['A0061','1.584556','43.461156','MONTGISCARD']
data = data.reindex([0,1,2,23,3,4,5,6,7,8,9,11,10,18,17,16,15,14,13,20,21,22,24,19,12])
data = data.set_index(np.arange(len(data)))
data.to_csv('data.csv')

#%%
# creation dataframe des distances
import requests
import json
DIST = np.zeros((len(data),len(data)))

for i in range(len(data)):
    for j in range(i,len(data)):
        x1,y1=(data['x'][j],data['y'][j])
        x,y=(data['x'][i],data['y'][i])
        r = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")
        r2 = requests.get(f"http://router.project-osrm.org/route/v1/car/{x1},{y1};{x},{y}?overview=false""")
        routes = json.loads(r.content)
        routes2 = json.loads(r2.content)
        route = routes.get("routes")[0]
        route2 = routes2.get("routes")[0]
        DIST[i,j]=min(round(route['distance']/1000),round(route2['distance']/1000))
print(DIST)

# source : https://ichi.pro/fr/distance-parcourue-entre-deux-ou-plusieurs-endroits-en-python-151146835025391

#%%
DIST2 = DIST + DIST.T

DISTANCE = pd.DataFrame(DIST2,columns=['St-Jean-de-Vedas','Sete','Agde Pezenas','Peage de Beziers-Cabrials','Beziers ouest','Narbonne est ',
'Narbonne sud','Sigean ','Leucate','Perpignan nord','Perpignan sud','Le Boulou  (peage sys ferme)','Peage du Perthus','Lezignan',
'Carcassonne est','Carcassonne ouest','Bram','Castelnaudary','Villefranche-de-Lauragais','Nailloux','Mazeres-Saverdun','Peage de pamiers','Montgiscard','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est'])

DISTANCE.index=['St-Jean-de-Vedas','Sete','Agde Pezenas','Peage de Beziers-Cabrials','Beziers ouest','Narbonne est ',
'Narbonne sud','Sigean ','Leucate','Perpignan nord','Perpignan sud','Le Boulou  (peage sys ferme)','Peage du Perthus','Lezignan',
'Carcassonne est','Carcassonne ouest','Bram','Castelnaudary','Villefranche-de-Lauragais','Nailloux','Mazeres-Saverdun','Peage de pamiers','Montgiscard','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est']
DISTANCE.to_csv('Distance.csv')
    
# %%
url = 'https://raw.githubusercontent.com/ABernard27/PROJET-groupe-3/Developpement/Document/tarif.csv'
path_target = "./prix.csv"
download(url, path_target, replace=False)

prix = pd.read_csv("prix.csv", sep=';',usecols=['St-Jean-de-Vedas','Sete','Agde Pezenas','Peage de Beziers-Cabrials','Beziers ouest','Narbonne est ',
'Narbonne sud','Sigean ','Leucate','Perpignan nord','Perpignan sud','Le Boulou  (peage sys ferme)','Peage du Perthus','Lezignan',
'Carcassonne est','Carcassonne ouest','Bram','Castelnaudary','Villefranche-de-Lauragais','Nailloux','Mazeres-Saverdun','Peage de pamiers','Montgiscard','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est'])

prix = prix.drop(prix.index[[0,1,2,3,5,18,29,30,33,34,35,36,37,38,39,40,41,42]])
prix.index=['St-Jean-de-Vedas','Sete','Agde Pezenas','Peage de Beziers-Cabrials','Beziers ouest','Narbonne est ',
'Narbonne sud','Sigean ','Leucate','Perpignan nord','Perpignan sud','Le Boulou  (peage sys ferme)','Peage du Perthus','Lezignan',
'Carcassonne est','Carcassonne ouest','Bram','Castelnaudary','Villefranche-de-Lauragais','Nailloux','Mazeres-Saverdun','Peage de pamiers','Montgiscard','Peage de Toulouse sud/ouest','Peage de Toulouse sud/est']

prix.to_csv('Prix.csv')
