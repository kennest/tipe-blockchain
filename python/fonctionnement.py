import modelisation as md

net = md.reseau_etoile(10)
id_ag = 1
info1 = md.Information(0,3,"?")

def boucle_diffusion(net, agent0, info):
    """ Diffuse l'information info à partir de agent0.
    net : Reseau()
    agent0 : int
    info : Information()
    """
    info._add_passeur(agent0)
    net._get_agent(agent0)._add_info(info)
    
    list_vois = net._get_voisins_emet(agent0)
    for i in list_vois:
        if not( info1.id in net._get_agent(i)._get_list_info_id()):
            boucle_diffusion(net, i, info)
