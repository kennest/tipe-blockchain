"""
Module de gestion de la blockchain
"""

import os


def get_id_last_bloc(utilisateur):
    """ Récupère le numéro du dernier bloc d'un utilisateur."""

    # récupère la liste des blocs
    blockchain = os.listdir(utilisateur + "/blockchain")

    # Récupère la liste des numéros des blockchains
    for i in range(len(blockchain)):
        blockchain[i] = int(blockchain[i])
    m = max(blockchain) # Dernier bloc de l'utilisateur



def get_bloc(utilisateur, i):
    """Récupère le bloc i de l'utilisateur. Renvoie une liste de la forme
    [< hash précédent >, < hash du bloc >, < timestamp >,
    < transaction 1 >, < transaction 2 >, < transaction 3 >,
    solde alice, solde bob, solde cedric,
    solde dylan, solde etienne, solde fanny]
    """
    # Récupère le bloc
    with open(utilisateur + '/blockchain/' + i, 'r') as f:
        bloc = f.readlines()
    for j in range(3): # Les trois premiers champs sont
                            # 1) hash précédent
                            # 2) hash du bloc
                            # 3) timestamp
        bloc[j] = int(bloc[j])
        
    # traitement des trois transactions
    for j in range(3,6):
        t = bloc.split(" ; ")
        bloc[j] = [int(k) for k in t]
    return bloc
