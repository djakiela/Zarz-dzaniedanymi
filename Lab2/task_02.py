import folium
import pandas as pd

volcanoes = pd.read_csv('Volcanoes.txt')

# print(data_from_file)
# print(f'Type of data: {type(data_from_file)}')
# print(f'Type of some (sekected colum: {type(data_from_file["NAME"])})')


def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

mapa = folium.Map(location=[37.296933, -121.9574983], zoom_start=5)


for index, row in volcanoes.iterrows():
    iframe = folium.IFrame(f'''
    <h4>Informacja dodatkowa:</h4>
    Nazwa wulkanu: {row['NAME']}<br>
    Wysokość: {row['ELEV']} metrów
    ''', width=300, height=120)
    
    popup = folium.Popup(iframe, max_width=300)

    folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=9,
        tooltip=row['NAME'],
        popup=popup,
        color=color_producer(row['ELEV']),
        fill=True,
        fill_color=color_producer(row['ELEV']),
        fill_opacity=0.7
    ).add_to(mapa)

mapa.save("Mapa_Wulkanow.html")
