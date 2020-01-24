from parametres.potentiel_financier_moyen import  potentiel_financier_moyen


class Commune(object):
    
    def __init__(self, nom, siren, code_insee, code_epci):
        self.nom = nom
        self.siren = siren
        self.code_insee = code_insee
        self.code_epci = code_epci

    def dotation_solidarite_rurale(self, nombre_habitants, pfi_habitant):
        # http://www.dotations-dgcl.interieur.gouv.fr/consultation/documentAffichage.php?id=94
        # pages 6 et 7
        
        # moins de 10000 habitants > sinon non
        dsr_max_nombre_habitants = 10000
        if nombre_habitants >= dsr_max_nombre_habitants:
            return 0
        
        for seuil_habitants in reversed(list(potentiel_financier_moyen['brackets']['2019-01-01'].keys())):
            if nombre_habitants >= int(seuil_habitants):
                # pfi/habitant < 2 * (pfi moyen toutes communes confondues de même strate démographique/habitant)
                print(potentiel_financier_moyen['brackets']['2019-01-01'][seuil_habitants])
                return pfi_habitant < 2 * potentiel_financier_moyen['brackets']['2019-01-01'][seuil_habitants]


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
