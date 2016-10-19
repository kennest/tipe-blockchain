import modelisation as mod


## Initialisation du réseau
net = mod.Reseau()

for i in range(10):
    net._set_agent(i)

liens = [(1,5),(1,2), (2,1),(2,0), (3,4),(3,5),(3,8),(3,9), (4,0), \
         (5,2),(5,6), (6,3), (7,3),(7,9), (8,3), (9,0),(9,7)]
for lien in liens:
    net._set_tunnel(lien[0], lien[1])

## Boucle principale
information0 = mod.Informations()
agent0 = net._get_agent(0)
agent0._add_info(information0)

for i in range(10):
    for agent in net.agents:
        
