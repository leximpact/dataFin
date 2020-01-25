import geopandas as gp
import matplotlib.pyplot as plt

from dotation_solidarite_rurale import eligible_dsr


eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = 10000, ponderation = 2)
print(eligibilite_par_code_insee)

geojson = gp.read_file('./back/inputs/communes-20190101.json')

# print("Degrés", geojson.length)
deg2km = 111  # https://ocefpaf.github.io/python4oceanographers/blog/2015/03/30/geo_pandas/
# print("Kilomètres", geojson.length * deg2km)

print(geojson.__dict__)

geojson.plot()
plt.show()
