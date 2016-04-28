"""
Module de gestion de la blockchain
"""

import os


def get_blockchain(utilisateur):
    """ Récupère la blockchain d'un utilisateur sous forme de liste. """

    # Détermine le dernier bloc
    blockchain = os.listdir(utilisateur + "/blockchain") # récupère la liste des blocs
    for i in range(len(blockchain)):
        blockchain[i] = int(blockchain[i])
    m = max(blocs) # Dernier bloc de l'utilisateur

    # Récupère le bloc
    with open(utilisateur + '/blockchain/' + m, 'r') as f:
        bloc = f.readlines()
    for i in range(3): # Les trois premiers champs sont
                            # 1) hash précédent
                            # 2) hash du bloc
                            # 3) timestamp
        bloc[i] = int(bloc[i])
    # traitement des trois transactions
    for i in range(3,6):
        #....
    return bloc
