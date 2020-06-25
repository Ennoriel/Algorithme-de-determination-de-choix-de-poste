# Algorithme de détermination de choix de poste

## Contexte

Avant la pandémie du COVID-19, tous les stagiaires d'une promotion de l'Ecole Nationale des Greffes se réunissaient 2 jours à Dijon pour réaliser à main lever le choix de poste. Cela représente, en fonction des 3 promotions annuelles environ 250 stagiaires par session soit 750 par an, soit 100 € pour le transport (certains venant d'Outre-Mers) et 100 € pour le logement (jusqu'à 2 nuits d'hotel ou dans l'école), soit 150 000 €.

Cette année le choix de poste a été fait à distance, en remplissant un fichier Excel, imprimé par l'école, vérifié manuellement (les stagiaires étaient contactés s'il y avait des erreurs). Avec deux équipes faisant le travail de répartition, vérifié tous les 50 candidats, le procésssus à pris 2,5 jours.

## Choix de poste

Le choix ce poste s'effectue ainsi :
  - un candidat dispose d'un classement
  - un candidat réalise une liste de voeux aussi longue que son classement
  - un candidat sera affecté au premier choix de sa liste encore disponible

## Algorithme mis en place

Le fichier de choix des candidats a volontairement été conservé tel quel, même si non optimisé. Il a été convertit au format csv.

Deux fichiers csv ont été constitués :
  - un fichier de classement (candidats.csv) consituté d'une colonne reprenant le matricule d'un stagiaire et une colonne avec son classement
  - un fichier du nombre de poste disponible (postes-disponibles) constitué d'une colonne avec le poste et d'une colonne avec le nombre disponible de position pour ce poste

L'algorithme (main.py) prend en paramètre le chemin du répertoire dans lequel ses fichiers csv sont et permet de :
  - afficher les erreurs de tous les candidats s'il y en a :
    - choix X non formulé.
    - plusieurs choix formulés en position X (TJ BORDEAUX, TJ NANTERRE).
  - sortir la liste d'affectation définitive s'il n'y a pas d'erreur

## Améliorations à prévoire

  - lire le format xlsx
  - modifier le format du fichier xlsx pour :
    - instruire une liste suivant les choix croissants
    - que le candidat puisse voir s'il y a des doubons, choix manquants en temps réel
  - ajouter une robustesse sur les éventuelles modifications sur les postes