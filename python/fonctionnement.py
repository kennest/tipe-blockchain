import modelisation as md

##Variables utilisables pour les tests 

net = md.reseau_etoile(10)
id_ag = 1
info1 = md.Information(0,3,"?")


##Définition des fonctions

def iteration(net):
    """Itération d'une boucle
    
    A chaque boucle, tous les agents font un 'tour d'action' sur le réseau. (modèle multi-agents)"""
    
    agents = net._get_list_id()
    for i in agents:
        

def boucle_diffusion(net, agent0, info):
    """ Diffuse l'information info à partir de agent0.
    net : Reseau()
    agent0 : int
    info : Information()
    """
    ##A faire
    #Modifier pour intégrer le comportement d'un attaquant
    
    ##Initialisation :
    #L'id de l'émetteur est ajoutée à l'info, et l'info est ajoutée à
    #l'émetteur.
    info._add_passeur(agent0)
    net._get_agent(agent0)._add_info(info)
    
    ##Diffusion vers les voisins
    list_vois = net._get_voisins_emet(agent0)
    for i in list_vois:
        
        agent_i = net._get_agent(i)
        # Si l'agent ne possède pas encore l'information :
        if not( info.id in agent_i._get_list_info_id()):
            if agent_i.strategie == "normal":
                #copie pour éviter les problèmes d'alias sur la liste
                #des destinataires
                infobis = info.copy()
                #par récurrence, la diffusion est effectuée
                boucle_diffusion(net, i, infobis)
            elif agent_i.strategie == "attaque":
                infobis = info.copy()
                infobis.infotxt = "faux"
                boucle_diffusion(net, i, infobis)

def diff_etoile(n, p, centre, emetteur, destinataire):
    """ Génère un réseau en étoile de taille n avec p attaquants. (p<n)
    Si centre = True, l'agent 0 sera un attaquant. Sinon, c'est un agent normal."""
    
    ##Initialisation
    net = md.reseau_etoile(n)
    if centre:
        for i in range(p):
            net._get_agent(i).strategie = "attaque"
    else:
        for i in range(1,p+1):
            net._get_agent(i).strategie = "attaque"
    
    info = md.Information(0, destinataire, "vrai")
    
    ##Diffusion
    boucle_diffusion(net, emetteur, info)
    
    ##Affichage des résultats
    for i in range(n):
        print("  ----  ")
        net._get_agent(i).prinfo()
        
def diff_aleatoire(n, nb_tun, p, emetteur, destinataire):
    """ Génère un réseau en aléatoire de taille n, avec nb_tun tunnels partant 
    de chaque noeud, avec p attaquants. (p<n)
    """
    ##Problèmes !
    
    ##Initialisation
    net = md.reseau_aleatoire(n, nb_tun)
    for i in range(p):
            net._get_agent(i).strategie = "attaque"
    
    info = md.Information(0, destinataire, "vrai")
    
    ##Diffusion
    boucle_diffusion(net, emetteur, info)
    
    ##Affichage des résultats
    for i in range(n):
        print("  ----  ")
        net._get_agent(i).prinfo()