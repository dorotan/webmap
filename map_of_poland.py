import folium

map = folium.Map(location=[52, 20], zoom_start=6, tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")

# using "for" loop to create a new marker on the map of Poland
for coordinates in [[50.4166667, 17.9666667], [52.4166667, 18.9666667]]:
    fg.add_child(folium.Marker(
        location=coordinates,
        popup="To jest tooltip",
        icon=folium.Icon(color='pink')
    ))

# adding a marker one by one
fg.add_child(folium.Marker(
    location=[52.4166667, 16.9666667],
    popup="Poznań to miasto na prawach powiatu "
    "w zachodniej Polsce, położone nad rzeką Wartą, "
    "u ujścia Cybiny.",
    icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(
    location=[52.22977, 21.01178],
    popup="Warszawa - stolica Polski i województwa mazowieckiego, "
    "największe miasto kraju, położone nad Wisłą.",
    icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(
    location=[51.1, 17.03333],
    popup="Wrocław to miasto na prawach powiatu, położone w "
    "południowo-zachodniej Polsce, "
    "siedziba władz województwa dolnośląskiego "
    "i powiatu wrocławskiego.",
    icon=folium.Icon(color='red')))
map.add_child(fg)


# saving my map
map.save("Polandmap.html")