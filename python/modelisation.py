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
        
    def _set_id(self, inf_id):
        """Change l'id de l'information."""
        self.id = inf_id

    def _add_destinataire(self, ag_id):
        self.destinataire = ag_id
        
    def _add_passeur(self,ag_id):
        self.passeurs.append(ag_id)

    def prinfo(self):
        print("id: " + str(self.id))
        print("passeurs: " + str(self.destinataire))

    


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
        assert not((id_emetteur,id_recepteur) in list_tunnels)
        t = Tunnel()
        t._set_emetteur(id_emetteur)
        t._set_recepteur(id_recepteur)
        self.tunnels.append(t)

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

    def _get_voisins(self,ag_id):
        """Retourne la liste des voisins de l'agent d'id ag_id."""
        t = self._get_list_tunnels()
        voisins = []
        for i in t :
            if i[0] == ag_id :
                voisins.append(i[1])
            elif i[1] == ag_id :
                voisins.append(i[0])
        return voisins
        
    
        

        
    
