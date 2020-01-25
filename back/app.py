from dotation_solidarite_rurale import dotation_solidarite_rurale

import pandas

communes_criteres_repartition_2019 = pandas.read_csv(
    './back/inputs/2019-communes-criteres-repartition.csv',
    decimal=",")
# print(communes_criteres_repartition_2019.keys())

assert len(communes_criteres_repartition_2019["Informations générales - Nom de la commune"]) == 35056

nombre_habitants = communes_criteres_repartition_2019[
    "Informations générales - Population DGF Année N'"
    ]
pfi_habitant = communes_criteres_repartition_2019[
    "Potentiel fiscal et financier des communes - Potentiel financier par habitant"
    ]
print(pfi_habitant)
print(dotation_solidarite_rurale(nombre_habitants, pfi_habitant))


# from entites import Commune
#
# c = Commune('c', 1234, 1234, 1234)
# dotation_solidarite_rurale = c.dotation_solidarite_rurale(1500, 1500)
# print("éligible ?", dotation_solidarite_rurale)
