"""
Module de gestion de la blockchain
"""


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
    return bloc
