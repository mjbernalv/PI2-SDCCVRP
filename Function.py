import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math, os, random

#n: nodes
#k: vehicles
#Q: max capacity
#q: demands
#d: distances

def readFile(path):
    txt = np.loadtxt(path)
    Q=int(txt[0][0])
    K=int(txt[0][1])
    nodes=[]
    q=[]
    for node in txt[1:]:
        nodes.append([int(node[0]), int(node[1])])
        q.append(int(node[2]))
    return nodes, K, Q, q

def distance(nodes):
    distances=[]
    for i in range(len(nodes)):
        values=[]
        for j in range(len(nodes)):
            distance=math.sqrt(math.pow(nodes[i][0]-nodes[j][0],2)+math.pow(nodes[i][1]-nodes[j][1],2))
            values.append(distance)
        distances.append(values)
    return distances

def sequence(N):
    seq=[0]
    order=np.random.permutation(N-1)
    for i in order:
        seq.append(i+1)
    return seq

def cost(trip,Q,d,deliv): #Deliver
    c=0
    load=Q
    for i in range(1,len(trip)):
        c+=d[i-1][i]*load
        load-=deliv[i]
    return c

def objective(trips):
    obj=0
    for trip in trips:
        obj+=cost(trip)
    return obj
