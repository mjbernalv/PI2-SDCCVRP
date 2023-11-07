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
    nodes, q = [], []
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

# Splits Nmut nodes in 2 separate nodes
def mutate(N, seq, q, Nmut):
    k = random.sample(range(1,N), Nmut)
    new_seq = seq.copy()
    # new_q = q.copy()
    mp = {}
    pos = N
    for i in k:
        # aux = q[i]
        # r = random.randint(1, aux-1)
        # new_q[i] = r
        # new_q.append(aux-r)
        new_seq.append(pos)
        mp[pos] = i
        pos += 1
    new_seq = new_seq[0:1] + random.sample(new_seq[1:], len(new_seq)-1)
    return new_seq, mp, #new_q

# Calculates the cost of a single trip
    #Deliver -> ob=sum(D_i*q_i)
def cost(trip, deliv, d): 
    c = 0
    dist = 0
    for i in range(1,len(trip)):
        dist += d[trip[i-1]][trip[i]]
        c += dist * deliv[i]
    return c

# Calculates the objective function of a solution
def objective(K, trips, delivs, d):
    obj = 0
    for i in range(K):
        obj += cost(trips[i], delivs[i], d)
    return obj

# For each vehicle, it finds the complete route from a specific path and its cost
def calculate(N, K, q, d, seq, path, mp, Nmut):
    trips,delivs,costs = [], [], []
    curr = 1
    nxt = path[curr]
    i = 1
    while i < N + Nmut:
        trip = [0]
        deliv = [0]
        while i < N + Nmut and seq[i] != nxt:
            if seq[i] >= N:
                trip.append(mp[seq[i]])
                deliv.append(q[mp[seq[i]]])
            else:
                trip.append(seq[i])
                deliv.append(q[seq[i]])
            i+=1
        if seq[i] >= N:
            trip.append(mp[seq[i]])
            deliv.append(q[mp[seq[i]]])
        else:
            trip.append(seq[i])
            deliv.append(q[seq[i]])
        trip.append(0)
        deliv.append(0)
        trips.append(trip)
        delivs.append(deliv)
        costs.append(cost(trip, deliv, d))
        i += 1
        curr += 1
        if(curr>K):
            break
        nxt = path[curr]
    return trips, delivs, costs


# # Calculates the objective function of a solution
# def objective1(costs):
#     obj = 0
#     for cost in costs:
#         obj += cost
#     return obj

# # Calculates the cost of a single trip
#     #Deliver -> ob=sum(D_i*q_i)
# def cost(trip,deliv,d): 
#     c = 0
#     dist = 0
#     for i in range(1,len(trip)):
#         dist += d[trip[i-1]][trip[i]]
#         c += dist * deliv[i]
#     return c

def plot_route(nodes, routes, delivs, demands):
    colors=[f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(routes))]
    # colors=['lightseagreen', 'mediumpurple', 'palegreen', 'hotpink']

    x=[node[0] for node in nodes[1:]]
    y=[node[1] for node in nodes[1:]]

    fig, ax = plt.subplots()

    for i in range(len(routes)):
        for j in range(1,len(routes[i])):
            x_route=[nodes[routes[i][j-1]][0], nodes[routes[i][j]][0]]
            y_route=[nodes[routes[i][j-1]][1], nodes[routes[i][j]][1]]
            lab='['+str(routes[i][j]) + ', '+ str(demands[routes[i][j]]) + ', ' + str(delivs[i][j-1]) + ']'
            ax.plot(x_route, y_route, color=colors[i], linewidth=2, zorder=1)
            ax.text(x_route[1], y_route[1], lab)
   
    # for i, route in enumerate(routes):
    #     # for j in route:
    #     #     x1=nodes[j[0]][0]
    #     #     y1=nodes[j[0]][1]
    #     #     x2=nodes[j[1]][0]
    #     #     y2=nodes[j[1]][1]
    #     #     ax.plot([x1, x2], [y1, y2], color=colors[i], linewidth=2)
    #     x_route=[nodes[j][0] for j in route]
    #     y_route=[nodes[j][1] for j in route]
    #     ax.plot(x_route, y_route, color=colors[i], linewidth=2, zorder=1)

    ax.scatter(nodes[0][0], nodes[0][1], color='orangered', zorder=3)
    ax.scatter(x, y, color='gray', zorder=3)

    # ax.text(nodes[0][0], nodes[0][1], 0)
    # for i in range(len(x)):
    #     ax.text(x[i], y[i], i+1) 

    ax.set_title('SDCCVRP Routes', fontsize = 18, fontweight ='bold')
    ax.set_xlabel('x', fontsize = 12, fontweight ='bold')
    ax.set_ylabel('y', fontsize = 12, fontweight ='bold')
    plt.show()
