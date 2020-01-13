import folium
import pandas

data = pandas.read_json("dealersjson.json")
lat = list(data["latitude"])
lon = list(data["longitude"])
rat = list(data["rating"])
name = list(data["name"])
address = list(data["formatted_address"])

def color_producer(rating):
    if rating < 2:
        return 'red'
    elif 2<= rating <3:
        return 'orange'
    else:
        return 'green'

map = folium.Map(location=[33.74,-84.38], zoom_start=5)
fg = folium.FeatureGroup(name="Dealers Map")

for lt,ln, rt, name, address in zip(lat, lon, rat, name, address):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup="Name: "+str(name)+"  Address: "+str(address),
    fill_color=color_producer(rt), color = 'white',fill_opacity=0.7))

map.add_child(fg)
map.save("MapDealers.html")
