import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[42.0306403, -102.3134298], zoom_start=4, tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")

# using "for" loop to create a new marker on the map of USA
for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lat, lon], popup=str(elev)+" metres"))



map.add_child(fg)


# saving my map
map.save("Volcanoesmap.html")