import hashlib
import time

def nombre_zeros(c,r) :
    nb = 0
    for i in range (r) :
        if c[i] == '0' :
            nb = nb + 1

    return nb
        


def preuve_travail_nbr_zeros(x) : 
    """x est le paramètre de difficulté de la preuve
        1 : 4
        2 : 256
        3 : 2021
        4 : 64756
        5 : 911460"""
    a = time.time()
    k = 0 
    l = 'Hello world !'
    while nombre_zeros((hashlib.sha256((l + str(k)).encode('utf8'))).hexdigest(),x) < x :
        k += 1
    b = time.time()
    #print("Temps : " + str(b-a))
    return b-a

def temps_preuve_nbr_utilisateurs(fonction, param, n):
    """fonction est la fonction calculant la preuve de travail et param est son paramètre."""
    listtemps = []
    for i in range(n+1):
        temps = fonction(param)
        listtemps.append(temps)
    min_tps = min(listtemps)
    somme_tps = 0
    for x in listtemps:
        somme_tps += x
    moyenne_tps = somme_tps / len(listtemps)
    print("Minimum : " + str(min_tps))
    print("Moyenne : " + str(moyenne_tps))
    return None
        
