from modelisation.fonctionnement import diff_aleatoire
from modelisation import est_connexe, conv_net_to_matrix
from modelisation.fichiers import ecrit_csv
import matplotlib.pyplot as plt
import numpy as np

iterations = 10 #nombre de passages pour un même nombre d'attaquants

def test_atkaleat(n, nb_tun, nbr_fichier):
    """Lance une batterie de tests sur des réseaux générés aléatoirement, en 
    faisant varier le nombre d'attaquants."""

    nom_fichier = "atkaleat-" + str(n) +"-"+ str(nb_tun) +"-"+ str(nbr_fichier)
    resultats = [] # tableau contenant les résultats de la simulation
    
    for p in range(n): #avec p attaquants
        for k in range(iterations): #nombre de tests avec p attaquants
            # n-1 sera le dernier agent non attaquant, n-2 l'avant-dernier
            net = diff_aleatoire(n, nb_tun, p, n-1, n-2)
            
            
            
            # Calcul du nombre de 'vrai' et de 'faux'
            #
            vrai = 0
            faux = 0
            for agent in net.agents:
                try:
                    info = agent.informations[0]
                    assert info.id == 0 # l'information transmise a pour id 0
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
    ecrit_csv(resultats, nom_fichier)
    # Trace un graphe avec matplotlib
    les_x = [i for i in range(n)]
    les_vrais = []
    les_faux = []
    k = 0 # Compteur utilisé pour les deux boucles suivantes
    for i in range(n):
        sum = [0,0]
        for j in range(iterations):
            sum[0] = sum[0] + resultats[k][1]
            sum[1] = sum[1] + resultats[k][2]
            k += 1
        les_vrais.append(sum[0]/iterations)
        les_faux.append(sum[1]/iterations)
    
    plt.clf()
    plt.plot(les_x, les_vrais)
    plt.plot(les_x, les_faux)
    plt.show()
    plt.savefig(nom_fichier + ".png")
    
    return resultats


