import cmd
import argparse
from modelisation.fonctionnement import *
from tests.atkaleat import test_atkaleat
from tests.scale_free import test_atk_scale_free


class Interpreteur(cmd.Cmd):
    intro = "\nReseaux\n======="
    prompt = "} "
    
    def do_diffetoile(self, arg):
        (n, p, centre, emetteur, destinataire) = parse_nbr(arg)
        diff_etoile(n, p, centre, emetteur, destinataire)

    def help_diffetoile(self):
        print("""Lance la diffusion en étoile
        Paramètres :
        n : Nombre d'agents
        p : nombre d'attaquants (p<=n)
        centre : 1 si le centre est attaquant, 0 sinon
        emetteur : emetteur de l'information
        destinataire : destinataire de l'information""")
        
    def do_diffaleat(self, arg):
        # def parse(arg):
        #     """Traite les arguments de la fonction"""
        #     parser = argparse.ArgumentParser()
        #     parser.add_argument("echo")
        #     parser.parse_args()
        
        (n, nb_tun, p, emetteur, destinataire) = parse_nbr(arg)
        diff_aleatoire(n, nb_tun, p, emetteur, destinataire)

    def help_diffaleat(self, arg):
        print("""Lance la diffusion sur un réseau aléatoire
        
        Paramètres :
        `n` : Nombre d'agents
        nb_tun : nombre de tunnels
        p : nombre d'attaquants (p<=n)
        emetteur : emetteur de l'information
        destinataire : destinataire de l'information""")

        
    def do_testatkaleat(self, arg):
        """Créé une fonction permettant de simuler un grand nombre de diffusion aléatoires à n et nb_tun fixés, en faisant varier p. Ensuite, trace une courbe représentant le nombre de 'vrais' par rapport aux 'faux'.
        
        Paramètres :
        n : nombre d'agents
        nb_tunnels : nombre de tunnels
        nbr_fichier : nombre ajouté au nom de fichier
        """
        (n, nb_tun, nbr_fichier) = parse_nbr(arg)
        r = test_atkaleat(int(n), int(nb_tun), int(nbr_fichier))
        #print(r)

    def do_testsf(self, arg):
        """Simule un grand nombre d'itérations sur des réseaux scale-free.

Paramètres :
n : nombre d'agents
filenbr: nombre ajouté au fichier
-i <iterations>: int
-s: showall: flag
-g: type de graphe"""
        
        args = parsersf.parse_args(arg.split(" "))
        n, nbr_fichier, showall, iterations, gtype = args.n, args.filenumber, args.showall, args.iterations, args.gtype
        
        r = test_atk_scale_free(n, nbr_fichier, showall, iterations, gtype)

    def help_testsf(self):
        print("""Simule un grand nombre d'itérations sur des réseaux scale-free.

Paramètres :
n : nombre d'agents
filenbr: nombre ajouté au fichier
-i <iterations>: int
-s: showall: flag
-g: type de graphe""")
        
        #print("""Simule un grand nombre d'itérations sur des réseaux scale-free.
#
#Paramètres :
#        {n}
#""".format(n=sf_n_help))
        
    def do_quitter(self, arg):
        """Quitte le programme"""
        print("Au revoir\n")
        return True


def parse_nbr(arg):
    """Retourne un tuple d'entiers avec un argument sous forme de chaîne 
    de caractères."""
    return tuple(map(float, arg.split()))

sf_n_help = "Number of agents"
sf_filenumber_help = "Number of the file"
sf_iterations_help = "Number of iterations"
sf_showall_help = "Show all curves of iterations"
sf_gtype_help = "Graph type\n1-Normal\n2-Scatter plot"

#parser for sf function
parsersf = argparse.ArgumentParser()
parsersf.add_argument("n", help=sf_n_help, type = int)
parsersf.add_argument("filenumber", help=sf_filenumber_help, type = int, default = -1)
parsersf.add_argument("--iterations", "-i", help=sf_iterations_help, type=int, default = 1)
parsersf.add_argument("--showall", "-s", help=sf_showall_help, action = "store_true")
parsersf.add_argument("--gtype", "-g", help=sf_gtype_help, type=int, default=1)


def launch():
    c = Interpreteur()
    c.cmdloop()
