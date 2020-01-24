import pytest

import os.path
import pandas
from configparser import RawConfigParser


# CSV des comptes consolidés :
# https://data.ofgl.fr/explore/dataset/comptes-consolides-des-communes-2012-20180/export/?disjunctive.agregat

def test_comptes_consolides():
    # Chargement de la configuration
    config_parser = RawConfigParser()
    found = config_parser.read('./config.ini')
    csv_comptes_consolides = config_parser.get('communes', 'csv_comptes_consolides')
    
    # Chargement des données
    data_comptes_consolides = pandas.read_csv(csv_comptes_consolides, sep=';')
    
    assert data_comptes_consolides.commune is not None
