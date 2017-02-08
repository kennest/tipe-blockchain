import modelisation as md

##Variables utilisables pour les tests 

# net = md.reseau_etoile(10)
# id_ag = 1
# info1 = md.Information(0,3,"?")
# ag = net._get_agent(id_ag)
# ag0 = net._get_agent(0)
# ag2 = net._get_agent(2)




##Définition des fonctions

def iteration(net):
    """Itération d'une boucle
    
    A chaque boucle, tous les agents font un 'tour d'action' sur le réseau. 
    (modèle multi-agents)
    """
    
    list_agents_id = net._get_list_id()
    for i in list_agents_id:
        # L'agent i envoie les informations qu'il a envie d'échanger à ses 
        # voisins
        # 
        #
        agent = net._get_agent(i)
        if agent.strategie == "attaque":
            # print(i)
            # print("Attaque !")
            comportement_attaquant(net, agent)
        
        else:
            list_voisins = net._get_voisins_emet(i)
            
            for j in list_voisins:
                recepteur = net._get_agent(j)
                
                for k in agent._get_list_info_id():
                    info = agent._get_info(k)
                    agent.envoyer_info(recepteur, info, list_voisins)

def boucle(net, n):
    """Exécute n iterations"""
    for i in range(n):
        iteration(net)

def comportement_attaquant(net, attaquant):
    """Gère le comportement d'un agent attaquant"""
    list_voisins = net._get_voisins_emet(attaquant.id)
    for j in list_voisins:
        # Parcours de la liste des voisins
        recepteur = net._get_agent(j)
        
        for k in attaquant._get_list_info_id():
            # Parcours des informations
            info = attaquant._get_info(k)
            info.infotxt = "faux"
            #info.prinfo()
            attaquant.envoyer_info(recepteur, info, list_voisins)



# def boucle_diffusion(net, agent0, info):
#     """ Diffuse l'information info à partir de agent0.
#     net : Reseau()
#     agent0 : int
#     info : Information()
#     """
#     ##A faire
#     #Modifier pour intégrer le comportement d'un attaquant
#     
#     ##Initialisation :
#     #L'id de l'émetteur est ajoutée à l'info, et l'info est ajoutée à
#     #l'émetteur.
#     info._add_passeur(agent0)
#     net._get_agent(agent0)._add_info(info)
#     
#     ##Diffusion vers les voisins
#     list_vois = net._get_voisins_emet(agent0)
#     for i in list_vois:
#         
#         agent_i = net._get_agent(i)
#         # Si l'agent ne possède pas encore l'information :
#         if not( info.id in agent_i._get_list_info_id()):
#             if agent_i.strategie == "normal":
#                 #copie pour éviter les problèmes d'alias sur la liste
#                 #des destinataires
#                 infobis = info.copy()
#                 #par récurrence, la diffusion est effectuée
#                 boucle_diffusion(net, i, infobis)
#             elif agent_i.strategie == "attaque":
#                 infobis = info.copy()
#                 infobis.infotxt = "faux"
#                 boucle_diffusion(net, i, infobis)

def init_info(net, emetteur, destinataire):
    info = md.Information(0, destinataire, "vrai")
    info._add_passeur(emetteur)
    agent_emet = net._get_agent(emetteur)
    agent_emet._add_info(info)
    
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
    
    init_info(net, emetteur, destinataire)
    
    ##Diffusion
    boucle(net, 3) # Dans un réseau en étoile, un information se propage dans 
        # le réseau en au maximum 3 itérations
    
    ##Affichage des résultats
    for i in range(n):
        print("  ----  ")
        net._get_agent(i).prinfo()
        
def diff_aleatoire(n, nb_tun, p, emetteur, destinataire):
    """ Génère un réseau en aléatoire de taille n, avec nb_tun tunnels partant 
    de chaque noeud, avec p attaquants. (p<n)
    """
    
    ##Initialisation
    net = md.reseau_aleatoire(n, nb_tun)
    if not(md.est_connexe(net)):
        print("Graphe non connexe !")
    for i in range(p):
            net._get_agent(i).strategie = "attaque"
    
    init_info(net, emetteur, destinataire)
    
    ##Diffusion
    boucle(net, n) #S'il y a n agents, en n tours, l'informations sera arrivée
    
    ##Affichage des résultats
    # for i in range(n):
    #     print("  ----  ")
    #     net._get_agent(i).prinfo()

    ##Test si toutes les informations sont non vides
    for agent in net.agents:
        if agent.informations == []:
            print("Erreur, la liste de l'agent {} est vide !".format(agent.id))
    ## Retourne le réseau
    return net
    
    

##Script
# 
# net = diff_aleatoire(20,4,0,1,3)
# mat = md.conv_net_to_matrix(net)
# md.matrix_to_csv(mat, "res_aleat")