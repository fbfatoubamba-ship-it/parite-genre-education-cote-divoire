\# Parité fille/garçon dans l'éducation en Côte d'Ivoire



Petit projet perso où j'ai voulu regarder comment ça a évolué au primaire et

au collège en Côte d'Ivoire sur les 20 dernières années, en utilisant les

données de l'UNESCO.



\## Pourquoi ce sujet

On entend souvent parler des inégalités filles/garçons à l'école en Afrique

de l'Ouest, mais je voulais voir concrètement où en est mon pays avec de

vraies données, pas juste des impressions.



\## Ce que j'ai trouvé

\- Au primaire, l'indice de parité (GPI) est passé de 0,75 en 2000 à plus de

&#x20; 1,0 en 2024. Donc en gros la parité est atteinte, voire les filles sont

&#x20; légèrement plus nombreuses maintenant.

\- Au collège (1er cycle secondaire), pareil, ça part de 0,73 en 2013 et ça

&#x20; dépasse 1,0 en 2024, et la progression est même plus rapide qu'au primaire.

\- Ça correspond à peu près à la période de la loi de 2015 qui a rendu

&#x20; l'école gratuite et obligatoire jusqu'à 16 ans, donc probablement pas

&#x20; un hasard.



\## Dashboard

Le fichier `dashboard\_education\_civ.html` s'ouvre dans n'importe quel

navigateur, pas besoin d'internet une fois téléchargé.

Version en ligne : https://fbfatoubamba-ship-it.github.io/parite-genre-education-cote-divoire/dashboard_education\_civ.html



\## Données utilisées

Tout vient du UIS Data Browser (site de l'UNESCO) :

\- GER.1.GPIA : indice de parité de genre, primaire

\- GER.2.GPIA : indice de parité de genre, 1er cycle secondaire

\- effectifs scolarisés primaire et secondaire (pour le contexte)



\## Pour lancer le script

```bash

pip install pandas plotly

python analyse\_education\_civ.py

```



\## Ce que je n'ai pas encore fait

Je n'ai pas les données sur le taux d'achèvement (completion rate), et

je sais que c'est là que les vraies inégalités ressortent souvent — la

parité en fréquentation ne veut pas dire que les filles finissent le

lycée au même rythme que les garçons. À creuser si j'ai le temps.



