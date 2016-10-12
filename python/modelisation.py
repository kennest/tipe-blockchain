class Agent:
    """Les agents sont les noeuds du réseau (utilisateurs). """
    def __init__(self):
        self.id = 0
        self.strategie = "normal"

    def _set_id(self, ag_id):
        self.id = ag_id
        
    def _get_voisins(self):
        pass


class Tunnel:
    def __init__(self):
        self.emetteur = 0
        self.recepteur = 0
    
    def _set_emetteur(self,id_emetteur):
        self.emetteur = id_emetteur

    def _set_recepteur(self,id_recepteur):
        self.recepteur = id_recepteur

class Informations:
    def __init__(self):
        self.id = 0


class Reseau:
    def __init__(self):
        self.agents = []
        self.tunnels = []

    def _get_list_id(self):
        """Récupère la liste des id des agnets du réseau."""
        return [ag.id for ag in self.agents]
                
    def _set_agent(self, ag_id):
        """Ajoute un agent d'id ag_id à la liste agents. Si l'id est
    déjà utilisée, échoue."""
        # Echoue si l'id est déjà prise
        list_id = self._get_list_id()
        assert not(ag_id in list_id)
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
                return (t.emetteur,t.recepteur)
        return False

    def _get_list_tunnels(self):
        """Récupère la liste des tunnels du réseau."""
        return [(t.emetteur,t.recepteur) for t in self.tunnels]
    

