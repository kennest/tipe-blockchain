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

def graphe_deg_nbr(savename, points, title, xlabel, ylabel):
    """
savename: str
points: tuple list """
    
    plt.clf()
    for p in points:
        x,y = p
        plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savename + ".png")
    plt.show()
    
