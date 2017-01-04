"""TIPE"""


class Agent:
    """Les agents sont les noeuds du réseau (utilisateurs). """
    def __init__(self):
        self.id = 0
        self.strategie = "normal"
        self.informations = []

    def _set_id(self, ag_id):
        """Change l'id de l'agent."""
        self.id = ag_id

    def _add_info(self, info):
        """Ajoute une information au noeud."""
        self.informations.append(info)

    def prinfo(self):
        print("id: " + str(self.id))
        print("Informations:")
        for i in self.informations:
            i.prinfo()
            
    def _get_list_info_id(self):
        list_id = []
        for i in self.informations:
            list_id.append(i.id)
        return list_id
    


class Tunnel:
    def __init__(self):
        self.emetteur = 0
        self.recepteur = 0

    def _set_emetteur(self,id_emetteur):
        self.emetteur = id_emetteur

    def _set_recepteur(self,id_recepteur):
        self.recepteur = id_recepteur

    def prinfo(self):
        print("Récepteur : "+str(self.recepteur))
        print("Emetteur : "+str(self.emetteur))

    
    
            
class Informations:
    def __init__(self):
        self.id = 0
        self.passeurs = []
        self.destinataire = 0
        # ajouter un champ requête et un champ réponse ?
        
    def _set_id(self, inf_id):
        """Change l'id de l'information."""
        self.id = inf_id

    def _add_destinataire(self, ag_id):
        """ """
        self.destinataire = ag_id
        
    def _add_passeur(self,ag_id):
        self.passeurs.append(ag_id)

    def prinfo(self):
        print("id: " + str(self.id))
        print("destinataire: " + str(self.destinataire))
        print("passeurs: " + str(self.passeurs))

    


class Reseau:
    def __init__(self):
        self.agents = []
        self.tunnels = []

    def prinfo(self):
        """Affiche la liste des agents du réseau."""
        print([ag.id for ag in self.agents])

    def _get_list_id(self):
        """Récupère la liste des agents du réseau."""
        return [ag.id for ag in self.agents]

    def _set_agent(self, ag_id):
        """Ajoute un agent d'id ag_id à la liste agents. Si l'id est
    déjà utilisée, échoue."""
        # Ajouter le fait que ça échoue si l'id est déjà prise
        x = Agent()
        x._set_id(ag_id)
        self.agents.append(x)
        
    def _set_list_agents(self, liste):
        """ Ajoute une liste d'agents au réseau."""
        for i in liste:
            self._set_agent(i)
        
    def _get_agent(self, ag_id):
        """Retourne l'agent d'id ag_id. Si il n'existe pas, renvoie False."""
        for x in self.agents:
            if x.id == ag_id:
                return x
        return False

    def _set_tunnel(self,id_emetteur,id_recepteur):
        """Ajoute un tunnel entre l'émetteur d'id id_emetteur et
        le récepteur d'id id_recepteur. Echoue si ce tunnel existe déjà."""
        list_tunnels = self._get_list_tunnels()
        if not((id_emetteur,id_recepteur) in list_tunnels):
            t = Tunnel()
            t._set_emetteur(id_emetteur)
            t._set_recepteur(id_recepteur)
            self.tunnels.append(t)
        else:
            pass

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


# Génération de certains types de réseau

def reseau_sans_tunnel(n):
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
