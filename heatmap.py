import folium
import pandas as pd
from folium.plugins import HeatMap

data = pd.read_json("dealersjson.json")
lat = list(data["latitude"])
lon = list(data["longitude"])
rat = list(data["rating"])
name = list(data["name"])
address = list(data["formatted_address"])
web = list(data["website"])

html = """
Dealers name: <br>
<a href="http://www.google.com/search?q=%%22%s%%22" target="_blank">%s
Height: %s m
"""

max_amount = float(data['rating'].max())

hmap = folium.Map(location=[33.74,-84.38], zoom_start=7, )

hm_wide = HeatMap( list(zip(data.latitude.values, data.longitude.values, data.rating.values)),
                    min_opacity=0.2,
                    max_val=max_amount,
                    radius=15, blur=25,
                    max_zoom=1,
                    )

for lt,ln, rt, name, address, web in zip(lat, lon, rat, name, address, web):
    hmap.add_child(folium.CircleMarker(location=[lt, ln], radius = 3, popup="Name: "+str(name)+"  Address: "+str(address)+"  Website: "+str(web),
    fill_color='red', color = 'red',fill_opacity=0.7))


hmap.add_child(hm_wide)

hmap.save('heatmap.html')
