###########################################
# Ceci n'est absolument pas opérationnel. #
# Le réseau sera développé plus tard.     #
###########################################

"""

Gestion transaction
- Vérification identité (couple clef publique/clef privée)
- Échange de clés Diffie-Hellman
- Commande pour la faire

Blockchain
- Vérifier avec autres noeuds

Preuve de travail (minage)
- Échange de clés Diffie-Hellman


Fichiers
- nodes
    les noeuds enregistres par le PC
"""

import os
import modules.reseau
import modules.pow
import modules.login


#Variables :

leave = False # Booléen pour savoir si l'utilisateur veut quitter


def initialisation():
    """ Initialise le programme au lancement. Récupère le chemin du fichier
    contenant wallet et blockchain."""
    acces = False #Par défaut, l'accès est refusé
    name = input('Username : ') # Nom de l'utilisateur
    path = "../" + name # Le dossier contenant wallet et blockchain est a
                        # l'addresse de path
    check = modules.login.checkuser(path) # Check if the file exist
    
    if not(check): # if no user is registered
        modules.login.signin(path)
        
    while acces != True: # login loop
        acces = modules.login.login(path)
    return path

def main(path):
    """ Main function"""

path = initialisation()

while leave == False:
    main(path)

exit()
