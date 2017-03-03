"""TIPE"""

import random

class Agent:
    """Les agents sont les noeuds du réseau (utilisateurs)."""
    def __init__(self, id, strategie = "normal"):
        self.id = id
        self.strategie = strategie
        self.informations = []

    def _set_id(self, ag_id):
        """Change l'id de l'agent."""
        self.id = ag_id

    def _add_info(self, info):
        """Ajoute une information au noeud."""
        self.informations.append(info)

    def __str__(self):
        print("id: " + str(self.id))
        print("Informations:")
        for i in self.informations:
            print(i)
    
    def copy(self):
		""" Retourne un agent ayant les mêmes caractéristiques, en 
		évitant les problèmes d'alias."""
		
		
		
    def _get_list_info_id(self):
        list_id = []
        for i in self.informations:
            list_id.append(i.id)
        return list_id
    
    def envoyer_info(self, recepteur, info, list_voisins):
        """Envoie une information à un voisin.
        
        recepteur : Agent
        info : Information
        list_voisins : liste des voisins, int list"""
        assert (recepteur.id in list_voisins)
        if not info.id in recepteur._get_list_info_id():
            # Ne pas renvoyer une information que le voisin possède déjà
            infobis = info.copy()
            infobis._add_passeur(recepteur.id)
            recepteur._add_info(infobis)
    
    def _get_info(self, i):
        """ Récupère l'information d'id i possédée par l'agent """
        assert (i in self._get_list_info_id())
        for info in self.informations:
            if info.id == i:
                return info
        
    


class Tunnel:
    def __init__(self, emet, recep):
        self.emetteur = emet
        self.recepteur = recep

    def _set_emetteur(self,id_emetteur):
        self.emetteur = id_emetteur

    def _set_recepteur(self,id_recepteur):
        self.recepteur = id_recepteur

    def __str__(self):
        print("(" + str(self.emetteur) + "> " + str(self.recepteur) + ")")

    
    
            
class Information:

    def __init__(self, id, destinataire, infotxt):
        self.id = id
        self.passeurs = []
        self.destinataire = destinataire
        self.infotxt = infotxt
        # ajouter un champ requête et un champ réponse ?
        
    def _set_id(self, inf_id):
        """Change l'id de l'information."""
        self.id = inf_id

    def _set_destinataire(self, ag_id):
        """ """
        self.destinataire = ag_id
    
    def _set_info(self, infotxt):
        """ info : str """
        self.info = infotxt
        
    def _add_passeur(self,ag_id):
        """ Ajoute l'agent d'id ag_id à la liste des passeurs."""
        self.passeurs.append(ag_id)

    def __str__(self):
        print("id: " + str(self.id))
        print("destinataire: " + str(self.destinataire))
        print("passeurs: " + str(self.passeurs))
        print("Info: " + self.infotxt)
     
    def _set_information(self, id, destinataire, infotxt):
        _set_id(self, id)
        _set_destinataire(self, destinataire)
        _set_info(self, infotxt)
    
    def copy(self):
        """Renvoie une information identique (pour éviter les problèmes d'alias)."""
        infocopy =  Information(self.id, self.destinataire, self.infotxt)
        infocopy.passeurs = [x for x in self.passeurs]
        return infocopy
    


class Reseau:
    def __init__(self):
        self.agents = []
        self.tunnels = []

    def __str__(self):
        """Affiche la liste des agents du réseau."""
        print([ag.id for ag in self.agents])
        print(tunnel for i in self.tunnels)
    
    def copy(self):
		"""Retourne un réseau identique, en évitant les problèmes d'alias."""
		agents = [a.copy() for a in self.agents]
		tunnels = self.tunnels
		net = Reseau(agents, tunnels)

    def _get_list_id(self):
        """Récupère la liste des agents du réseau."""
        return [ag.id for ag in self.agents]

    def _set_agent(self, ag_id):
        """Ajoute un agent d'id ag_id à la liste agents. Si l'id est
    déjà utilisée, échoue."""
        # Ajouter le fait que ça échoue si l'id est déjà prise
        x = Agent(ag_id)
        x._set_id(ag_id)
        self.agents.append(x)
        
    def _set_list_agents(self, liste):
        """ Ajoute une liste d'agents au réseau."""
        for i in liste:
            self._set_agent(i)
        
    def _get_agent(self, ag_id):
        """Retourne l'agent (objet "Agent") d'id ag_id. Si il n'existe pas, renvoie False."""
        for x in self.agents:
            if x.id == ag_id:
                return x
        return False

    def _set_tunnel(self,id_emetteur,id_recepteur):
        """Ajoute un tunnel entre l'émetteur d'id id_emetteur et
        le récepteur d'id id_recepteur. Echoue si ce tunnel existe déjà."""
        list_tunnels = self._get_list_tunnels()
        #if not((id_emetteur,id_recepteur) in list_tunnels):
        t = Tunnel(id_emetteur, id_recepteur)
        t._set_emetteur(id_emetteur)
        t._set_recepteur(id_recepteur)
        self.tunnels.append(t)

    def _set_tunnel_double(self, id_1, id_2):
        self._set_tunnel(id_1, id_2)
        self._set_tunnel(id_2, id_1)
        

    def _get_tunnel(self,id_emetteur,id_recepteur):
        """Retourne le tunnel entre l'agent d'id id_emetteur et le récepteur
        d'id id_recepteur. S'il n'y en a pas, retourne False."""
        for t in self.tunnels:
            if (t.emetteur,t.recepteur) == (id_emetteur,id_recepteur):
                return t #(t.emetteur,t.recepteur)
        return False

    def _get_list_tunnels(self):
        """Récupère la liste des tunnels du réseau."""
        return [(t.emetteur,t.recepteur) for t in self.tunnels]

    def _get_voisins_emet(self,ag_id):
        """Retourne la liste des voisins vers lesquels peut émettre
    l'agent d'id ag_id."""
        t = self._get_list_tunnels()
        voisins_emet = []
        for i in t :
            if i[0] == ag_id :
                voisins_emet.append(i[1])
        return voisins_emet
        
    def _get_voisins_recep(self,ag_id):
        """Retourne la liste des voisins depuis lesquels peut recevoir
    l'agent d'id ag_id."""
        t = self._get_list_tunnels()
        voisins_recep = []
        for i in t :
            if i[1] == ag_id :
                voisins_recep.append(i[0])
        return voisins_recep


