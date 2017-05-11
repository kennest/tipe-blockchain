# tipe-blockchain

## Description

Projet de TIPE en MP

En MPSI, il a été centré sur la création d'une cryptomonnaie en local. Ce projet a par la suite été abandonné.
En MP, nous nous concentrons sur l'aspect réseau P2P, en se basant sur des modèles comme I2P.

## Contenu :

### Comptes-rendus

Les comptes-rendus en pdf, avec les sources Tex.

### MPSI

Le travail de premier année. Le programme python fonctione plus ou moins.


### Python

Le programme Python de seconde année :
 * main.py : c'est le fichier à exécuter (requiert matplotlib pour certaines choses, masi peut être utilisé sans). Il a utilise le module cmd de la bibliothèque standard.
 * modelisation : module comprenant les définitions des objets utilisés
 * djikstra.py comprend l'algorithme de recherche de chemin dans le réseau (inutilisé)
 * tests: différents tests
    + test1000.py est la modélisation d'un réseau de taille 1000
    + testa.py est la modélisation d'un réseau de taille 1à, pour les premiers tests
    + atkaleat : simule une attaque sur un *réseau aléatoire*, c'est-à-dire que chaque agent a le même nombre de tunnels sortants
    + scale-free : sur un réseau *scale-free*


## A faire :

 * vérifier le comportement de *testsf* : est-ce bien un noeud au moins qui est voisin (pas plus ?)
 * afficher toutes les courbes pour chaque itération


## A lire :
 * The Law of The Few - Goyal

## Notes :

 * attaques sur les liens
 * diffusion, contagion dans un réseau
 * le réseau créé, avec cette transmission, est un arbre !
 * représenter réseaux en LaTeX
 * pour avoir moins de problèmes de connexité (donc accélère la génération) : réseau multi-directionnel
 * agents hétérogènes (différents types, tendance *homophilique* : se connectent plutôt avec des agents du même type)
 * donc modifint la propagation