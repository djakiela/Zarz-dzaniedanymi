import folium

lokacja_wsiz = [50.049, 21.98]

#Zadanie 1
# MAP 01
map = folium.Map(location=lokacja_wsiz, zoom_start=17)
map.save("Map1.html")

#Zadanie2
# MAP 02
map_terrain = folium.Map(location=lokacja_wsiz, zoom_start=13)
map_terrain.save("Mapa_Stamen_Terrain.html")

#Zadanie3
# MAP 03
map_cartodb = folium.Map(location=lokacja_wsiz, zoom_start=13, tiles='CartoDB Positron')
map_cartodb.save("Mapa_CartoDB.html")

#Zadanie4
# MAP 04
map_wskaznik_wsiz = folium.Map(location=lokacja_wsiz, zoom_start=13)

folium.Marker(
    lokacja_wsiz,
    popup='Tu jest marker!',  
    tooltip='Kliknij mnie!'  
).add_to(map_wskaznik_wsiz)
map_wskaznik_wsiz.save("Mapa_Wskaznik_Wsiz.html")

#MAP 05
lokacja_rzeszow = [50.041187, 21.999121]
lokacja_bilgoraj = [50.541280, 22.722030]

map_2_wskazniki = folium.Map(location=[50.049, 21.98], zoom_start=8)
folium.Marker(
    lokacja_rzeszow,
    popup='Stolica Podkarpacia',
    tooltip= 'Rzeszów',
    icon=folium.Icon(color='green')
).add_to(map_2_wskazniki)
folium.Marker(
    lokacja_bilgoraj,
    popup='Jakieś zadupie XD',
    tooltip='Biłgoraj',
    icon=folium.Icon(color='green')
).add_to(map_2_wskazniki)

map_2_wskazniki.save("Mapa_z_zielonymi_markerami.html")

#Zadanie5
#MAP 06

lokacje = {
    'Krosno': [49.6835, 21.7661],
    'Bałucianka': [49.895, 22.3308],
    'Kraków': [50.0614, 19.9372],
    'Lublin': [51.2465, 22.5684]
}

mapa_z_pomaranczowymi_markerami = folium.Map(location=[50.0614, 19.9372], zoom_start=6)

for nazwa, wspolrzedne in lokacje.items():
    folium.Marker(
        location=wspolrzedne,
        popup=nazwa,
        tooltip= nazwa + '- warto odwiedzić',
        icon=folium.Icon(color='orange')
    ).add_to(mapa_z_pomaranczowymi_markerami)

mapa_z_pomaranczowymi_markerami.save("Mapa_z_pomaranczowymi_markerami.html")

