"""Remplit les fonctions de hash demandées"""

import time
import hashlib

def genere_clefs(utilisateur):
    timestamp = time.time()
    """Génère un couple de clefs pour l'utilisateur"""
    
    chaine = utilisateur + 'mot_de_passe' + str(timestamp)
    hash_obj = hashlib.sha256(chaine.encode('utf8'))
    publique = int(hash_obj.hexdigest())

    temp =(int(time.time())) % 42) + (int(time.time())) % 17)
    
    chainep = str(publique) + chaine + str(temp)
    hash_obj_p = hashlib.sha256(chainep.encode('utf8'))
    privee = int(hash_obj_p.hexdigest())
    return publique, privee
