import math
from Function import *
from Split import *
from SetCovering import *
from Metaheuristic import * 

path = "PI2-SDCCVRP/data/ins1.txt"
metaheuristic(path)

# #EXAMPLE
# N=6
# K=3
# Q=10
# q=[0,5,4,4,2,7]
# d=[[0,20,25,30,40,35],[20,0,10,math.inf,math.inf,math.inf],[25,10,0,30,math.inf,math.inf],[30,math.inf,30,0,25,math.inf],[40,math.inf,math.inf,25,0,15],[35,math.inf,math.inf,math.inf,15,0]]
# seq=[0,1,2,3,4,5]
# path=split(N,K,Q,q,d,seq)
# print(path)
# trips, delivs, costs=calculate(N,K,Q,q,d,seq,path)
# print(trips)
# print(delivs)
# print(costs)

# seq=sequence(N)
# print(Q)
# print(seq)
# print(q)
# path=split(N,K,Q,q,d,seq)
# print(path)