import matplotlib.pyplot as plt


def graphe(les_x, les_y, savename, title, xlabel, ylabel):
    """Trace un graphe avec en abscisse les_x, en ordonnée les_y, ayant pour titre title.
les_x: float list ou int list
les_y: float list ou int list
savename: str
title: str
xlabel: str
ylabel: str
"""
    plt.clf()
    plt.plot(les_x, les_y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()

def graphe_full(les_x, les_ys, savename, title, xlabel, ylabel):
    """Trace un graphe avec en abscisse les_x, en ordonnée les différentes données de les_ys, ayant pour titre title.
les_x: float list ou int list
les_ys: float list ou int list
savename: str
title: str
xlabel: str
ylabel: str
"""
    plt.clf()
    for y in les_ys:
        plt.plot(les_x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()

def graphe_deg_nbr():
    pass
    



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
 
    
