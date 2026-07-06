"""
PROJET : Parité de genre dans l'éducation en Côte d'Ivoire
------------------------------------------------------------
Ce script :
1. Charge les données brutes exportées de UIS/UNESCO
2. Les nettoie et les met en forme avec pandas
3. Crée des graphiques interactifs avec plotly
4. Exporte un dashboard HTML que tu peux ouvrir dans ton navigateur

Comment lancer ce script :
    pip install pandas plotly
    python analyse_education_civ.py

Le fichier civ_education_gender_raw.csv doit être dans le même dossier.
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ============================================================
# ÉTAPE 1 : CHARGER LES DONNÉES
# ============================================================
# pd.read_csv() lit un fichier CSV et le transforme en "DataFrame"
# (un DataFrame = un tableau, comme dans Excel, mais manipulable en code)
df = pd.read_csv("civ_education_gender_raw.csv")

# Affiche les premières lignes pour vérifier que le chargement a marché
print("Aperçu des données brutes :")
print(df.head())
print()

# ============================================================
# ÉTAPE 2 : COMPRENDRE LA STRUCTURE
# ============================================================
# Nos données ont 3 colonnes : indicatorId, year, value
# Le problème : toutes les données sont "empilées" dans une seule colonne "value"
# On doit les séparer par indicateur pour pouvoir les comparer

# On isole chaque indicateur dans son propre DataFrame
gpi_primaire = df[df["indicatorId"] == "GER.1.GPIA"].copy()
gpi_secondaire = df[df["indicatorId"] == "GER.2.GPIA"].copy()
effectif_primaire = df[df["indicatorId"] == "20062"].copy()
effectif_secondaire_sup = df[df["indicatorId"] == "20070"].copy()

# .sort_values("year") trie par année pour que les courbes soient dans l'ordre
gpi_primaire = gpi_primaire.sort_values("year")
gpi_secondaire = gpi_secondaire.sort_values("year")

# ============================================================
# ÉTAPE 3 : NETTOYAGE
# ============================================================
# On s'assure que "year" et "value" sont bien des nombres (pas du texte)
# pd.to_numeric() force la conversion, errors="coerce" met NaN (vide) si ça échoue
for d in [gpi_primaire, gpi_secondaire, effectif_primaire, effectif_secondaire_sup]:
    d["year"] = pd.to_numeric(d["year"], errors="coerce")
    d["value"] = pd.to_numeric(d["value"], errors="coerce")
    d.dropna(subset=["year", "value"], inplace=True)  # supprime les lignes vides

print(f"GPI primaire : {len(gpi_primaire)} années de données ({gpi_primaire['year'].min()}-{gpi_primaire['year'].max()})")
print(f"GPI secondaire : {len(gpi_secondaire)} années de données ({gpi_secondaire['year'].min()}-{gpi_secondaire['year'].max()})")
print()

# ============================================================
# ÉTAPE 4 : GRAPHIQUE 1 — Évolution du GPI primaire et secondaire
# ============================================================
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=gpi_primaire["year"], y=gpi_primaire["value"],
    mode="lines+markers", name="Primaire",
    line=dict(color="#2E86AB", width=3)
))

fig1.add_trace(go.Scatter(
    x=gpi_secondaire["year"], y=gpi_secondaire["value"],
    mode="lines+markers", name="1er cycle secondaire",
    line=dict(color="#E63946", width=3)
))

# Ligne horizontale à 1.0 = ligne de parité parfaite (repère visuel clé)
fig1.add_hline(y=1.0, line_dash="dash", line_color="gray",
               annotation_text="Parité parfaite (1.0)", annotation_position="bottom right")

fig1.update_layout(
    title="Indice de parité de genre (GPI) dans l'éducation — Côte d'Ivoire",
    xaxis_title="Année",
    yaxis_title="Indice de parité (1.0 = parité filles/garçons)",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)

fig1.write_html("graphique_gpi_evolution.html")
print("Graphique 1 sauvegardé : graphique_gpi_evolution.html")

# ============================================================
# ÉTAPE 5 : GRAPHIQUE 2 — Effectifs scolarisés (contexte)
# ============================================================
fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=effectif_primaire["year"], y=effectif_primaire["value"],
    mode="lines+markers", name="Effectif primaire",
    line=dict(color="#2E86AB", width=3), fill="tozeroy"
))

fig2.update_layout(
    title="Évolution du nombre d'élèves scolarisés au primaire — Côte d'Ivoire",
    xaxis_title="Année",
    yaxis_title="Nombre d'élèves",
    template="plotly_white"
)

fig2.write_html("graphique_effectifs.html")
print("Graphique 2 sauvegardé : graphique_effectifs.html")

# ============================================================
# ÉTAPE 6 : DASHBOARD COMBINÉ (les 2 graphiques sur une page)
# ============================================================
dashboard = make_subplots(
    rows=2, cols=1,
    subplot_titles=(
        "Indice de parité de genre (GPI) — Primaire vs Secondaire",
        "Effectif scolarisé au primaire"
    ),
    vertical_spacing=0.15
)

dashboard.add_trace(go.Scatter(
    x=gpi_primaire["year"], y=gpi_primaire["value"],
    mode="lines+markers", name="GPI Primaire", line=dict(color="#2E86AB")
), row=1, col=1)

dashboard.add_trace(go.Scatter(
    x=gpi_secondaire["year"], y=gpi_secondaire["value"],
    mode="lines+markers", name="GPI 1er cycle secondaire", line=dict(color="#E63946")
), row=1, col=1)

dashboard.add_hline(y=1.0, line_dash="dash", line_color="gray", row=1, col=1)

dashboard.add_trace(go.Scatter(
    x=effectif_primaire["year"], y=effectif_primaire["value"],
    mode="lines+markers", name="Effectif primaire",
    line=dict(color="#2E86AB"), fill="tozeroy", showlegend=False
), row=2, col=1)

dashboard.update_layout(
    height=800,
    title_text="Dashboard : Éducation et parité de genre en Côte d'Ivoire (2000-2024)",
    template="plotly_white"
)

dashboard.write_html("dashboard_education_civ.html")
print("Dashboard complet sauvegardé : dashboard_education_civ.html")
print()
print("Ouvre ce fichier dans ton navigateur pour voir le résultat final !")
