"""
Test sur des réseaux homogènes (ou réguliers)
"""
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
    # il ne sera pas possible de générer des graphes, mais les .csv le seront
    pass

#import numpy as np

iterations = 100 # nombre de passages pour un même nombre d'attaquants

def test_atkaleat(n, nb_tun, nbr_fichier):
    """Lance une batterie de tests sur des réseaux générés 
    aléatoirement, en faisant varier le nombre d'attaquants."""

    nom_fichier = "../resultats/atkaleat/" + "atkaleat-" + str(n) +\
                  "-"+ str(nb_tun) +"-"+ str(nbr_fichier) + "-i" + str(iterations)
    resultats = [] # tableau contenant les résultats de la simulation

    temps_init = t.monotonic() # temps_init sera la base de la mesure du temps
    
    for k in range(iterations):

        # Progression :
        print("Temps écoulé : " + str(t.monotonic() - temps_init) +\
              " s")
        print("Progression : " + str(k/iterations * 100) + "%")

        
        net_init = reseau_aleatoire(n, nb_tun)
        init_info(net_init, n-1, n-2) # l'info initiale
        
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
                     # on en avait besoin pour faire des tests
                    info = agent.informations[0]
                    assert info.id == 0 # l'information transmise
                    #                      a pour id 0
                    if info.infotxt == 'faux':
                        faux += 1
                    elif info.infotxt == 'vrai':
                        vrai += 1
                    else:
                        print("Erreur ! Le texte de l'information est invalide !")
                        
                except: # Normalement, jamais utilisé
                    print("Erreur, {} agents et {} attaquants ({} tunnels)".format(n, p, nb_tun))
                    print("Connexe : " + str(est_connexe(net)))
                    print(net)
            resultats.append((p, vrai, faux))
    print("Temps écoulé : " + str(t.monotonic() - temps_init) + " s")
    print("Progression : " + str(k/iterations * 100) + "%")

    # On enregistre un .csv avec les résultats :
    ecrit_csv(resultats, nom_fichier)
    
    # Tracé du graphe avec matplotlib
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


    graphe(les_x, les_faux, nom_fichier, "Réseau homogène "+str(n)+" nœuds et "+str(nb_tun)+" arêtes", "Proportion d'attaquants", "Proportion d'informations fausses")
    
    return resultats

