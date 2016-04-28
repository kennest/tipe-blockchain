"""
Module de gestion de la blockchain
"""


def getblockchain(utilisateur):
    """ Récupère la blockchain d'un utilisateur sous forme de liste. """
    with open(utilisateur + 'blockchain', 'r') as f:
        f.readlines()
