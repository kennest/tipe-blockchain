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
