import time
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

from dotation_solidarite_rurale import eligible_dsr


def carte_communes_eligibles_dsr_perequation(eligibilite_par_code_insee):
    geojson = gp.read_file('./back/inputs/communes-20190101.json')

    john=[eligibilite_par_code_insee[str(geojson["insee"][k])] if str(geojson["insee"][k]) in eligibilite_par_code_insee else -1 for k in range(len(geojson["insee"]))]
    geojson=geojson.assign(trueness=pd.Series(
        data=john, 
        index=range(len(geojson["insee"]))))

    deg2km = 111  # https://ocefpaf.github.io/python4oceanographers/blog/2015/03/30/geo_pandas/
    geojson.plot(column="trueness",legend = True)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    path_carte = "./static/eligibilite_dsr_perequation_{}.png".format(timestr)
    plt.savefig(path_carte)
    # plt.show()

    return path_carte


# pour tester
if __name__ == '__main__':
    eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = 10000, ponderation = 2)
    # print(eligibilite_par_code_insee)

    path_carte = carte_communes_eligibles_dsr_perequation(eligibilite_par_code_insee)
    print(path_carte)
