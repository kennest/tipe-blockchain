import modelisation as mod
import heapq as hq #Pour implémenter des files de priorité

## Initialisation du réseau
net = mod.Reseau()

for i in range(10):
    net._set_agent(i)

liens = [(0,3),(0,4), (1,2),(1,5), (2,0),(2,1), (3,4),(3,5),(3,8),(3,9), \
         (4,0), (5,1),(5,2),(5,6), (6,3), (7,3),(7,9), (8,3), (9,0),(9,7)]
for lien in liens:
    net._set_tunnel(lien[0], lien[1])



##
#
# Recherche la distance entre deux noeuds par l'algorithme de Djikstra
#
##

#hq.heapify()

predecesseur = [1000]*10
# d : distances calculées à la main, pour vérification
"""d = [[0,3,3,1,1,2,3,3,2,2],[2,0,1,3,3,1,6,5,4,4],[1,1,0,2,2,2,3,4,3,3],\
     [2,2,2,0,1,1,2,2,1,1],[1,4,4,2,0,3,4,4,3,3],[2,1,2,2,3,0,1,4,3,3],\
     [3,3,3,1,2,2,0,3,2,2],[2,3,3,2,2,3,0,2,1],[3,3,3,1,2,2,3,3,0,2],\
     [1,4,4,2,2,3,4,1,3,0]]"""



def calcule_distance(emetteur_id) :
    """Calcule la distance d'emetteur_id à tous les noeuds du réseau."""
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
