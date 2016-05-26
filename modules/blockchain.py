"""
Module de gestion de la blockchain
"""

import os


def get_id_last_bloc(utilisateur):
    """ str -> int
    Récupère le numéro du dernier bloc d'un utilisateur."""

    # récupère la liste des blocs
    blockchain = os.listdir("../utilisateurs/" + utilisateur + "/blockchain")

    # Récupère la liste des numéros des blockchains
    for i in range(len(blockchain)):
        blockchain[i] = int(blockchain[i])
    m = max(blockchain) # Dernier bloc de l'utilisateur
    return m



def get_bloc(utilisateur, i):
    """ str -> int -> list
    Récupère le bloc i de l'utilisateur. Renvoie une liste de la forme
    [< hash précédent >, < hash du bloc >, < timestamp >,    int
    < transaction 1 >, < transaction 2 >, < transaction 3 >, [int, int, int]
    solde alice, solde bob, solde cedric,                    [int, int]
    solde dylan, solde etienne, solde fanny]
    """

    nbr = str(i)
    
    # Récupère le bloc
    with open("../utilisateurs/" + utilisateur + '/blockchain/' + nbr, 'r') as f:
        bloc = f.readlines()
    l_bloc = len(bloc)
    for j in range(2):             # Les deux premiers champs sont
        bloc[j] = int(bloc[j], 16) # 0) hash précédent
                                   # 1) hash du bloc
    bloc[2] = int(bloc[2])  # 2) timestamp
    
    # traitement des trois transactions
    for j in range(3,6):
        temp = bloc[j].split(" ; ")
        bloc[j] = [int(k.strip("( )\n")) for k in temp]
        
    for j in range(6, l_bloc): #traitement des soldes
        temp = '\n'.strip(bloc[j])
        templist = temp.split('::')
        bloc[j] = [templist[0], float(templist[1])]
    return bloc

def validite_hash_bloc(utilisateur, i):
    """ Vérifie la validité du bloc i. """

    #Vérifie hash bloc i
    bloc = get_bloc(utilisateur, i) # Récupère le bloc i
    l_bloc = len(bloc)
    bloc_text = bloc.copy() # Créé un bloc temporaire, qui sera converti
    bloc_text.pop(1)        # en texte, afin d'en calculer le hash
    for i in range(l_bloc -1):
        bloc_text[i] = str(bloc_text[i])
    hash_obj = hashlib.sha256(bloc_text.encode('utf8'))
    hash_current = int(hash_obj.hexdigest(), 16)
    validite_courante = (hash_current == bloc[1])

    bloc_p = get_bloc(utilisateur, i)
    validite_precedente = (bloc_p[1] == bloc[0])
    
    validite = validite_courante and validite_precedente
    return validite

    
