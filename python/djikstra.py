"""
Implémentaion de l'algorithme de Djikstra, inutile
"""

import modelisation as mod
import heapq as hq #Pour implémenter des files de priorité

## Initialisation du réseau

"""
net = mod.Reseau()

for i in range(10):
    net._set_agent(i)

liens = [(0,3),(0,4), (1,2),(1,5), (2,0),(2,1), (3,4),(3,5),(3,8),(3,9), \
         (4,0), (5,1),(5,2),(5,6), (6,3), (7,3),(7,9), (8,3), (9,0),(9,7)]
for lien in liens:
    net._set_tunnel(lien[0], lien[1])
"""

net = mod.Reseau()
for i in range(4):
    net._set_agent(i)

net._set_tunnel(0,2)
net._set_tunnel(2,1)
net._set_tunnel(1,0)
net._set_tunnel(3,2)
net._set_tunnel(2,3)

##
#
# Recherche la distance entre deux noeuds par l'algorithme de Djikstra
#
# Voir : http://stackoverflow.com/questions/4997851/python-dijkstra-algorithm#16117378
#
##

#hq.heapify()


# r : distances calculées à la main, pour vérification, certaines
# valeurs sont fausses
r = [[0,3,3,1,1,2,3,3,2,2],[2,0,1,3,3,1,6,5,4,4],[1,1,0,2,2,2,3,4,3,3],\
     [2,2,2,0,1,1,2,2,1,1],[1,4,4,2,0,3,4,4,3,3],[2,1,2,2,3,0,1,4,3,3],\
     [3,3,3,1,2,2,0,3,2,2],[2,3,3,2,2,3,0,2,1],[3,3,3,1,2,2,3,3,0,2],\
     [1,4,4,2,2,3,4,1,3,0]]



def calcule_distance(emetteur_id) :
    """Calcule la distance d'emetteur_id à tous les noeuds du réseau.
    Attention, si un noeud n'a pas de tunnel sortant, cette fonction
    ne termine pas."""
    d = []
    for i in net._get_list_id() :
        t = [emetteur_id]
        k = 0
        while not i in t :
            k = k + 1
            r = t.copy()
            for j in r :
               for v in net._get_voisins_emet(j) :
                   t.append(v)
        d.append(k)
    return  d

# Liste des distances :
d = [calcule_distance(k) for k in net._get_list_id()]

def calcule_distance2(emetteur_id,recepteur_id) :
    """Calcule la distance entre emetteur_id et recepteur_id."""
    d = []
    t = [emetteur_id]
    k = 0
    while not recepteur_id in t :
        k = k + 1
        # print(k)
        r = t.copy()
        for j in r :
             for v in net._get_voisins_emet(j) :
                t.append(v)
    return k

def Trouve_min(emetteur_id,Noeuds) :
    """ Trouve le noeud le plus proche. (Pas _get_voisins,
    car Noeud peut varier.) """
    mini = 1000
    noeud = emetteur_id
    for i in Noeuds :
        if d[emetteur_id][i] < mini and d[emetteur_id][i] != 0 :
            mini = d[emetteur_id][i]
            noeud = i
    return noeud

def maj_distance(emetteur_id, n1, n2, distance, predecesseur):
    """ Calcule le prédecesseur de n2 sur le chemin (emet_id -> n2).
    Faut-il passer par n1 ? Si oui, n1 devient le prédecesseur de n2.
    distance est la liste des distances entre tous le spoints du réseau.
    predecesseur est le chemin."""
    dist_emet_n2 = distance[emetteur_id][n2]
    dist_emet_n1_n2 = distance[emetteur_id][n1] + distance[n1][n2]
    
    if dist_emet_n2 >= dist_emet_n1_n2:
        dist_emet_n2 = dist_emet_n1_n2
        predecesseur[n2] = n1
    return predecesseur


def recherche_chemin(emetteur_id,dest_id) :
    
    Chemin = []
    d_maj = d.copy() #liste des distances entre les points
    Noeuds = net._get_list_id() #liste des noeuds considérés
    n = len(Noeuds)
    predecesseur = [-1]* n
    s1 = Trouve_min(emetteur_id,Noeuds)# noeud le plus proche de
                                       #l'émetteur, puis du suivant...
    predecesseur[s1] = emetteur_id # A l'init, on connaît un
                                   # prédecesseur de s1 : emetteur_id

    
    while n != 0 : # Noeuds != [] :
        # variant n est le nombre de noeuds considérés
        
        s1 = Trouve_min(emetteur_id,Noeuds)
        #print('s1 :',s1)
        #print("Noeuds ", Noeuds)
        Noeuds.pop(Noeuds.index(s1))
        n -= 1
        #print('predecesseur :',predecesseur)
        for s2 in net._get_voisins_emet(s1) :
            #print('s2 :',s2)
            predecesseur = maj_distance(emetteur_id, s1, s2, d_maj, predecesseur)
            #print('predecesseur :',predecesseur)
        # n = n_debut -1

    #print('Sortie predecesseur :',predecesseur)
    s = dest_id

    
    
    while s != emetteur_id :
        #print(Chemin)
        Chemin.append(s)
        #print(Chemin)
        s = predecesseur[s]
        # s = predecesseur[predecesseur.index(s)]
    Chemin.append(s)
    Chemin.reverse()
    return Chemin
