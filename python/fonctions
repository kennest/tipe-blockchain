import modelisation as mod
import random


def est_connexe(net) :
    """Retourne True si le graphe est connexe, False sinon."""
    M = mod.conv_net_to_matrix(net)
    for i in range(len(M[0])) :
        n = 0
        for k in range(len(M[0])) :
            n = n + M[k][i]
        if n == 0 :
            return False
    return True



def nombre_aretes(net) :
    """Retourne le nombre d'aretes du réseau net."""
    M = mod.conv_net_to_matrix(net)
    nombre_aretes = 0
    for i in range(len(M[0])) :
        for j in range(i,len(M[0])) :
            nombre_aretes = nombre_aretes + M[i][j]
    return nombre_aretes


            
def f(net,k,l) :
    """Simule une attaque informatique contre le réseau net. k représente les moyens
    du défenseur, l ceux de l'attaquant."""
    Noeuds = net._get_list_id()
    M = mod.conv_net_to_matrix(net)

    d = [-1]*k
    d[0] = 0
    for i in range(1,k) :  
        c = -1
        while c in d :
            c = random.randint(0,len(Noeuds)-1)
        d[i] = c
    #print (d)
        
        

    a = [-1]*l
    for i in range(l) :
        c = -1
        while c in a :
            c = random.randint(0,len(Noeuds)-1)
        a[i] = c
    #print (a)

    for i in a :
        if not i in d :
            for q in range(len(M[0])) :
                M[i][q] = 0
                M[q][i] = 0

    Nouveau_réseau = mod.conv_matrix_to_net(M)

    n = 0
    if est_connexe(Nouveau_réseau) :
        n = 1
     
    return (est_connexe(Nouveau_réseau),(n-nombre_aretes(net)-k))

def test(net,k,l,n) :
    resultats = 0
    for i in range(n) :
        a = f(net,k,l)
        if a[0] == True :
            resultats += 1
    return resultats
