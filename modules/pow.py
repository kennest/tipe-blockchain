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


def transaction(utilisateur,recepteur,montant) :
    """Effectue une transaction d'un compte vers un autre."""
    
    assert validite_hash_bloc(utilisateur,get_id_last_bloc(utilisateur))

    f = get_bloc(utilisateur,get_id_last_bloc(utilisateur))
    nb = int(f[0])
    a = get_id_last_bloc(utilisateur)
    if nb == 3 : #Vérifie le nombre de transactions effectuées dans le bloc. Si le nombre maximum est atteint (3), on créé un nouveau bloc et on enregistre les transactions dedans.
        id = str(int(get_id_last_bloc(utilisateur)) + 1)
        with open (utilisateur + '/blockchain/'+ id, 'w') as nouveau_bloc :
            f[0] = '0'
            for i in f :
                nouveau_bloc.write i
        a = id 


    else f[0] = str(int(f[0]) + 1) #Si le nombre maximum n'est pas atteint, on incrémente simplement le nombhre de transactions du bloc.
        
    

    i = 0
    while ((f[i]).split('::'))[0] != utilisateur : #Recherche la ligne correspondant à l'envoyeur.
        i = i + 1

    t = int(f[i]).split('::'))[1]                  #t prend la valeur de l'argent que possède l'envoyeur.
    if int(t) >= montant :                         #Si l'envoyeur possède plus d'argent qu'il n'en envoie, déduit le montant de son portefeuille.
        t = str(int(t)-montant)

    k = 0
    while ((f[k]).split('::'))[0] != recepteur :   #Recherche la ligne correspondant au recepteur.
        k = k + 1

    r = int(f[k]).split('::'))[1]                  #Ajoute le montant envoyé au portefeuille du récepteur.
        r = str(int(r) + montant)


    with open (utilisateur + '/blockchain/' + a, 'w') as bloc : #Copie les changements effectués dans le bloc.
        for i in f :
            bloc.write(i)
