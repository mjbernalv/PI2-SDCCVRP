from queue import Queue
from Function import *
import math

#N: nodes
#K: vehicles
#Q: max capacity
#q: demands
#d: distances

# Constructs the auxiliary graph for the split algorithm
    # Arc (i,j) means that there is a path from node i+1 to node j (including the depot)
def aux(N, Q, q, d, seq, mp, Nmut):
    g = [None] * (N + Nmut)
    for i in range(N + Nmut):
        gi = []
        load = Q
        dist = 0
        cost = 0
        j = i
        while (j < (N + Nmut - 1)) and (load > 0):
            if seq[j+1] >= N:
                k = mp[seq[j+1]]
            else:
                k = seq[j+1]
            if seq[j] >= N:
                m = mp[seq[j]]
            else:
                m = seq[j]
            if i == j:  
                dist += d[0][k]
            else:
                dist += d[m][k]
            cost += dist * q[k]
            load -= q[k]
            if load >= 0:
                gi.append((seq[j + 1],cost))
            else:
                break
            j += 1
        g[seq[i]]=gi
    return g

# Reconstructs the path using exactly K arcs of the auxiliary graph (K vehicles)
def find_path(K, end, p):
    path = []
    while end!=-1:
        path.append(end)
        end = p[end][K]
        K -= 1
    path.reverse()
    return path

# Splits the sequence into K routes using the auxiliary graph and DP
def split(N, K, Q, q, d, seq, mp, Nmut):
    g=aux(N, Q, q, d, seq, mp, Nmut)
    in_degree = [0] * (N + Nmut)
    p = [[-1 for _ in range(N + Nmut)] for _ in range(N + Nmut)]

    for i in range(N + Nmut):
        for v in g[i]:
            in_degree[v[0]] += 1
    q = Queue()
    q.put(0)
    in_degree[0] = -1
    dist = [[math.inf for _ in range(N + Nmut)] for _ in range(N + Nmut)]
    dist[0][0] = 0

    while not q.empty():
        u = q.get()
        for v in g[u]:
            in_degree[v[0]] -= 1
            if in_degree[v[0]] == 0:
                in_degree[v[0]] = -1
                q.put(v[0])
            for i in range(1, N + Nmut):
                if dist[v[0]][i] > dist[u][i - 1] + v[1]:
                    dist[v[0]][i] = dist[u][i - 1] + v[1]
                    p[v[0]][i] = u
    
    path = find_path(K, seq[N + Nmut - 1], p)
    return path


# def split(N,K,Q,q,d,seq):
#     v=[math.inf]*N
#     v[0]=0
#     w=[math.inf]*N
#     w[0]=0
#     p=[[0]*K]*N

#     for k in range(K):
#         for i in range(N-1):
#             j=i
#             load=q[seq[i]]
#             dist=0
#             cost=0
#             while(j<N-1 and load<=Q):
#                 if(i==j):
#                     dist=d[seq[0]][seq[j+1]]
#                     cost=dist*q[seq[j+1]]
#                 else:
#                     dist+=d[seq[j]][seq[j+1]]
#                     cost+=dist*q[seq[j+1]]
#                 if(w[j-1]+cost<v[j]):
#                     v[j]=w[i-1]+cost
#                     p[j][k]=i-1
#                 j+=1
#                 load+=q[seq[j]]
#                 # print("load:",load)
#                 # print("dist:",dist)
#                 # print("cost:",cost)

#         for i in range(N):
#             w[i]=v[i]
