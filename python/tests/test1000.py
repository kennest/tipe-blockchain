import modelisation as mod
import random

## Init

net = mod.Reseau()

for i in range(1000):
    net._set_agent(i)

for i in range(1000):
    voisins = [random.randrange(0,1000) for j in range(10)]
    voisins = list(set(voisins))
    for vois in voisins:
        net._set_tunnel(i, vois)

