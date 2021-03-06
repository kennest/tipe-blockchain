"""
TESTS ONLY (probablement périmé)

Module pour exécuter des tests sur un petit réseau
"""
import modelisation as mod

## Initialisation du réseau
net = mod.Reseau()

for i in range(10):
    net._set_agent(i)

liens = [(0,3),(0,4), (1,2),(1,5), (2,0),(2,1), (3,4),(3,5),(3,8),(3,9), \
         (4,0), (5,1),(5,2),(5,6), (6,3), (7,3),(7,9), (8,3), (9,0),(9,7)]
for lien in liens:
    net._set_tunnel(lien[0], lien[1])

## Fonctions
def envoyer_info(information, emetteur_id, dest_id):
    """emetteur envoie information à l'agent d'id destinataire."""
    # Il faut faire attention aux alias !
    emetteur = net._get_agent(emetteur_id)


    
    voisins = net._get_voisins_emet(emetteur_id)
    list_id_emet = emetteur._get_list_info_id() #liste des id des
                            # informations que possède emetteur
    list_id_dest = net._get_agent(dest_id)._get_list_info_id() #liste
                            # des id des informations que possède
                            # le destinataire
    if information.id in list_id_dest:
        return None
    
    #Pour ne pas avoir de problème d'alias
    info_bis = mod.Informations()
    info_bis._set_id(information.id)
    passeurs_bis = information.passeurs.copy()
    info_bis.passeurs = passeurs_bis
    info_bis._add_destinataire(information.destinataire)
    
    assert information.id in list_id_emet
    assert dest_id in voisins
    info_bis._add_passeur(dest_id)
    net._get_agent(dest_id)._add_info(info_bis)
    
def actions_agent(agent):
    """Réalise les actions entre les agents, depuis l'agent 'agent'."""
    ag_id = agent.id
    voisins_id = net._get_voisins_emet(ag_id)
    for info in agent.informations:
        info_id = info.id
        for vois_id in voisins_id:
            if not info in net._get_agent(vois_id).informations:
                envoyer_info(info, ag_id, vois_id)



## Boucle principale
information0 = mod.Informations()
information0._add_passeur(0)
agent0 = net._get_agent(0)
agent0._add_info(information0) #pas de problème d'alias ici


for i in range(1):
    for agent in net.agents:
        actions_agent(agent)

for i in range(10):
    print(net.agents[i])
    print('---')


##
#
# Recherche la distance entre deux noeuds par l'algorithme de Djikstra
#
##
 
predecesseur = [1000]*10
# d : distances calculées à la main, pour vérification
d = [[0,3,3,1,1,2,3,3,2,2],[2,0,1,3,3,1,6,5,4,4],[1,1,0,2,2,2,3,4,3,3],\
     [2,2,2,0,1,1,2,2,1,1],[1,4,4,2,0,3,4,4,3,3],[2,1,2,2,3,0,1,4,3,3],\
     [3,3,3,1,2,2,0,3,2,2],[2,3,3,2,2,3,0,2,1],[3,3,3,1,2,2,3,3,0,2],\
     [1,4,4,2,2,3,4,1,3,0]]


def distance_min(emetteur_id,liste,d) :
    """ liste : liste de noeuds ? """
    mini = float("Infinity") # Valeur arbitraire, tous les chemins
                             # sont plus petits
    noeud = -1
    for x in liste :
        if d[emetteur_id][x] < mini :
            mini = d[emetteur_id][x]
            noeud = x
    return noeud

def maj_distance(emetteur_id,n1,n2,d) :
    if d[emetteur_id][n2] > d[emetteur_id][n1] + 1 :
        d[emetteur_id][n2] = d[emetteur_id][n1] + 1
        predecesseur[n2] = n1




    
def recherche_chemin(emetteur_id,dest_id) :
    """Recherche un plus court chemin dans le graphe entre l'émetteur et le destinataire."""
    Chemin = []
    d_maj = [[0,3,3,1,1,2,3,3,2,2],[2,0,1,3,3,1,6,5,4,4],[1,1,0,2,2,2,3,4,3,3],[2,2,2,0,1,1,2,2,1,1],[1,4,4,2,0,3,4,4,3,3],[2,1,2,2,3,0,1,4,3,3],[3,3,3,1,2,2,0,3,2,2],[2,3,3,2,2,3,0,2,1],[3,3,3,1,2,2,3,3,0,2],[1,4,4,2,2,3,4,1,3,0]]
    Q = net._get_list_id()

    while Q != [] :
        print(Q)
        s1 = distance_min(emetteur_id,Q,d_maj)
        print(s1)
        Q.pop(Q.index(s1))
        for s2 in net._get_voisins_emet(s1) :
            print(s2)
            maj_distance(emetteur_id,s1,s2,d_maj)
            print(predecesseur)
            
    
    
    s = dest_id
    while s != emetteur_id :
        Chemin.append(s)
        
        s = predecesseur[predecesseur.index(s)]

    return Chemin

def calcule_distance(emetteur_id) :
    d = []
    for i in net._get_list_id() :
        t = [emetteur_id]
        k = 0
        while not i in t :
            k = k + 1
            for j in t :
               for v in net._get_voisins_emet(j) :
                   t.append(v)
        d.append(k)
    return  d


