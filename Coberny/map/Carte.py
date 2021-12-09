#%%
import openrouteservice
import json 
from openrouteservice import convert
import folium
import time
#%%
def carte(Coord, Name, Key, prix):
    """ Trace sur une carte la route passant par des points GPS données, sur l'autoroute. Donne également le nom du point, les temps de trajet et le nombre de kilomètres entre les portions. Ce programme utilise les données de ``openstreetmap``

    :param numpy.ndarray Coord: Les coordonnées GPS en WSG84 : (longitude,latitude)
    :param DataFrame Name: Les noms des villes (ou autres) correspondant aux coordonnées (dans l'ordre)
    :param DataFrame prix: Les prix entre deux péages consécutifs
    :param str Key: La clé API créée avec *openrouteservice*

    .. warning:: 
        
        Attention! La clé doit être créée par vos soins, une rubrique expliquant comment le faire est disponible --> :ref:`Créer une clé API`
    
    :returns: La carte avec le tracé et les données sur le trajet
    
    :exemple: Voici un exemple de comment utiliser la fonction : 
    
    .. code::
    
    	Coberny.carte(np.column_stack([data['x'],data['y']]), data[' Nom gare' ], '5b3ce3597851110001cf6248dfd20bf8793e4e978b4bb0ca383bfd55', prix)
    """
    start = time.time()
    client = openrouteservice.Client(key=Key) 
    #utilise la clé openrouteservice pour pouvoir utiliser les données cartographiques
    m = folium.Map(location=[43.1837661, 3.0042121], zoom_start=10, control_scale=True)
    #se place autour du point donné qui est Narbonne ici
    
    # la boucle va faire des requêtes de chaque point de coordonnée entré puis relier ces points en passant par l'autoroute
    for i in range(0, len(Coord)-1):
        coords = (tuple(Coord[i, :]), )+(tuple(Coord[i+1, :]), )
        res = client.directions(coords)

        with(open('test.json', '+w')) as f:
            f.write(json.dumps(res, indent=4, sort_keys=True))

        geometry = client.directions(coords)['routes'][0]['geometry']
        # decode_polyline est une fonction pour relier les points
        decoded = convert.decode_polyline(geometry)
        distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>" + str(round(res['routes'][0]['summary']['distance'] / 1000, 1)) + " Km </strong>" + "</h4></b>"
        duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+ str(round(res['routes'][0]['summary']['duration'] / 60, 1)) + " Mins. </strong>" + "</h4></b>"
        test = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(prix[Name[i]][i+1]) + "€ </strong>" + "</h4></b>"
        folium.GeoJson(decoded).add_child(folium.Popup(test+distance_txt+duration_txt, max_width=500)).add_to(m) # ajout des données à une carte existante neutre
        folium.Marker(
        location=list(coords[0][::-1]),
        popup=Name[i],
        icon=folium.Icon(color='orange', icon='car', prefix='fa'),
        ).add_to(m) # folium.Marker pour noter et nommer les points de coordonnées
    m.save('map.html')
    end = time.time()
    print("Temps passé pour exécuter la commande: {0:.5f} s.".format(end - start))
    return m
