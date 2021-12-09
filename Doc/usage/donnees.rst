Données à titre d'exemple
=========================

Voici un extrait des données que nous avons utilisé pour illustrer les fonctions du package. Vous pouvez les retrouver également sur le lien suivant : https://github.com/ABernard27/PROJET-groupe-3.git


Un extrait du tableau des distances
--------------------------------------

.. figure:: distance.png
   :width: 600
   :align: center

\

Le tableau des distances doit être symétrique (donc carré) et les noms des colonnes et des indices doivent être identiques.

\


Un extrait du tableau des prix
-------------------------------

.. figure:: prix.png
   :width: 600
   :align: center

\

Le tableau des prix doit également être symétrique et pour que les fonctions *carte* et *distribution* fonctionnent bien les indices doivent être numérotés de 0 à n-1 où n est la taille du tableau. 

\

Graph du chemin optimal (celui revenant le moins cher) entre Sigean et Nailloux.
------------------------------------------------------------------------------------------------------------------------------------------------
.. figure:: graph.png
   :width: 600
   :align: center
   
   
Pour que l'algorithme puisse fonctionner, il est primordial que les données soit représentées dans un dataframe de la forme suivante:

.. figure:: dataframe.png
   :width: 600
   :align: center
   
Comme vous pouvez le constater, il faut que la première colonne du dataframe soit composée uniquement du nom des villes. Les noms des autres colonnes représentent également les noms des villes. Les valeurs numériques du dataframe représentent le prix que l'on va payer pour un trajet direct entre la ville associé à la ligne et la ville associée à la colonne.
