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
- nodes
    les noeuds enregistres par le PC
"""

import modules.reseau

def getpeer():
    """ Se connecte à une adresse-mère, donnant les adresses d'autres noeuds du
    réseau. """
    return None

    
def getblockchain():
    """ Créé la blockchain sur cet ordinateur, en se connectant aux
    autres pairs du réseau. """
    return None


def initialisation():
    """ Initialise le programme au lancemant. """
    getpeer()
    getblockchain()
    return None


def login():
    """ Permet à l'utilisateur de se connecter. """


def signin():
    """ Permet à l'utilisateur de créer un compte. """
