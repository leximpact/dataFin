potentiel_financier_moyen = {
    'description': 'Potentiel FInancier (PFI) moyen par habitant',
    'threshold_unit': "nombre d'habitants (d'après la population DGF)",
    'rate_unit': 'euros',
    'reference': 'http://www.dotations-dgcl.interieur.gouv.fr/consultation/documentAffichage.php?id=94',
    'brackets': {
        '2019-01-01': {
            '0': 657.114759, # de 0 à 499 habitants
            '500': 722.315256,
            '1000': 785.439563,
            '2000': 862.218176,
            '3500': 940.663574,
            '5000': 1016.450575,
            '7500': 1073.239296, # à 9 999 habitants
        },
    }
}
