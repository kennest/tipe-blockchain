"""
Ce module sert à réaliser les graphes avec matplotlib.pyplot
Fonctions :
 * graphe
 * graphe_full
"""

import matplotlib.pyplot as plt



def graphe(les_x, les_y, savename, title, xlabel, ylabel):
    """Trace un graphe avec en abscisse les_x, en ordonnée les_y, ayant pour titre title.
les_x: float list ou int list
les_y: float list ou int list
savename: str
title: str
xlabel: str
ylabel: str
"""
    # Bottom vertical alignment for more space
    title_font = {'size':'40', 'color':'black', 'weight':'bold'}
    
    axis_font = {'size':'30'}

    plt.clf()
    
    plt.plot(les_x, les_y)
    plt.title(title, size = 'xx-large')
    plt.xlabel(xlabel, size = 'x-large')
    plt.ylabel(ylabel, size = 'x-large')
    plt.savefig(savename + ".png")
    plt.show()

def graphe_full(les_x, les_ys, savename, title, xlabel, ylabel):
    """Trace un graphe avec en abscisse les_x, en ordonnée les différentes données de 
les_ys, ayant pour titre title.
les_x: float list ou int list
les_ys: float list ou int list
savename: str
title: str
xlabel: str
ylabel: str
"""
    plt.clf()
    for y in les_ys:
        plt.plot(les_x, y)
    plt.title(title, size = 'xx-large')
    plt.xlabel(xlabel, size = 'x-large')
    plt.ylabel(ylabel, size = 'x-large')
    plt.savefig(savename + ".png")
    plt.show()

def graphe_deg_nbr(savename, points, n, title, xlabel, ylabel):
    """
savename: str
points: tuple list
These tuples are (x, y), with x=nbr of atkers and y=total degree of attackers
So 0<=x<n and 0<=y<n**2"""

    tbl = [[0 for j in range(n**2)] for i in range(n)] 
    plt.clf()
    for p in points:
        x,y = p
        tbl[x][y] += 1
    print("Check1")
    for i in range(n): # Il faudrait améliorer l'efficacité de cette boucle
        for j in range(n**2):
            if tbl[i][j] != 0:
                plt.scatter(i, j, s=(tbl[i][j]/2))
                # La division par deux, c'est pour contrôler la taille des points
    print("Check2") #Le dessin des points prend du temps. Ce checkpoint permet de
    #                savoir lorsque c'est fini.
    plt.title(title, size = 'xx-large')
    plt.xlabel(xlabel, size = 'x-large')
    plt.ylabel(ylabel, size = 'x-large')
    plt.savefig(savename + ".png")
    plt.show()
    
