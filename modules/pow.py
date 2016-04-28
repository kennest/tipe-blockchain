"""
Module pour le minage.

    - Créé un nouveau bloc
    - Vérifie le hash du bloc
    - Dès que c'est bon maj de la blockchain
    
"""
import os
import hashlib


def gettransactions(utilisateur):
    """ Get the transactions from a transaction pool on the other computers."""
    liste = [] # liste de transactions
    transactions = os.listdir(utilisateur + "/transactions_pending") # liste des
                                                    # fichiers de transactions
    n = len(transactions)
    for i in range(n):
        with open(transactions[i], 'r') as f: # lecture de chaque
                                              # fichier de transaction
            t = f.readlines() # liste contenant la transaction
        liste.append(t)
        os.remove(transactions[i]) # supprime le fichier de transaction
                                   # pour éviter des doublons
    return liste


def validitetransaction(transaction):
    """ Vérifie la validité d'une transaction. """
    if <...>:
        return False
    return True
