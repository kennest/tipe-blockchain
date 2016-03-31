###########################################
# Ceci n'est absolument pas opérationnel. #
# Le réseau sera développé plus tard.     #
###########################################

"""

Gestion transaction
- Vérification identité (couple clef publique/clef privée)
- Échange de clés Diffie-Hellman
- Commande pour la faire

Blockchain
- Vérifier avec autres noeuds

Preuve de travail (minage)
- Échange de clés Diffie-Hellman


Fichiers
- blockchain.txt ? : la blockchain, historique des transactions
- wallet.txt : le porte-monnaie de la personne
     -> cle prive / cle publique
     mot de passe
     Ne gère qu'un seul utilisateur par ordinateur.
- nodes
    les noeuds enregistres par le PC
"""

import os
import modules.reseau
import modules.pow
import modules.login

def initialisation():
    """ Initialise le programme au lancement. Récupère le chemin du fichier
    contenant wallet et blockchain."""
    acces = False #Par défaut, l'accès est refusé
    name = input('Username : ') # Nom de l'utilisateur
    path = "../" + name # Le dossier contenant wallet et blockchain est a
                        # l'addresse de path
    check = modules.login.checkuser(path)
    if not(check):
        modules.login.signin(path)
    while acces != True:
        acces = modules.login.login(path)
    return None


initialisation()


