from modelisation.fonctionnement import diff_aleatoire
from modelisation import est_connexe

def test_atkaleat(n, nb_tun):
    """Lance une batterie de tests sur des réseaux générés aléatoirement, en 
    faisant varier le nombre d'attaquants."""
    
    resultats = [] # tableau contenant les résultats de la simulation
    
    for p in range(n): #avec p attaquants
        for k in range(10): #nombre de tests avec p attaquants
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
                    print(est_connexe(net))
            resultats.append((p, vrai, faux))
    return resultats