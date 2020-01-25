import os
import pandas
import numpy as np

from back.parametres.potentiel_financier_moyen import  potentiel_financier_moyen


def rang_strate_par_commune(nombre_habitants):
    # Prépare le parcours des strates de la plus à la moins peuplée.
    seuils_inverses_pfi_moyen = list(reversed(list(potentiel_financier_moyen['brackets']['2019-01-01'].keys())))
    
    # Par strate (du plus grand nombre d'habitants au plus petit), indique les communes présentes.
    check_strate = lambda strate: nombre_habitants >= int(strate)
    communes_par_strate = list(map(check_strate, seuils_inverses_pfi_moyen))

    # Calcul de l'identifiant de la strate de chaque commune.
    rang_strate_par_commune = sum(communes_par_strate) - 1 # rangs dans l'ordre croissant d'habitants (inversion annulée par la somme)
    rang_strate_par_commune.name = 'rang_strate_par_commune'
    
    return rang_strate_par_commune


def dotation_solidarite_rurale(nombre_habitants, pfi_habitant, max_nombre_habitants, ponderation):
    # http://www.dotations-dgcl.interieur.gouv.fr/consultation/documentAffichage.php?id=94
    # pages 6 et 7
    
    # strictement moins de max_nombre_habitants habitants, sinon pas de dsr
    condition_nombre_habitants = (nombre_habitants < max_nombre_habitants)

    montants_potentiels_financiers_moyens = list(potentiel_financier_moyen['brackets']['2019-01-01'].values())
    get_pfi_moyen = lambda rang_strate: montants_potentiels_financiers_moyens[rang_strate]
    rangs_strates = rang_strate_par_commune(nombre_habitants)
    pfi_moyen_par_commune = np.array(list(map(get_pfi_moyen, rangs_strates)))
    
    # pfi/habitant < ponderation * (pfi moyen toutes communes confondues de même strate démographique/habitant)
    return condition_nombre_habitants * (pfi_habitant < ponderation * pfi_moyen_par_commune)


def eligible_dsr(max_nombre_habitants = 10000, ponderation = 2):
    csv_communes_criteres_repartition = './back/inputs/2019-communes-criteres-repartition.csv'
    # print(os.path.abspath(csv_communes_criteres_repartition))
    communes_criteres_repartition_2019 = pandas.read_csv(
        csv_communes_criteres_repartition,
        decimal=",")
    # print(communes_criteres_repartition_2019.keys())

    assert len(communes_criteres_repartition_2019["Informations générales - Nom de la commune"]) == 35056

    nombre_habitants = communes_criteres_repartition_2019[
        "Informations générales - Population DGF Année N'"
        ]
    pfi_habitant = communes_criteres_repartition_2019[
        "Potentiel fiscal et financier des communes - Potentiel financier par habitant"
        ]
    codes_insee = communes_criteres_repartition_2019[
        "Informations générales - Code INSEE de la commune"
    ]
    
    eligibilite = dotation_solidarite_rurale(nombre_habitants, pfi_habitant, max_nombre_habitants, ponderation)
    # print(len(eligibilite),  "09034" in codes_insee.values)
    return pandas.Series(data=eligibilite.values, index=[str(k) for k in codes_insee.values])


# pour tester
if __name__ == '__main__':
    eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = 10000, ponderation = 2)
    # print(eligibilite_par_code_insee)

    indexes_communes_eligibles = np.where(eligibilite_par_code_insee == True)[0]
    print("#Communes éligibles DSR péréquation : ", len(indexes_communes_eligibles))
    print("Liste communes éligibles : ", indexes_communes_eligibles)
