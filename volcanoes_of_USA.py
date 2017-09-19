import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <=elevation < 1500:
        return 'pink'
    elif 1501 <=elevation < 2000:
        return 'green'
    elif 2001 <=elevation < 2500:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[42.0306403, -102.3134298], zoom_start=4, tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")

# using "for" loop to create a new marker on the map of USA
for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=str(elev)+" metres",
                                     fill_color=color_producer(elev), color='grey', fill=True, fill_opacity=0.7))


fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))



map.add_child(fg)


# saving my map
map.save("Volcanoesmap.html")