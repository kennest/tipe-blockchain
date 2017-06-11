import graphes as g
import modelisation as md

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
