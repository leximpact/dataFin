class Commune(object):
    
    def __init__(self, nom, siren, code_insee, code_epci):
        self.nom = nom
        self.siren = siren
        self.code_insee = code_insee
        self.code_epci = code_epci

    # Comptes consolidés : 
    # https://forum.datafin.fr/t/comptes-consolides-des-communes-2012-2018/453


class EPCI(object):
    
    # Établissement public de coopération intercommunale

    def __init__(self, nom, communes):
        self.nom = nom
        self.communes = communes

    @property
    def a_fiscalite_propre(self):
        # Deux types d'EPCI : sans fiscalité propre, à fiscalité propre
        return self._a_fiscalite_propre

    @a_fiscalite_propre.setter
    def a_fiscalite_propre(self, a_fiscalite_propre):
        self._a_fiscalite_propre = a_fiscalite_propre


class Departement(object):

    # Est aussi une collectivité territoriale

    def __init__(self, nom):
        self.nom = nom
