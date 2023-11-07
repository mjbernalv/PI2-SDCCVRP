import math
import random
import time
import numpy as np
from queue import Queue
from Function import *
from Split import *
from Neighborhoods import *
from SetCovering import setCovering

def algorithm(file_path, iter, Nmut, lim):
    print("Data")
    nodes, K, Q, q = readFile(file_path)
    N = len(nodes)
    d = distance(nodes)
    c, r, trips, delivs = [], [], [], []

    print("Sequences")
    start = time.time()
    while len(c) < K*iter and time.time() - start < lim:
        s = list(range(N))
        seq, mp = mutate(N, s, q, Nmut) 
        path = split(N, K, Q, q, d, seq, mp, Nmut)

        if len(path) == K + 1:
            tripsi, delivsi, costsi = calculate(N, K, q, d, seq, path, mp, Nmut)
            trips.extend(tripsi)
            delivs.extend(delivsi)

            for i in range(K):
                ri = [0] * N
                for node in tripsi[i]:
                    ri[node] = 1
                r.append(ri)
                c.append(costsi[i])

            for i in range(len(tripsi)):
                new_trip, new_deliv, new_cost = join_nodes(tripsi[i], delivsi[i], d)
                trips.append(new_trip)
                delivs.append(new_deliv)
                ri = [0] * N
                for node in new_trip:
                    ri[node] = 1
                r.append(ri)
                c.append(new_cost)
                tripsi[i] = new_trip.copy()
                delivsi[i] = new_deliv.copy()

            for i in range(len(tripsi)):
                new_trip, new_deliv, new_cost = reverse_trip(tripsi[i], delivsi[i], d)
                trips.append(new_trip)
                delivs.append(new_deliv)
                ri = [0] * N
                for node in new_trip:
                    ri[node] = 1
                r.append(ri)
                c.append(new_cost)

    print("Set Covering")
    T = len(c)
    cov = setCovering(N, K, T, c, r, lim)
    print(cov)

    opt_trips = [None] * K
    opt_delivs = [None] * K
    opt_c = [None] * K
    rep = [None] * N

    for i in range(K):
        opt_trips[i] = trips[cov[i]]
        opt_delivs[i] = delivs[cov[i]]
        opt_c[i] = c[cov[i]]

        for j in range(1,len(opt_trips[i])-1):
            node = opt_trips[i][j]
            if rep[node] == None:
                rep[node] = [(i,j)]
            else:
                rep[node].append((i,j))

    print(opt_trips)
    print(rep)

    print("Neighborhoods 1")
    for i in range(1,N):
        if len(rep[i]) == 1:
            continue
        for j in range(len(rep[i])-1):
            if rep[i][j][0] == rep[i][j+1][0]:
                new_trip, new_deliv, new_cost = merge_nodes(opt_trips[rep[i][j][0]], opt_delivs[rep[i][j][0]], rep[i][j][1], rep[i][j+1][1], d)
                opt_trips[rep[i][j][0]] = new_trip
                opt_delivs[rep[i][j][0]] = new_deliv
                opt_c[rep[i][j][0]] = new_cost
                rep[i].pop(j+1)

    print("Neighborhoods 2")
    for i in range(1,N):
        if len(rep[i]) == 1:    
            continue
        new_trip, new_deliv, new_cost = move_nodes(opt_trips, opt_delivs, opt_c, rep[i], K, d)
        opt_trips = new_trip
        opt_delivs = new_deliv
        opt_c = new_cost

    print("Final")
    for i in range(K):
        for j in range(len(opt_delivs[i])-2, 0, -1):
            if opt_delivs[i][j] == 0:
                opt_trips[i].pop(j)
                opt_delivs[i].pop(j)
        opt_c[i] = cost(opt_trips[i], opt_delivs[i], d)

    return opt_trips, opt_delivs, opt_c, sum(opt_c)

    # N=6
    # K=3
    # Q=10
    # Nmut=3
    # q=[0,5,4,4,2,7]
    # d=[[0,20,25,30,40,35],[20,0,10,12,13,15],[25,10,0,30,22,21],[30,12,30,0,25,18],[40,13,22,25,0,15],[35,15,21,18,15,0]]