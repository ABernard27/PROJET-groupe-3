## Groupe Projet
Ce projet est dirigé par Chery Fanny (fanny.chery@etu.umontpellier.fr), Côme Olivier (olivier.come@etu.umontpellier.fr) et Bernard Anne (anne.bernard@etu.umontpellier.fr).

## Introduction
Ce package python nommé Coberny (Co=Côme, Ber=Bernard, Ny=Fanny) vise à étudier les autoroutes sous plusieurs angles. Tout d'abord il permet d'afficher une distribution des prix sur différents trajets. Il permet de créer un carte sur laquelle nous pouvons voir le trajet de l'autoroute ainsi que les prix, les temps et les distances entre deux portions d'autoroute. Pour finir il permet de déterminer, avec un nombre fixé de sortie, les sorties à effectuer pour avoir un coût du trajet minimal sur une portion donnée. La description détaillée des différents modules se trouve dans la documentation.

## Programme de Travail
- Codage et visualisation de la carte permettant de déterminer le prix entre deux péages. 
- Codage de l'algorithme minimisant le coût du péage avec une contrainte k du nombre de sortie 
- Fonction test permettant de vérifier si l'algorithme fonctionne
- Création du beamer et tournage de la vidéo

## Création des données
Pour la création des données nous avons utilisé plusieurs packages. Tout d'abord nous avons utilisé la package ```download``` afin de télécharger les données provenant du site internet suivant https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routier-national-concede/, il s'agit d'un fichier .csv contenant les noms des gares de péage, les coordonnées GPS (format L93), les noms des autoroutes ainsi que d'autres données que nous n'exploiteront pas ici. De plus, à l'aide de ```pandas```nous avons chargé les fichiers .csv afin de les modifier pour récupérer uniquement les éléments souhaités. 

- Nous avons, dans un premier temps, créé un dataframe contenant les noms des gares, les coordonnées et les autoroutes. Les autres colonnes ont donc été supprimées, ou plutôt lors de l'importation du fichier nous avons choisi les colonnes que nous voulions garder puis nous avons choisi les lignes décrivant les autoroutes concernées par la projet à l'aide de la fonction .loc. Pour les coordonnées nous avons modifié les coordonnées qui étaient dans un format L93 pour les mettre en WGS84 à l'aide du package ```pyproj```. Toutes ces données sont alors mises dans un dataframe nommé "data" (sous format .csv).

- Ensuite nous avons utilisé ce dataframe pour créer la matrice des distances entre les portions d'autoroute. Pour cela nous avons utiliser ```requests```et ```json```pour faire des requêtes de distance entre chaque coordonnées de "data". Avec ceci nous recueillons les distances entre A et B mais nous souhaitons savoir si le trajet entre B et A est identique. Ce qui n'est pas nécessairement le cas car les packages utilisent ```openstreetmap``` qui suit la route tout le long et ne peut changer de sens sur l'autoroute qu'en sortant de celle-ci ce qui n'est pas le plus pratique dans nos calculs. Nous avons donc fait de A vers B puis de B vers A pour prendre le minimum des deux. Nous obtenons alors une matrice triangulaire que nous rendons symétrique. Cette matrice est alors transformée en dataframe nommé "distance" (sous format .csv) dans lequel nous avons en colonne le nom des gares et en ligne les index allant de 0 à la longueur du dataframe. Ce choix d'index sera utile pour la suite.

- Pour le dataframe des prix nous avons simplement reporté le fichier suivant https://public-content.vinci-autoroutes.com/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf en format .csv pour l'utiliser avec ```pandas```et choisir les péages voulus. Puis nous avons renommé les colonnes pour être cohérent avec les autres dataframe. Nous obtenons un dataframe nommé "prix" (sous format .csv).

## Programme détaillé
Après les données nettoyées et les dataframe créés nous pouvons commencer le programme. 

Pour ce projet, il y a 3 objectifs majeurs. Ces 3 objectifs sont les suivants : 

- Nous allons créer une carte intéractive du réseau autoroutier d'une partie de l'occitanie. Sur cette carte nous pourrons cliquer sur des portions de route (entre deux péages) afin d'avoir les informations suivantes : prix, km, temps. Nous utiliserons les packages ```folium``` et ```openstreetmap``` pour créer la carte que nous enregistrons en .html . 
- Nous souhaitons également réaliser une distribution des prix. Nous souhaitons  un graphique d'estimation de la densité du noyau KDE (Kernel Density Estimate) pour visualiser le prix par kilomètre entre chaque sortie où il sera possible de modifier l'entrée et la sortie pour obtenir des graphiques différents. Nous allons créer une classe "distribution" avec les arguments "data", "entrée", "sortie" qui nous retournera la distribution pour la portion choisie. 
- Enfin nous allons programmer un algorithme permettant de déterminer le trajet pour un coût minimal avec une contrainte k du nombre de sorties. C'est-à-dire que l'on donnera en entrée un point A d'entrée, un point B de sortie et k sorties possible durant le trajet. L'algorithme ressortira les noms des k sorties permettant de payer le moins cher possible sur cette portion de A à B. Nous utiliserons le package ```networkx```. Pour cela nous nous appuierons sur des algorithmes existants notamment l'algorithme de Kruskal (et celui de Ford-Fulkerson).

Suite à ces 3 axes majeurs nous créerons des fonctions test avec ```pytest``` afin de vérifier la cohérence de notre programme. Nous utiliserons également ```time``` nous permettant de mesurer et d'afficher le temps d'exécution. 

## Répartition du Travail
Le projet se partageant en 3 grosses phases de travail, nous aurons un objectif chacun. Bernard Anne s'occupera de créer la carte intéractive. Chery Fanny fera la partie sur la distribution des prix et Côme Olivier se chargera de la minimisation du coût du trajet. Il s'agit d'une répartition globale et non significative car il reste beaucoup d'autres parties du projet non expliquées ici, par exemple la documentation, sur lesquelles nous travaillerons tous. 
