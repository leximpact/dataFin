import time
import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

from dotation_solidarite_rurale import eligible_dsr


def carte_communes_eligibles_dsr_perequation(eligibilite_par_code_insee):
    geojson = gp.read_file('./back/inputs/communes-20190101.json')

    john=[("1) Éligible" if eligibilite_par_code_insee[str(geojson["insee"][k])] else "2) Non éligible") if str(geojson["insee"][k]) in eligibilite_par_code_insee else "1) Éligible" for k in range(len(geojson["insee"]))]
    geojson=geojson.assign(trueness=pd.Series(
        data=john, 
        index=range(len(geojson["insee"]))))

    deg2km = 111  # https://ocefpaf.github.io/python4oceanographers/blog/2015/03/30/geo_pandas/
    
    # X_detail = np.linspace(-5, 5, 1024)
    # Y_detail = np.sinc(X_detail)
    
    leg_kwds={'loc': 'lower left'}
    # 'fancybox':True, 'framealpha':1, 'shadow':True, 'borderpad':1
    geojson.plot(column="trueness", legend=True, legend_kwds=leg_kwds)

    timestr = time.strftime("%Y%m%d-%H%M%S")
    path_carte = "static/eligibilite_dsr_perequation_{}.png".format(timestr)
    
    plt.xlim(-5.5, 10.5)
    plt.ylim(41, 51.5)
    # plt.show()

    plt.savefig(path_carte)

    return path_carte


# pour tester
if __name__ == '__main__':
    eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = 10000, ponderation = 2)
    # print(eligibilite_par_code_insee)

    path_carte = carte_communes_eligibles_dsr_perequation(eligibilite_par_code_insee)
    print(path_carte)
