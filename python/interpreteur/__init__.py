"""
Module interpreteur

Définit principalement la classe Interpreteur, qui gère le menu du programme
"""

import cmd
import argparse
from modelisation.fonctionnement import *
from tests.atkaleat import test_atkaleat
from tests.scale_free import test_atk_scale_free


class Interpreteur(cmd.Cmd):
    intro = "\nReseaux\n======="
    prompt = "} "
    
    def do_diffetoile(self, arg): #
        (n, p, centre, emetteur, destinataire) = parse_nbr(arg)
        diff_etoile(n, p, centre, emetteur, destinataire)

    # Aide de diffetoile :
    def help_diffetoile(self):
        print("""Lance la diffusion en étoile
        Paramètres :
        n : int, Nombre d'agents
        p : int, nombre d'attaquants (p<=n)
        centre : int, 1 si le centre est attaquant, 0 sinon
        emetteur : int, emetteur de l'information
        destinataire : int, destinataire de l'information""")
        
    def do_diffaleat(self, arg):
        # def parse(arg):
        #     """Traite les arguments de la fonction"""
        #     parser = argparse.ArgumentParser()
        #     parser.add_argument("echo")
        #     parser.parse_args()
        
        (n, nb_tun, p, emetteur, destinataire) = parse_nbr(arg)
        diff_aleatoire(n, nb_tun, p, emetteur, destinataire)

    def help_diffaleat(self):
        print("""Lance la diffusion sur un réseau aléatoire
        
        Paramètres :
        n : nombre d'agents
        nb_tun : nombre de tunnels
        p : nombre d'attaquants (p<=n)
        emetteur : émetteur de l'information
        destinataire : destinataire de l'information""")

        
    def do_testatkaleat(self, arg):
        (n, nb_tun, nbr_fichier) = parse_nbr(arg)
        r = test_atkaleat(int(n), int(nb_tun), int(nbr_fichier))

    def help_testatkaleat(self):
        print("""Créé une fonction permettant de simuler des diffusions aléatoires à n et nb_tun fixés, en faisant varier p. Ensuite, trace une courbe représentant le nombre de 'vrais' par rapport aux 'faux'.
        
        Paramètres :
        n : nombre d'agents
        nb_tunnels : nombre de tunnels
        nbr_fichier : nombre ajouté au nom de fichier
        """)

    def do_testsf(self, arg):
        
        args = parsersf.parse_args(arg.split(" "))
        n, nbr_fichier, showall, iterations, gtype = args.n, args.filenumber, args.showall, args.iterations, args.gtype
        
        r = test_atk_scale_free(n, nbr_fichier, showall, iterations, gtype)

    def help_testsf(self):
        print("""Simule des itérations sur des réseaux scale-free.

Paramètres :
n : nombre d'agents
filenbr: nombre ajouté au fichier
-i <iterations>: int
-s: showall: flag
-g: type de graphe""")
        
    def do_quitter(self, arg):
        """Quitte le programme"""
        print("Au revoir\n")
        return True


### On définit ensuite un parser, pour traiter les arguments reçus en entrée de l'interpréteur

def parse_nbr(arg):
    """Retourne un tuple d'entiers avec un argument sous forme de chaîne 
    de caractères."""
    return tuple(map(float, arg.split()))

# De l'aide, inutilisée

sf_n_help = "Number of agents"
sf_filenumber_help = "Number of the file"
sf_iterations_help = "Number of iterations"
sf_showall_help = "Show all curves of iterations"
sf_gtype_help = "Graph type\n1-Normal\n2-Scatter plot"

# Le parser pour testsf
parsersf = argparse.ArgumentParser()
parsersf.add_argument("n", help=sf_n_help, type = int)
parsersf.add_argument("filenumber", help=sf_filenumber_help, type = int, default = -1)
parsersf.add_argument("--iterations", "-i", help=sf_iterations_help, type=int, default = 1)
parsersf.add_argument("--showall", "-s", help=sf_showall_help, action = "store_true")
parsersf.add_argument("--gtype", "-g", help=sf_gtype_help, type=int, default=1)



def launch():
    """Lance l'interpréteur""" 
    c = Interpreteur()
    c.cmdloop()
