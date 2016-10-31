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
    voisins = net._get_voisins(emetteur_id)
    list_id_emet = emetteur._get_list_info_id() #liste des id des
                            # informations que possède emetteur
    assert information.id in list_id_emet
    assert dest_id in voisins$
    
    information._add_passeur(dest_id)
    information.prinfo()
    net._get_agent(dest_id)._add_info(information)
    
def actions_agent(agent):
    """Réalise les actions entre les agents, depuis l'agent 'agent'."""
    ag_id = agent.id
    voisins_id = net._get_voisins(ag_id)
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

"""
for i in range(10):
    for agent in net.agents:
        actions_agent(agent)
"""
