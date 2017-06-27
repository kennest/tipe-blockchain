"""
Comptage des degrés moyens dans les réseaux scale-free générés
"""

from modelisation import scale_free

# Résultats :
#             n = 50 -> ~ 1.99
#             n = 100 -> ~ 2
#             n = 100 -> ~ 2.20
#             n = 100, k = 200 -> 2.203
#             n = 1000 -> ~ ?


n = 200
k = 300

nbr = 0
for i in range(k):
    net = scale_free(n)
    for x in net.agents:
        nbr += net._get_nbr_tun(x.id)
    print(i/k*100)


print(nbr/(2*k*n))
