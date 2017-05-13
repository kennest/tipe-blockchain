import time as t

from modelisation.fonctionnement import diff_aleatoire, init_info, boucle
from modelisation import est_connexe, conv_net_to_matrix, scale_free
from modelisation.fichiers import ecrit_csv
try:
    import matplotlib.pyplot as plt # voir
    # http://www.science-emergence.com/Articles/Tutoriel-Matplotlib/
except ModuleNotFoundError: # Si jamais exécuté sur un ordinateur
    # n'ayant pas matplotlib
    pass

#import numpy as np

iterations = 10 #nombre de passages pour un même nombre d'attaquants



def test_atk_scale_free(n, nbr_fichier, showall):
    """Lance une batterie de tests sur des réseaux générés 
    aléatoirement, en faisant varier le nombre d'attaquants.
n: int
lambd: float
nbr_fichier: int
showall: bool"""

    nom_fichier = "../resultats/scale-free/" + "sf-" + str(n) +"-"+ str(nbr_fichier)
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

    ecrit_csv(resultats, nom_fichier)
    # Trace un graphe avec matplotlib
    les_x = [i for i in range(n)]
    les_vrais = [0 for i in range(n)]
    les_faux = [0 for i in range(n)]
    k = 0 # Compteur utilisé pour les deux boucles suivantes
    for res in resultats:
        (p, v, f) = res
        les_vrais[p] += v
        les_faux[p] += f
    for i in range(n):
        les_vrais[i] = les_vrais[i]/iterations
        les_faux[i] = les_faux[i]/iterations
 
    plt.clf()
    plt.plot(les_x, les_faux)
    plt.title("Tracé avec " + str(n) + " agents")
    plt.xlabel("Nombre d'attaquants")
    plt.ylabel("Nombre de réponses fausses")
    plt.savefig(nom_fichier + ".png")
    plt.show()
    
    return resultats
