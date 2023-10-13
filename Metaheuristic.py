import math
from Function import *
from Split import *
from SetCovering import setCovering

def metaheuristic(path):
    #Read file
    nodes, K, Q, q = readFile(path)
    N = len(nodes)
    d = distance(nodes)
    iter = 1000
    c, r, trips, delivs, costs = [], [], [], [], []

    #Generate trips using split algorithm
    for i in range(iter):
        seq = sequence(N)
        path = split(N, K, Q, q, d, seq)

        if(len(path) != K + 1):
            continue
        
        tripsi, delivsi, costsi=calculate(N, K, Q, q, d, seq, path)
        trips.extend(tripsi)
        delivs.extend(delivsi)
        costs.extend(costsi)

        for i in range(K):
            ri = [0] * N
            for node in tripsi[i]:
                ri[node] = 1
            r.append(ri)
            c.append(costsi[i])

    #Use set covering to choose K trips
    T = len(c)
    lim = 1000
    cov = setCovering(N, K, T, c, r, lim)

    for i in range(K):
        print(trips[cov[i]])
        print(costs[cov[i]])

    #Improve solutions

