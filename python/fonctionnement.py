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
    
    ##Initialisation :
    #L'id de l'émetteur est ajoutée à l'info, et l'info est ajoutée à
    #l'émetteur.
    info._add_passeur(agent0)
    net._get_agent(agent0)._add_info(info)
    
    list_vois = net._get_voisins_emet(agent0)
    for i in list_vois:
        
        # Si l'agent ne possède pas encore l'information :
        if not( info.id in net._get_agent(i)._get_list_info_id()):
            
            #copie pour éviter les problèmes d'alias sur la liste
            #des destinataires
            infobis = info.copy()
            #par récurrence, la diffusion est effectuée
            boucle_diffusion(net, i, infobis) 

