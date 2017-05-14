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
    plt.clf()
    plt.plot(les_x, les_y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()

def graphe_full(les_x, les_ys, savename, title, xlabel, ylabel):
    """Trace un graphe avec en abscisse les_x, en ordonnée les différentes données de les_ys, ayant pour titre title.
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
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()

def graphe_deg_nbr(savename, points, n, title, xlabel, ylabel):
    """
savename: str
points: tuple list
These tuples are (x, y), with x=total degree of attackers and y=nbr of atkers
So 0<=x<n**2 and 0<=y<n"""

    tbl = [[0 for j in range(n)] for i in range(n**2)]
    plt.clf()
    for p in points:
        x,y = p
        tbl[x][y] += 1
    print("Check1")
    for i in range(n**2):
        for j in range(n):
            plt.scatter(i, j, s=(tbl[i][j]/10))
    print("Check2")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()
    
