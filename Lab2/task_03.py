import folium
import json

with open('world.json', 'r', encoding='utf-8-sig') as f:
    world_data = json.load(f)

def color(feature):
    population = feature['properties']['POP2005']
    if population < 10000000:
        return {'fillColor': 'green'}
    elif 10000000 <= population < 50000000:
        return {'fillColor': 'orange'}
    else:
        return {'fillColor': 'red'}

mapa = folium.Map(location=[52.0693, 19.4803], zoom_start=6)

# Dodawanie warstwy GeoJSON do mapy
folium.GeoJson(
    world_data,
    style_function=color,
    name='geojson'
).add_to(mapa)

# Dodanie warstwy kontrolnej, aby można było włączać i wyłączać warstwę GeoJSON
folium.LayerControl().add_to(mapa)

mapa.save("Mapa_Polski.html")
