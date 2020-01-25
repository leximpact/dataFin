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


def dotation_solidarite_rurale(nombre_habitants, pfi_habitant):
    # http://www.dotations-dgcl.interieur.gouv.fr/consultation/documentAffichage.php?id=94
    # pages 6 et 7
    
    # strictement moins de 10000 habitants, sinon pas de dsr
    dsr_max_nombre_habitants = 10000
    condition_nombre_habitants = (nombre_habitants >= dsr_max_nombre_habitants)

    montants_potentiels_financiers_moyens = list(potentiel_financier_moyen['brackets']['2019-01-01'].values())
    get_pfi_moyen = lambda rang_strate: montants_potentiels_financiers_moyens[rang_strate]
    rangs_strates = rang_strate_par_commune(nombre_habitants)
    pfi_moyen_par_commune = np.array(list(map(get_pfi_moyen, rangs_strates)))
    
    # pfi/habitant < 2 * (pfi moyen toutes communes confondues de même strate démographique/habitant)
    return condition_nombre_habitants * (pfi_habitant < 2 * pfi_moyen_par_commune)
