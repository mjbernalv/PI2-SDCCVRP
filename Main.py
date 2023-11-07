import math
from Algorithm import *
from Initial import *
import numpy as np

path = "PI2-SDCCVRP/data/clusters.txt"
nodes, K, Q, q = readFile(path)
N = len(nodes)
d = distance(nodes)

# Initial solution
# M=np.amax(d)
# far=f_nodes(N, K, d, M, 30)
# print(far)
# routes, loads, obj=initial2(K, Q, d, q, far)
# delivs=[]

# for i in range(len(loads)):
#     deliv=[0]
#     for j in range(1,len(loads[i])):
#         deliv.append(loads[i][j]-loads[i][j-1])
#     deliv.append(0)
#     delivs.append(deliv)

# print("INITIAL SOLUTION")
# print('routes:', routes)
# print('deliveries:', delivs)
# print('objective: ', objective(K, routes, delivs, d))
# print(" ")
# plot_route(nodes, routes, loads, q)

# Metaheuristic algorithm
opt_trips, opt_delivs, opt_c, obj = algorithm(path, 1000, 2, 1000)

print("METAHEURISTIC ALGORITHM SOLUTION")
print('routes:', opt_trips)
print('deliveries:', opt_delivs)
print('objective:', obj)
plot_route(nodes, opt_trips[1:3], opt_delivs[1:3], q)

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