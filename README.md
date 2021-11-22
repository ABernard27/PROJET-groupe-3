## Groupe Projet
Ce projet est dirigé par Chery Fanny (fanny.chery@etu.umontpellier.fr), Côme Olivier (olivier.côme@etu.umontpellier.fr) et Bernard Anne (anne.bernard@etu.umontpellier.fr).

## Programme de Travail
- Codage et visualisation de la carte permettant de déterminer le prix entre deux péages. 
- Codage de l'algorithme minimisant le coût du péage avec une contrainte k du nombre de sortie 
- Fonction test permettant de vérifier si l'algorithme fonctionne
- Création du beamer et tournage de la vidéo

## Programme détaillé
Nous allons tout d'abord créer les tableaux de données contenant les prix des péages et les distances séparant ces péages. Les données des prix sont fournis sur le pdf suivant : https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf 
Pour les distances il nous faut utiliser  les coordonnées des péages Lambert93, les transformer en WGS84 puis déterminer les distances à l'aide du package ```json``` et ```requests```. 

Pour ce projet, il y a 3 objectifs majeurs. Ces 3 objectifs sont les suivants : 

- Nous allons créer une carte intéractive du réseau autoroutier d'une partie de l'occitanie. Sur cette carte nous pourrons cliquer sur des portions de route (entre deux péages) afin d'avoir les informations suivantes : prix, km, prix/km. Nous utiliserons les packages ```folium``` et ```openstreetmap``` pour créer la carte que nous enregistrons en .html . 
- Nous souhaitons également réaliser une distribution des prix. Nous souhaitons  un graphique d'estimation de la densité du noyau KDE (Kernel Density Estimate) pour visualiser le prix par kilomètre entre chaque sortie où il sera possible de modifier l'entrée et la sortie pour obtenir des graphiques différents. Nous allons créer une classe "distribution" avec les arguments "data", "entrée", "sortie" qui nous retournera la distribution pour la portion choisie. 
- Enfin nous allons programmer un algorithme permettant de déterminer le trajet pour un coût minimal avec une contrainte k du nombre de sorties. C'est-à-dire que l'on donnera en entrée un point A d'entrée, un point B de sortie et k sorties possible durant le trajet. L'algorithme ressortira les noms des k sorties permettant de payer le moins cher possible sur cette portion de A à B. Nous utiliserons le package ```networkx```. Pour cela nous nous appuierons sur des algorithmes existants notamment l'algorithme de Kruskal (et celui de Ford-Fulkerson).

Suite à ces 3 axes majeurs nous créerons des fonctions test avec ```pytest``` afin de vérifier la cohérence de notre programme. Nous utiliserons également ```time``` nous permettant de mesurer et d'afficher le temps d'exécution. 

## Répartition du Travail
Le projet se partageant en 3 grosses phases de travail, nous aurons un objectif chacun. Bernard Anne s'occupera de créer la carte intéractive. Chery Fanny fera la partie sur la distribution des prix et Côme Olivier se chargera de la minimisation du coût du trajet. Malgré cette répartition il est évident que chacun d'entre nous travaillera un peu sur chaque partie nous sommes avant tout une équipe et nous travaillerons très souvent tous ensemble. 

