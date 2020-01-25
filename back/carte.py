import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

from dotation_solidarite_rurale import eligible_dsr


eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = 10000, ponderation = 2)
print(eligibilite_par_code_insee)

geojson = gp.read_file('./back/inputs/communes-20190101.json')

# object_to_string = lambda code_insee_object: str(code_insee_object)
# geojson["insee"] = list(map(object_to_string, geojson["insee"]))

# geojson=geojson.assign(trueness=pd.Series(data=[k for k in range(len(geojson["insee"]))], index=range(len(geojson["insee"]))))
print("ourreee","09034" in eligibilite_par_code_insee.index, "09034" in geojson["insee"], "9034" in geojson["insee"])
print(geojson.dtypes)
john=[eligibilite_par_code_insee[str(geojson["insee"][k])] if str(geojson["insee"][k]) in eligibilite_par_code_insee else -1 for k in range(len(geojson["insee"]))]

print(john)
geojson=geojson.assign(trueness=pd.Series(
    data=john, 
    index=range(len(geojson["insee"]))))

# print("Degrés", geojson.length)
deg2km = 111  # https://ocefpaf.github.io/python4oceanographers/blog/2015/03/30/geo_pandas/
# print("Kilomètres", geojson.length * deg2km)

print(geojson.__dict__)

geojson.plot(column="trueness",legend = True)
plt.show()
