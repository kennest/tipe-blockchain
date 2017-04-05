import random
import math
import matplotlib.pyplot as plt
import numpy as np

n = 1000


# Soit uni-, (soit bidirectionnel)
# [0, ... , n] noeuds
# pour chacun, génère nombre de liens avec bonne proba
# puis génère voisins
# P(k) = k^(-γ)

# http://stackoverflow.com/questions/10622401/implementing-barabasi-albert-method-for-creating-scale-free-networks?answertab=votes#tab-top


# random.expovariate(lambd)
#   Exponential distribution. lambd is 1.0 divided by the desired mean. It 
#   should be nonzero. (The parameter would be called “lambda”, but that is a 
#   reserved word in Python.) Returned values range from 0 to positive 
#   infinity if lambd is positive, and from negative infinity to 0 if lambd 
#   is negative.
#
# random.gammavariate(alpha, beta)

# If X ~ Exp(λ) then e^(−X) / k ∼ PowerLaw(k, λ)


k = np.linspace(0, 1000, n, endpoint=True)

#P(x; a) = ax^{a-1}, 0<x<1, a>0.

#numpy.random.power(a)

lis = []
lz = []
for i in range(n):
    x = random.expovariate(10)
    y = math.exp(-x) / 5
    z = int(np.random.power(1) * n) ## Remplacer 1 par qqchose d'autre (0,2 ?)
    lis.append(y)
    lz.append(z)

lis.sort(reverse = True)
#lz.sort(reverse = True)

lzb = [0 for i in range(n)]

for j in lz:
    lzb[j] = lzb[j] + 1
    
print("len lz : " + str(len(lz)))
print("len lzb : " + str(len(lzb)))
#plt.plot(k,lis)
plt.plot(k, lzb)
plt.show()
    
### Change strategy :
#
# x = random.randint(...)
# nbr_noeuds = int()