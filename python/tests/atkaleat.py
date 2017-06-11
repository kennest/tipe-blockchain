import time as t

from modelisation.fonctionnement import diff_aleatoire, init_info, boucle
from modelisation import est_connexe, conv_net_to_matrix, reseau_aleatoire
from modelisation.fichiers import ecrit_csv
from graphes import graphe
try:
    import matplotlib.pyplot as plt # voir
    # http://www.science-emergence.com/Articles/Tutoriel-Matplotlib/
except ModuleNotFoundError: # Si jamais exécuté sur un ordinateur
    # n'ayant pas matplotlib
    pass

#import numpy as np

iterations = 10 #nombre de passages pour un même nombre d'attaquants

def test_atkaleat(n, nb_tun, nbr_fichier):
    """Lance une batterie de tests sur des réseaux générés 
    aléatoirement, en faisant varier le nombre d'attaquants."""

    nom_fichier = "../resultats/atkaleat/" + "atkaleat-" + str(n) +\
                  "-"+ str(nb_tun) +"-"+ str(nbr_fichier)
    resultats = [] # tableau contenant les résultats de la simulation

    temps_init = t.monotonic()
    
    for k in range(iterations):
        print("Temps écoulé : " + str(t.monotonic() - temps_init) +\
              " s")
        print("Progression : " + str(k/iterations * 100) + "%")
        #nombre de tests avec p attaquants
        net_init = reseau_aleatoire(n, nb_tun)
        init_info(net_init, n-1, n-2)
        for p in range(n): #avec p attaquants, n-1 sera le
            #        dernier agent non attaquant, n-2 l'avant-dernier
            net = net_init.copy()
        
        # Ensuite, nous initialisations p agents qui seront attaquants
            for i in range(p):
                ag = net._get_agent(i)
                ag.strategie = "attaque"
            boucle(net, n)
            
            # Calcul du nombre de 'vrai' et de 'faux'
            #
            vrai = 0
            faux = 0
            for agent in net.agents:
                try: # En principe, le try est inutile, mais
                     # intéressant pour faire des tests
                    info = agent.informations[0]
                    assert info.id == 0 # l'information transmise
                    #                      a pour id 0
                    if info.infotxt == 'faux':
                        faux += 1
                    elif info.infotxt == 'vrai':
                        vrai += 1
                    else:
                        print("Erreur ! Le texte de l'information est invalide !")
                except:
                    print("Erreur, {} agents et {} attaquants ({} tunnels)".format(n, p, nb_tun))
                    print("Connexe : " + str(est_connexe(net)))
                    print(net)
            resultats.append((p, vrai, faux))
    print("Temps écoulé : " + str(t.monotonic() - temps_init) + " s")
    print("Progression : " + str(k/iterations * 100) + "%")

    ecrit_csv(resultats, nom_fichier)
    # Trace un graphe avec matplotlib
    les_x = [i/n for i in range(n)]
    les_vrais = [0 for i in range(n)]
    les_faux = [0 for i in range(n)]
    k = 0 # Compteur utilisé pour les deux boucles suivantes
    for res in resultats:
        (p, v, f) = res
        les_vrais[p] += v
        les_faux[p] += f
    for i in range(n):
        les_vrais[i] = les_vrais[i]/iterations/n
        les_faux[i] = les_faux[i]/iterations/n


    graphe(les_x, les_faux, nom_fichier, "Tracé avec "+str(n)+" nœuds et "+str(nb_tun)+" arêtes", "Proportion d'attaquants", "Proportion de réponses fausses")
    
    return resultats

