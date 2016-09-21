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
    chemin = "../utilisateurs/" + utilisateur + "/transactions_pending/"
    transactions = os.listdir(chemin)
          # liste des fichiers de transactions
    n = len(transactions)
    for i in range(min(n,3)): # Ne prend que trois transactions
        with open(chemin + transactions[i], 'r') as f:
            # lecture de chaque fichier de transaction
            t = f.readlines() # liste contenant la transaction
        for j in range(len(t)):
            t[j] = (t[j]).strip('\n')
        print(t)
        liste.append(t)
        os.remove(chemin + transactions[i]) # supprime le fichier de transaction
                                   # pour éviter des doublons
    return liste


def verifie_solde_transaction(utilisateur, i):
    """ str -> int -> bool
    Vérifie la validité de la transaction en cours. C'est-à-dire
    que l'émetteur ait plus ou autant de réserve que le montant envoyé."""
    validite = True
    id_last = blockchain.get_id_last_bloc(utilisateur)
    
    bloc_actuel = blockchain.get_bloc(utilisateur, id_last)
    l_bloc_actuel = len(bloc_actuel)
    bloc_precedent = blockchain.get_bloc(utilisateur, id_last - 1)
    l_bloc_precedent = len(bloc_precedent)
    
    for i in range(6, l_bloc_precedent):
        clefpublique = bloc_precedent[i][0]
        solde = bloc_precedent[i][1]
        for j in range(3,6):
            balance = 0
            if bloc_actuel[j][0] == clefpublique:
                balance = balance - bloc_actuel[j][2]
            if bloc_actuel[j][1] == clefpublique:
                balance = blance + bloc_actuel[j][2]
        if balance + solde < 0:
            return False
    return True
