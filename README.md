# Morpion

Jeu de morpion en console développé en Python. Le joueur affronte
l'ordinateur sur une grille de 3 x 3 cases.

## Fonctionnement

- L'ordinateur joue avec le symbole `X`.
- Le joueur joue avec le symbole `O`.
- L'ordinateur commence et choisit ses cases aléatoirement.
- À chaque tour, le joueur saisit le numéro d'une case libre entre `1` et `9`.
- Le premier joueur qui aligne trois symboles horizontalement, verticalement ou
  en diagonale gagne.
- Si toutes les cases sont occupées sans alignement gagnant, la partie est nulle.

La numérotation des cases est la suivante :

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

## Prérequis

- Python 3

## Lancer le jeu

Depuis le dossier du projet, exécutez :

```bash
python3 morpion.py
```

Puis saisissez le numéro d'une case libre lorsque le programme vous le demande.

## Structure du projet

```text
.
├── morpion.py   # Code du jeu
└── README.md    # Documentation
```

## Objectifs de l'exercice

Cet exercice permet de pratiquer :

- les listes et les boucles en Python ;
- les fonctions ;
- la validation des saisies utilisateur ;
- la génération de valeurs aléatoires ;
- la vérification des lignes, colonnes et diagonales gagnantes.