## Liens avec csv et matrices
        
def conv_net_to_matrix(net):
    """ Retourne une matrice représentant le réseau. La ligne j
    correspond à l'émetteur d'id i."""
    n = len(net._get_list_id())
    mat = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        voisins = net._get_voisins_emet(i)
        for j in voisins:
            mat[i][j] = 1
    return mat

def matrix_to_csv(matrice, filename):
    """ Prend en argument une matrice carrée et écrit un fichier csv
    la représentant. """
    with open(filename + '.csv', 'w') as f:
        for j in matrice:
            for i in range(len(j)):
                j[i] = str(j[i])
            text = ','.join(j)
            f.write(text)
            f.write("\n")
    return True

def csv_to_matrix(filename):
    """ Lis le fichier filename.csv et retourne la matrice
    représentée par le fichier.""" 
    mat = []
    with open(filename + '.csv', 'r') as f:
        text = f.readlines()
        for line in text:
            listi = line.split(',')
            for i in range(len(listi)):
                listi[i] = int(listi[i])
            mat.append(listi)
    return mat

def conv_matrix_to_net(matrice):
    net = Reseau()
    n = len(matrice)
    for i in range(n):
        net._set_agent(i)
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:
                net._set_tunnel(i,j)
    return net


## Génération de certains types de réseau

##Fonction fausse
#def est_connexe(net):
#    """Retourne True si le graphe est connexe, False sinon."""
#    M = conv_net_to_matrix(net)
#    Noeuds_visités = [0]*len(M)
    #Noeuds_à_visiter = [0]*len(M)

#    t = [0] #noeuds à visiter
#    for k in range(len(M)) :
#        r = t.copy()
#        for n in r :
#            Noeuds_visités[n] = 2
#            if Noeuds_visités == [2]*len(M) :
#                return True
#            t.pop(t.index(n))
#            for i in range(len(M)) :
#                if M[n][i] == 1 :
#                    t.append(i)
#    return False


##A optimiser si possible
def est_connexe(net):
    n = len(net.agents)

    for j in range(n):
        visite = [False for i in range(n)]

        q = [j]
        while q != []:
            k = q.pop()
            visite[k] = 1
            voisins = net._get_voisins_emet(k)
            for v in voisins:
                if visite[v] == 0:
                    q.append(v)
        
    
    if visite == [True for i in range(n)]:
        return True
    return False

def reseau_sans_tunnel(n):
    """Génère un réseau de n noeuds, sans tunnels pour les relier."""
    net = Reseau()
    liste = [i for i in range(n)]
    net._set_list_agents(liste)
    return net

def reseau_etoile(n):
    """ Génère un réseau en étoile de taille n :
    pour tout i appartenant à [1,n] chaque noeud i est lié
    avec le noeud 0 en émetteur et récepteur."""
    net = reseau_sans_tunnel(n)
    for i in range(1,n):
        net._set_tunnel_double(0,i)
    return net

def reseau_complet(n):
    """ Génère un réseau ayant la structure d'un graphe complet de n
    noeuds. """
    net = reseau_sans_tunnel(n)
    for i in range(n):
        for j in range(n):
            if i !=j:
                net._set_tunnel_double(i,j)
    return net

def gen_ens_aleat(n, m, M, y):
    """Génère un ensemble à n éléments, compris entre m (inclus) et M (exclus), diff�rents de x."""
    if M-m < n:
        raise IntervalError("""Les bornes de l'intervalle sont trop rapprochées
        par rapport au nombre d'éléments""")
    ens = []
    while len(ens) < n:
        x = random.randint(m, M-1)
        if not (x in ens) and x != y:
            ens.append(x)
    return ens


## A optimiser, il faudrait générer un réseau valide du premier coup !
def reseau_aleatoire(n,p):
    """Génère un réseau de taille n, avec chaque agent lié à p autres."""
    net = reseau_sans_tunnel(n)
    for i in range(n):
        voisins = gen_ens_aleat(p, 0, n, i)
        for vois in voisins:
            net._set_tunnel(i, vois)
            
    if not(est_connexe(net)):
        net = reseau_aleatoire(n, p)
    return net
