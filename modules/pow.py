"""

Module pour le minage.

    - Créé un nouveau bloc
    - Vérifie le hash du bloc
    - Dès que c'est bon maj de la blockchain
    
"""

import os
import hashlib
import blockchain


def gettransactions(utilisateur):
    """ Récupère les transactions en provenance d'un utilisateur. """
    liste = [] # liste de transactions
    transactions = os.listdir("../utilisateurs/" + utilisateur + "/transactions_pending")
          # liste des fichiers de transactions
    n = len(transactions)
    for i in range(max(n,3)): # Ne prend que trois transactions
        with open("../utilisateurs/" + utilisateur + "/transactions_pending/" + transactions[i], 'r') as f: # lecture de chaque fichier de transaction
            t = f.readlines() # liste contenant la transaction
        liste.append(t)
        os.remove("../utilisateurs/" + utilisateur + "/transactions_pending/" + transactions[i]) # supprime le fichier de transaction
                                   # pour éviter des doublons
    return liste


def verifie_solde_transaction(utilisateur, i):
    """ str -> int -> bool
    Vérifie la validité de la transaction en cours. C'est-à-dire
    que l'émetteur ait plus ou autant de réserve que le montant envoyé."""
    validite = True
    id_last = blockchain.get_id_last_bloc(utilisateur)
    bloc = blockchain.get_bloc(utilisateur, id_last)
    l_bloc = len(bloc)
    
    for i in range(6, l_bloc):
        clefpublique = bloc[i][0]
        solde = bloc[i][1]
        for j in range(3,6):
            balance = 0
            if bloc[j][0] == clefpublique:
                balance = balance - bloc[j][2]
            if bloc[j][1] == clefpublique:
                balance = blance + bloc[j][2]
        if balance + solde < 0:
            return False
    return True
