import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math, os, random

#n: nodes
#k: vehicles
#Q: max capacity
#q: demands
#d: distances

# Reads a .txt with problem instances
def readFile(path):
    txt = np.loadtxt(path)
    Q = int(txt[0][0])
    K = int(txt[0][1])
    nodes = []
    q = []
    for node in txt[1:]:
        nodes.append([int(node[0]), int(node[1])])
        q.append(int(node[2]))
    return nodes, K, Q, q

# Calculates the distance matrix for all nodes
def distance(nodes):
    distances = []
    for i in range(len(nodes)):
        values = []
        for j in range(len(nodes)):
            distance = math.sqrt(math.pow(nodes[i][0] - nodes[j][0], 2) + math.pow(nodes[i][1] - nodes[j][1], 2))
            values.append(distance)
        distances.append(values)
    return distances

# Returns a random sequence
def sequence(N):
    seq = [0]
    order = np.random.permutation(N-1)
    for i in order:
        seq.append(i+1)
    return seq

# Calculates the cost of a single trip
def cost(trip,deliv,d): #Deliver -> sum(D_i*q_i)
    c = 0
    dist = 0
    for i in range(1,len(trip)):
        dist += d[trip[i-1]][trip[i]]
        c += dist * deliv[i]
    return c

# Calculates the objective function of a solution
def objective(trips):
    obj = 0
    for trip in trips:
        obj += cost(trip)
    return obj

# For each vehicle, it finds the complete route from a specific path and its cost
def calculate(N,K,Q,q,d,seq,path):
    trips,delivs,costs = [], [], []
    curr = 1
    nxt = path[curr]
    i = 1
    while i < N:
        trip = [0]
        deliv = [0]
        while i < N and seq[i] != nxt:
            trip.append(seq[i])
            deliv.append(q[seq[i]])
            i+=1
        trip.append(seq[i]), trip.append(0)
        deliv.append(q[seq[i]]), deliv.append(0)
        trips.append(trip)
        delivs.append(deliv)
        costs.append(cost(trip, deliv, d))
        i += 1
        curr += 1
        if(curr>K):
            break
        nxt = path[curr]
    return trips, delivs, costs