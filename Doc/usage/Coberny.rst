Documentation
=============
Vous trouverez ici toute la documentation concernant le package ``Coberny``. Tous les modules sont décrits et documenter pour permettre aux utilisateurs de mieux manier le package. Bonne lecture ! 


Carte
-----
Le module Carte permet de créer une carte enregistrée automatiquement sous format html, sur laquelle nous pouvons afficher les différentes gares de péage présentes dans le jeu de données. Il est possible de clique sur les gares pour voir les noms s'afficher et nous pouvons cliquer entre deux portions d'autoroute pour voir des données sur ce trajet. 


.. automodule:: Coberny.map.Carte
   :members:
 

.. figure:: exemple_carte.jpg
   :width: 500
   :align: center

\   

Distribution
------------
Le module Distribution nous permet créer un Kernel Density Estimation (KDE)  qui est une méthode non-paramétrique d’estimation de la densité de probabilité d’une variable aléatoire. Ici, nous allons utiliser le prix au kilomètre comme variable aléatoire. Le KDE va être celui de l'estimation de la densité de la variable Prix/Kilomètre. De plus, ce module nous permet de visualiser les prix au kilomètre sur chaque section de la portion d'autoroute souhaitée.


.. automodule:: Coberny.distribution_of_price.distribution
   :members: 
   
Si nous exécutons ce code, nous obtenons :

.. figure:: plot1.png
   :align: center

.. figure:: plot2.png
   :align: center

.. figure:: plot3.png
   :align: center   

\

Graph et minimisation du coût
-----------------------------

.. automodule:: Coberny.graph_min_cost.best_price_path
   :members:


