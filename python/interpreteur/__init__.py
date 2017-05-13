import cmd
import argparse
from modelisation.fonctionnement import *
from tests.atkaleat import test_atkaleat
from tests.scale_free import test_atk_scale_free


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
        
    def do_diffaleat(self, arg):
        """Lance la diffusion sur un réseau aléatoire
        
        Paramètres :
        n : Nombre d'agents
        nb_tun : nombre de tunnels
        p : nombre d'attaquants (p<=n)
        emetteur : emetteur de l'information
        destinataire : destinataire de l'information"""
        
        # def parse(arg):
        #     """Traite les arguments de la fonction"""
        #     parser = argparse.ArgumentParser()
        #     parser.add_argument("echo")
        #     parser.parse_args()
        
        (n, nb_tun, p, emetteur, destinataire) = parse_nbr(arg)
        diff_aleatoire(n, nb_tun, p, emetteur, destinataire)
        
    def do_testatkaleat(self, arg):
        """Créé une fonction permettant de simuler un grand nombre de diffusion aléatoires à n et nb_tun fixés, en faisant varier p. Ensuite, trace une courbe représentant le nombre de 'vrais' par rapport aux 'faux'.
        
        Paramètres :
        n : nombre d'agents
        nb_tunnels : nombre de tunnels
        nbr_fichier : nombre ajouté au nom de fichier
        """
        (n, nb_tun, nbr_fichier) = parse_nbr(arg)
        r = test_atkaleat(n, nb_tun, nbr_fichier)
        #print(r)

    def do_testsf(self, arg):
        """Simule un grand nombre d'itérations sur des réseaux scale-free.

Paramètres :
n : nombre d'agents
lambd :
nbr_fichier : nombre ajouté au fichier"""
        n, nbr_fichier, showall = parse_testsf(arg)
        
        r = test_atk_scale_free(n, nbr_fichier, showall)
    
    def do_quitter(self, arg):
        """Quitte le programme"""
        print("Au revoir\n")
        return True


def parse_nbr(arg):
    """Retourne un tuple d'entiers avec un argument sous forme de chaîne 
    de caractères."""
    return tuple(map(float, arg.split()))

def parse_testsf(arg):
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Number of agents", type = int)
    parser.add_argument("filenumber", help="Number of the file", type = int, default = -1)
    parser.add_argument("--showall", "-s", help="Show all curves of iterations", action = "store_true")
    args = parser.parse_args(arg.split(" "))
    return args.n, args.filenumber, args.showall

    
def launch():
    c = Interpreteur()
    c.cmdloop()
