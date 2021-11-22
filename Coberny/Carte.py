#%%
import openrouteservice
import json 
from openrouteservice import convert
import folium
import numpy as np
import pandas as pd
import osmnx as ox
#%%
class carte:

    def __init__(self,Coord,Name):
        

        client = openrouteservice.Client(key='5b3ce3597851110001cf6248dfd20bf8793e4e978b4bb0ca383bfd55')
        m = folium.Map(location=[43.1837661,3.0042121],zoom_start=10, control_scale=True,tiles="cartodbpositron")
        for i in range (0,len(Coord)-1):
            coords= (tuple(Coord[i,:]),)+(tuple(Coord[i+1,:]),)
            res = client.directions(coords)

            with(open('test.json','+w')) as f:
                f.write(json.dumps(res,indent=4, sort_keys=True))

            geometry = client.directions(coords)['routes'][0]['geometry']
            decoded = convert.decode_polyline(geometry)
            
            distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
            duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

            folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

            folium.Marker(
            location=list(coords[0][::-1]),
            popup=Name[i],
            icon=folium.Icon(color='orange',icon='car',prefix='fa'),
            ).add_to(m)

    
        m.save('map.html')
