from modelisation import scale_free

n = 100
k = 100

nbr = k
for i in range(100):
    net = scale_free(n)
    for x in net.agents:
        nbr += net._get_nbr_tun(x.id)
        # on compte blabla


print(nbr/(2*k))
