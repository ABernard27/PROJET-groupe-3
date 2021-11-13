## Groupe Projet
Ce projet est dirigé par Chery Fanny, Côme Olivier et Bernard Anne.

## Programme de Travail
- Codage et visualisation de la carte permettant de déterminer le prix entre deux péages. 
- Codage de l'algorithme minimisant le coût du péage avec une contrainte k du nombre de sortie 
- Fonction test permettant de vérifier si l'algorithme fonctionne
- Création du beamer et tournage de la vidéo

## Programme détaillé
Nous allons tout d'abord créer les tableaux de données contenant les prix des péages et les distances séparant ces péages. Les données des prix sont fournis sur le pdf suivant : https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf 
Pour les distances il nous faut utiliser  les coordonnées des péages Lambert93, les transformer en WGS84 puis déterminer les distances à l'aide du package ```osmnx``` et ```pyroutelib3```. 

Pour ce projet, il y a 3 objectifs majeurs. Ces 3 objectifs sont les suivants : 

- Nous allons créer une carte intéractive du réseau autoroutier d'une partie de l'occitanie. Sur cette carte nous pourrons cliquer sur des portions de route (entre deux péages) afin d'avoir les informations suivantes : prix, km, prix/km. Nous utiliserons les packages ```folium``` et ```osmnx``` qui font appel aux données de OpenStreetMap. Nous utiliserons également ```plotly``` pour afficher la carte. 
- Il nous faudra également afficher une distribution des prix. La distribution étant libre nous avons choisi de .... à remplir.
- Enfin nous allons créer un algorithme permettant de déterminer le trajet pour un coùt minimal avec une contrainte k du nombre de sorties. C'est-à-dire que l'on donnera en entrée un point A d'entrée, un point B de sortie et k sorties possible durant le trajet. L'algorithme ressortira les noms des k sorties permettant de payer le moins cher possible sur cette portion de A à B. Nous utiliserons ```networkx```. Pour cela nous nous appuierons sur des algorithmes existants notamment l'algorithme de Kruskal et celui de Ford-Fulkerson.

Suite à ces 3 axes majeurs nous créerons des fonctions test avec ```pytest``` afin de vérifier la cohérence de notre programme.

## Répartition du Travail


