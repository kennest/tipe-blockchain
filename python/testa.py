import modelisation as mod


net = mod.Reseau()

for i in range(10):
    net._set_agent(i)

liens = [(1,5),(1,2), (2,1),(2,0), (3,4),(3,5),(3,8),(3,9), (4,0), \
         (5,2),(5,6), (6,3), (7,3),(7,9), (8,3), (9,0),(9,7)]
for lien in liens:
    net._set_tunnel(lien[0], lien[1])

