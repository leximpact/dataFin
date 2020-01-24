import pytest

import pandas
# import os.path
# from configparser import RawConfigParser


def test_dsr():
    c = Commune('c', 1234, 1234, 1234)
    dotation_solidarite_rurale = c.dotation_solidarite_rurale(1500, 1500)
    assert dotation_solidarite_rurale is True


# CSV des comptes consolidés :
# https://data.ofgl.fr/explore/dataset/comptes-consolides-des-communes-2012-20180/export/?disjunctive.agregat

# def test_comptes_consolides():
#     # Chargement de la configuration
#     config_parser = RawConfigParser()
#     found = config_parser.read('./back/config.ini')
#     csv_comptes_consolides = config_parser.get('communes', 'csv_comptes_consolides')
#     
#     # Chargement des données
#     data_comptes_consolides = pandas.read_csv(csv_comptes_consolides, sep=';')
#     
#     assert data_comptes_consolides.commune is not None
