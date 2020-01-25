# À exécuter dans un notebook

import folium
from IPython.display import display

# Create a map centered at the given latitude and longitude
my_map = folium.Map(location=[45,1], zoom_start=5)
# Add data from a geojson file
my_map.add_child(folium.GeoJson('./back/inputs/communes-20190101.json'))
# Display the map
display(my_map)
