import cmd
from modelisation.fonctionnement import *

class Interpreteur(cmd.Cmd):
    intro = "\nReseaux\n======="
    prompt = "} "
    
    def do_diffetoile(self, arg):
        """Lance la diffusion en étoile
        
        Paramètres :
        n : Nombre d'agents
        p : nombre d'attaquants (p<=n)
        centre : 1 si le centre est attaquant, 0 sinon
        emetteur : emetteur de l'information
        destinataire : destinataire de l'information"""
        (n, p, centre, emetteur, destinataire) = parse_nbr(arg)
        diff_etoile(n, p, centre, emetteur, destinataire)
    
    def do_quitter(self, arg):
        """Quitte le programme"""
        print("Au revoir\n")
        return True
    
def parse_nbr(arg):
    """Retourne un tuple d'entiers avec un argument sous forme de chaîne 
    de caractères."""
    return tuple(map(int, arg.split()))

def launch():
    c = Interpreteur()
    c.cmdloop()