###############################################################################
#########Este ejercicio ha sido realizado por Antonio Aguirre Arcos############
###############################################################################
import folium
import pandas as pd

specie = pd.read_csv ('Pyrrhocorax_graculus.csv', sep = '\t')
specie_1 = pd.read_csv('Tarucus_theophrastus.csv', sep = '\\t')
specie_2 = pd.read_csv('Ziziphous_lotus.csv', sep = '\\t')

species_map = folium.Map(location = [36.7306,-2.83201], tiles = 'Stamen Terrain',
                         zoom_start = 6)

for label, ocurrence in specie.iterrows():
 
    longitude = ocurrence['decimalLongitude']
    longitude_str = str(longitude)
    latitude = ocurrence ['decimalLatitude']
    latitude_str = str (latitude)
    nombre = ocurrence ['scientificName']
    nombre_cien = f'<i>{nombre}<\i>'

    if not pd.isnull(longitude):
        icono = folium.Icon (color = 'red', icon_color = 'black',
                             icon = 'binoculars', prefix = 'fa')
        marker = folium.Marker(
                location = [latitude,longitude],
                tooltip = 'Chova piquigualda ¡click para más!',
                popup = folium.Popup(nombre_cien+ '; Coordenadas: '  
                                     + latitude_str + ',' + longitude_str),
                                     icon = icono)
        marker.add_to(species_map)

for label, ocurrence in specie_1.iterrows():
    
    longitude_1 = ocurrence['decimalLongitude']
    longitude_str_1 = str(longitude_1)
    latitude_1 = ocurrence ['decimalLatitude']
    latitude_str_1 = str (latitude_1)
    nombre_1 = ocurrence ['scientificName']
    nombre_cien_1 = f'<i>{nombre_1}<\i>'

    if not pd.isnull(longitude_1):
        icono = folium.Icon(icon = 'bug',icon_color = 'white',
                            color = 'blue', prefix = 'fa')
        marker = folium.Marker(
                location = [latitude_1,longitude_1], 
                tooltip = 'Mariposa laberinto ¡click para más!',
                popup = folium.Popup(nombre_cien_1+ '; Coordenadas: '  
                                     + latitude_str_1 + ',' + longitude_str_1),
                                     icon = icono)
        marker.add_to(species_map) 
        
for label, ocurrence in specie_2.iterrows():
    
    longitude_2 = ocurrence['decimalLongitude']
    longitude_str_2 = str(longitude_2)
    latitude_2 = ocurrence ['decimalLatitude']
    latitude_str_2 = str (latitude_2)
    nombre_2 = ocurrence ['scientificName']
    nombre_cien_2 = f'<i>{nombre_2}<\i>'

        
    if not pd.isnull(longitude_2):
        icono = folium.Icon(color = 'green',icon_color='white', 
                                   icon= 'leaf', angle = 45)
        marker = folium.Marker(
                location = [latitude_2,longitude_2], 
                tooltip = 'Azufaifo ¡click para más!',
                popup = folium.Popup(nombre_cien_2+ '; Coordenadas: '  
                                     + latitude_str_2 + ',' + longitude_str_2),
                                     icon = icono)
                
        marker.add_to(species_map)         
        
species_map.save('mapa_especies.html')

