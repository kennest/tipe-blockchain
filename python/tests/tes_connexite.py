"""
TESTS ONLY

Module utilisé lors de tests
"""


from modelisation import *

net = Reseau()

ag_ids = [i for i in range(10)]

net._set_list_agents(ag_ids)

for i in range(4):
    net._set_tunnel(i, i+1)

net._set_tunnel(4, 0)

for i in range(5,9):
    net._set_tunnel(i, i+1)

net._set_tunnel(9,5)
