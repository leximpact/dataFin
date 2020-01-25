# dataFin

## Interface graphique

Le code source de l'interface graphique est dans le répertoire `frontend/`.  
Sa documentation est définie [ici](frontend/README.md).

## Calcul en arrière-plan servi par une API web

Le code source du backend est dans le répertoire `back/` ainsi que dans le fichier `app.py`.  
Les calculs en arrière-plan sont effectués en `Python 3.7`.

### Installation 

L'installation de l'ensemble des dépendances décrites dans le fichier `requirements.txt` peut se faire au travers de cette commande :

```shell
make install
```

### Exécution

L'exécution de l'API web se fait depuis le répertoire racine `/dataFin` :

```shell
make run
```

Elle est alors servie à l'adresse suivante : `http://127.0.0.1:5000/`

### Endpoint `/dotations/dsr/eligebilite`

`POST` sur, par exemple `http://localhost:5000/dotations/dsr/eligebilite`.

## Communes, données et documents de référence

* [Comptes consolidés](https://forum.datafin.fr/t/comptes-consolides-des-communes-2012-2018/453)
* Liste des communes issue de [2019-communes-criteres-repartition.csv](https://www.data.gouv.fr/fr/datasets/criteres-de-repartition-des-dotations-versees-par-letat-aux-collectivites-territoriales/)
* Liste des [indicateurs](https://www.collectivites-locales.gouv.fr/ofgl-cap-sur-indicateurs-utilises-dans-repartition-des-ressources-recensement-2019) et leur fréquence d'usage
* [Json des communes](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/#_) pour carte

