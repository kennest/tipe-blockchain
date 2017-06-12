import graphes as g
import modelisation as md

### Scale-free avec deg
"""
filename = "../resultats/scale-free/sf-t2-n-100-1-it100.csv"

savename = "../resultats/scale-free/sf-t2-n-100-1-it100.png"

n = 100

with open(filename, 'r') as f:
    text = f.readlines()
    resultats = []
    for line in text:
#        print(line)
        line.strip("\n ")
        str_list = line.split(" ")
        tmp_list = [0 for i in range(4)]
        for j in range(len(str_list)):
            tmp_list[j] = int(str_list[j])
        resultats.append(tmp_list)


# Copier coller de tests/scale-free.py
points = []
for res in resultats:
    p, v, f, d = res #p : nombre d'attaquants, d: somme des degrés
    points.append((p, d))
title = "Scale-free, {} agents".format(str(n))
xlabel = "Nombre d'attaquants"
ylabel = "Somme des degrés des noeuds attaquants"
g.graphe_deg_nbr(savename, points, n, title, xlabel, ylabel)
"""

# Modifications des légendes et titres

FNAMELIST = ["atkaleat-10-3-2", "atkaleat-50-3-1", "atkaleat-50-20-1",\
             "atkaleat-100-2-1",\
             "sf-t1s-n100-2-it3", "sf-t1-n100-1-it100"]
"""
i = 0

if i == 0:
    filename = FNAMELIST[i]
    n = 10
    iterations = 10
    
    with open("../resultats/atkaleat/" + filename + ".csv", 'r') as f:
        text = f.readlines()
    resultats = []
    for line in text:
        line.strip("\n ")
        str_list = line.split(" ")
        tmp_list = [0 for i in range(len(str_list))]
        for j in range(len(str_list)):
            tmp_list[j] = int(str_list[j])
        resultats.append(tmp_list)

    les_x = [i/n for i in range(n)]
    les_vrais = [0 for i in range(n)]
    les_faux = [0 for i in range(n)]
    k = 0 # Compteur utilisé pour les deux boucles suivantes
    for res in resultats:
        (p, v, f) = res
        les_vrais[p] += v
        les_faux[p] += f
    for i in range(n):
        les_vrais[i] = les_vrais[i]/iterations/n
        les_faux[i] = les_faux[i]/iterations/n


    g.graphe(les_x, les_faux, filename, "Réseau homogène 10 nœuds et 3 arêtes", "Proportion d'attaquants", "Proportion d'informations fausses")

"""
    
#i = 3

if True:
    filename = "atkaleat-100-2-1"
    n = 100
    iterations = 10
    
    with open("../resultats/atkaleat/" + filename + ".csv", 'r') as f:
        text = f.readlines()
    resultats = []
    for line in text:
        line.strip("\n ")
        str_list = line.split(" ")
        tmp_list = [0 for i in range(len(str_list))]
        for j in range(len(str_list)):
            tmp_list[j] = int(str_list[j])
        resultats.append(tmp_list)

    les_x = [i/n for i in range(n)]
    les_vrais = [0 for i in range(n)]
    les_faux = [0 for i in range(n)]
    k = 0 # Compteur utilisé pour les deux boucles suivantes
    for res in resultats:
        (p, v, f) = res
        les_vrais[p] += v
        les_faux[p] += f
    for i in range(n):
        les_vrais[i] = les_vrais[i]/iterations/n
        les_faux[i] = les_faux[i]/iterations/n


    g.graphe(les_x, les_faux, filename, "Réseau homogène 100 nœuds et 2 arêtes", "Proportion d'attaquants", "Proportion d'informations fausses")
    
