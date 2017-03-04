import modelisation as mod
import random



def est_connexe(net):
    """Retourne True si le graphe est connexe, False sinon."""
    M = mod.conv_net_to_matrix(net)
    Noeuds_visités = [0]*len(M)
    t = [0]
    for k in range(len(M)) :
        r = t.copy()
        for n in r :
            Noeuds_visités[n] = 2
            if Noeuds_visités == [2]*len(M) :
                return True
            t.pop(t.index(n))
            for i in range(len(M)) :
                if M[n][i] == 1 :
                    t.append(i)
    return False
                



def nombre_aretes(net) :
    """Retourne le nombre d'aretes du réseau net."""
    M = mod.conv_net_to_matrix(net)
    nombre_aretes = 0
    for i in range(len(M[0])) :
        for j in range(i,len(M[0])) :
            nombre_aretes = nombre_aretes + M[i][j]
    return nombre_aretes

def retire_colonne(M,k) :
    """Retire la colonne k de la matrice M."""
    for i in range (len(M)) :
        M[i].pop(k)

def retire_ligne(M,k) :
    """Retire la ligne k de la matrice M."""
    M.pop(k)

def retire_arete(M,i,j) :
    """Retire l'arête ij du graphe repésenté par la matrice M."""
    M[i][j] = 0
    M[j][i] = 0


            
def f_etoile_noeuds(net,k,l) :
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

    a = [-1]*l
    for i in range(l) :
        c = -1
        while c in a :
            c = random.randint(0,len(Noeuds)-1)
        a[i] = c
        
    a = sorted(a,reverse=True)
    for i in a :
        if not i in d :
            retire_colonne(M,i)
            retire_ligne(M,i)
    
    
    Nouveau_réseau = mod.conv_matrix_to_net(M)

    n = 0
    if est_connexe(Nouveau_réseau) :
        n = 1
    else :
        print(M)
        
    return (est_connexe(Nouveau_réseau),(n-nombre_aretes(net)-k))

def test_etoile_noeuds(net,k,l,n) :
    resultats = 0
    l = 0
    for i in range(n) :
        a = f_etoile(net,k,l)
        l = l + a[1]
        if a[0] == True :
            resultats += 1
    return (resultats,l/n)


def f_noeuds(net,k,l) :
    """Simule une attaque informatique contre le réseau net. k représente les moyens
    du défenseur, l ceux de l'attaquant."""
    Noeuds = net._get_list_id()
    M = mod.conv_net_to_matrix(net)

    d = [-1]*k
    for i in range(1,k) :  
        c = -1
        while c in d :
            c = random.randint(0,len(Noeuds)-1)
        d[i] = c

    a = [-1]*l
    for i in range(l) :
        c = -1
        while c in a :
            c = random.randint(0,len(Noeuds)-1)
        a[i] = c
        
    a = sorted(a,reverse=True)
    for i in a :
        if not i in d :
            retire_colonne(M,i)
            retire_ligne(M,i)
    print(M)
    
    
    Nouveau_réseau = mod.conv_matrix_to_net(M)

    n = 0
    if est_connexe(Nouveau_réseau) :
        n = 1
    else :
        print(M)
        
    return (est_connexe(Nouveau_réseau),(n-nombre_aretes(net)-k))


def test_noeuds(net,k,l,n) :
    resultats = 0
    x = 0
    for i in range(n) :
        a = f(net,k,l)
        x = x + a[1]
        if a[0] == True :
            resultats += 1
        print(a[0])
    return (resultats,x/n)




def liste_aretes(M) :
    """Fait la liste des aretes du graphe représenté par la matrice M."""
    l = []
    for i in range(len(M)):
        for j in range(i,len(M)) :
            if M[i][j] == 1 :
                l.append((i,j))
    return l

def f_aretes(net,k,l) :
    """Simule une attaque informatique contre le réseau net. k représente les moyens
    du défenseur, l ceux de l'attaquant."""
    M = mod.conv_net_to_matrix(net)
    L = liste_aretes(M)
    
    d = [-1]*k
    for i in range(1,k) :  
        c = -1
        while c in d or not c in L :
            c = (random.randint(0,len(Noeuds)-1),random.randint(0,len(Noeuds)-1))
        d[i] = c

    a = [-1]*l
    for i in range(l) :
        c = -1
        while c in a or not c in L :
            c = (random.randint(0,len(Noeuds)-1),random.randint(0,len(Noeuds)-1))
        a[i] = c
        
    for c in a :
        if not c in d :
            i,j = c
            retire_arete(M,i,j)
    
    Nouveau_réseau = mod.conv_matrix_to_net(M)

    n = 0
    if est_connexe(Nouveau_réseau) :
        n = 1
    else :
        print(M)
        
    return (est_connexe(Nouveau_réseau),(n-nombre_aretes(net)-k))

def test_aretes(net,k,l,n) :
    resultats = 0
    x = 0
    for i in range(n) :
        a = f_aretes(net,k,l)
        x = x + a[1]
        if a[0] == True :
            resultats += 1
        print(a[0])
    return (resultats,x/n)

def test(net,k1,l1,k2,l2,n) :
    a = test_noeuds(net,k1,l1,n)
    b = test_aretes(net,k2,l2,n)
    return (a,b,a[1]+b[1])
