import time as t

from modelisation.fonctionnement import diff_aleatoire, init_info, boucle
from modelisation import est_connexe, conv_net_to_matrix, scale_free
from modelisation.fichiers import ecrit_csv
from graphes import graphe, graphe_full
try:
    import matplotlib.pyplot as plt # voir
    # http://www.science-emergence.com/Articles/Tutoriel-Matplotlib/
except ModuleNotFoundError: # Si jamais exécuté sur un ordinateur
    # n'ayant pas matplotlib
    pass

#import numpy as np

#iterations = 10 #nombre de passages pour un même nombre d'attaquants



def test_atk_scale_free(n, nbr_fichier, showall, iterations):
    """Lance une batterie de tests sur des réseaux générés 
    aléatoirement, en faisant varier le nombre d'attaquants.
n: int
lambd: float
nbr_fichier: int
showall: bool"""

    savename = "../resultats/scale-free/" + "sf-" + str(n) +"-"+ str(nbr_fichier) +"-it" + str(iterations)
    resultats = [] # tableau contenant les résultats de la simulation

    temps_init = t.monotonic()
    
    for k in range(iterations):
        print("Temps écoulé : " + str(t.monotonic() - temps_init) +\
              " s")
        print("Progression : " + str(k/iterations * 100) + "%")
        #nombre de tests avec p attaquants
        net_init = scale_free(n)
        for p in range(n): #avec p attaquants, n-1 sera le
            #        dernier agent non attaquant, n-2 l'avant-dernier
            net = net_init.copy()
            
            init_info(net, n-1, n-2)
        
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
                    """print("Erreur, {} agents et {} attaquants ({} lambda)".format(n, p, lambd))"""
                    print("Connexe : " + str(est_connexe(net)))
                    """print(net)"""
            resultats.append((p, vrai, faux))
    print("Temps écoulé : " + str(t.monotonic() - temps_init) + " s")
    print("Progression : " + str(k/iterations * 100) + "%")

    ecrit_csv(resultats, savename)
    
    # Trace un graphe avec matplotlib
    les_x = [i/n for i in range(n)]

    title = "Scale-free, " + str(n) + " agents"
    xlabel = "Proportion d'attaquants"
    ylabel = "Proportion de réponses fausses"
    if showall:
        les_faux = [[0 for i in range(n)] for j in range(iterations)]
        k = 0
        for res in resultats:
            # p in range(n)
            p, v, f = res
            les_faux[k][p] += f/n
            if p == n-1:
                k += 1
        graphe_full(les_x, les_faux, savename, title, xlabel, ylabel)
            
            
    else:
        les_faux = [0 for i in range(n)]
        for res in resultats:
            (p, v, f) = res
            les_faux[p] += f/n
        for i in range(n):
            les_faux[i] = les_faux[i]/iterations
 
        graphe(les_x, les_faux, savename, title, xlabel, ylabel)   
    return resultats
