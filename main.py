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

def initialisation():
    """ Initialise le programme au lancement. """
    # getpeer()
    # getblockchain()
    name = input()
    path = "../name"
    while acces != True
     acces = login
    return path


def login():
    """ Permet à l'utilisateur de se connecter. """
    password = input()
    with open(path + '/wallet', 'r') as f:
        f.readline()
        f.readline()
        truepassword = f.readline()
     if truepassword == password
          return True
    return False


def signin():
    """ Permet à l'utilisateur de créer un compte. """
    while choix != 'y': # L'utilisateur doit confirmer le mot de passe
        password = input()
        print(password)
        choix = input('y/n')
     # Manque la clef publique et la clef privée
    with open(path + '/wallet', 'w') as f: # Sauvegarde la wallet
        f.write()
    return None

initialisation()
