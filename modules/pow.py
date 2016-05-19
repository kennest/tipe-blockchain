"""
Module pour le minage.

    - Créé un nouveau bloc
    - Vérifie le hash du bloc
    - Dès que c'est bon maj de la blockchain
    
"""
import os
import hashlib


def gettransactions(utilisateur):
    """ Récupère les transactions en provenance d'un utilisateur. """
    liste = [] # liste de transactions
    transactions = os.listdir("../utilisateurs" + utilisateur + "/transactions_pending")
          # liste des fichiers de transactions
    n = len(transactions)
    for i in range(max(n,3)): # Ne prend que trois transactions
        with open(transactions[i], 'r') as f: # lecture de chaque fichier de transaction
            t = f.readlines() # liste contenant la transaction
        liste.append(t)
        os.remove(transactions[i]) # supprime le fichier de transaction
                                   # pour éviter des doublons
    return liste


def validite_transaction(utilisateur, i):
    """ Vérifie la validité de la transaction en cours. C'est-à-dire
    que l'émetteur ait plus ou autant de réserve que le montant envoyé."""
    id_last = get_id_last_bloc(utilisateur)
    bloc = get_bloc(utilisateur, id_last)
    l_bloc = len(bloc)
    for i in range(6, l_bloc):
        
    return validite


def transaction(utilisateur,recepteur,montant) :
    """Effectue une transaction d'un compte vers un autre."""
    
    assert validite_hash_bloc(utilisateur,get_id_last_bloc(utilisateur))

    a = get_id_last_bloc(utilisateur)
    f = get_bloc(utilisateur, i) #Dernier bloc de la blockchain de l'utilisateur
    nb = int(f[0]) # Compteur (pour vérifier qu'il y ait bien trois transactions

    if nb == 3 : #Vérifie le nombre de transactions effectuées dans le bloc.
                 # Si le nombre maximum est atteint (3), on créé un nouveau bloc
                 # et on enregistre les transactions dedans.
                 
        id = str(a + 1) # id du nouveau bloc
        with open (utilisateur + '/blockchain/'+ id, 'w') as nouveau_bloc :
            f[0] = '0'
            for i in f :
                nouveau_bloc.write i
        a = id 

    else f[0] = str(int(f[0]) + 1) # Si le nombre maximum n'est pas atteint,
                                   # on incrémente simplement le nombre de
                                   # transactions du bloc.
    i = 0
    while ((f[i]).split('::'))[0] != utilisateur : # Recherche la ligne correspondant
                                                   # à l'envoyeur.
        i = i + 1

    t = int(f[i]).split('::'))[1]   #t prend la valeur de l'argent que possède
                                    # l'envoyeur.
    if int(t) >= montant : #Si l'envoyeur possède plus d'argent qu'il n'en envoie,
                           # déduit le montant de son portefeuille.
        t = str(int(t)-montant)

    k = 0
    while ((f[k]).split('::'))[0] != recepteur :   #Recherche la ligne correspondant
                                                   # au recepteur.
        k = k + 1

    r = int(f[k]).split('::'))[1]   #Ajoute le montant envoyé au portefeuille du
                                    # récepteur.
        r = str(int(r) + montant)


    # Copie les changements effectués dans le bloc.
    with open (utilisateur + '/blockchain/' + a, 'w') as bloc :
        for i in f :
            bloc.write(i)
