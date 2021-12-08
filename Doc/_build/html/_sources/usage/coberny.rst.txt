Documentation
=============
Vous trouverez ici toute la documentation concernant le package ``Coberny``. Tous les modules sont décrits et documenter pour permettre aux utilisateurs de mieux manier le package. Bonne lecture ! 


Carte
-----
Le module Carte permet de créer une carte enregistrée automatiquement sous format html, sur laquelle nous pouvons afficher les différentes gares de péage présentes dans le jeu de données. Il est possible de clique sur les gares pour voir les noms s'afficher et nous pouvons cliquer entre deux portions d'autoroute pour voir des données sur ce trajet. 


.. automodule:: Coberny.map.Carte
   :members:

Après avoir exécuté ce code nous obtenons la carte suivante : 

.. figure:: exemple_carte.jpg
   :width: 500
   :align: center
   

Distribution
------------

.. automodule:: Coberny.distribution_of_price.distribution
   :members: 
   
Si nous exécutons ce code, nous obtenons :

.. figure:: plot1.png
   :align: center

.. figure:: plot2.png
   :align: center

.. figure:: plot3.png
   :align: center   

Graph et minimisation du coût
-----------------------------

.. automodule:: Coberny.graph_min_cost.best_price_path
   :members:


