import math
import numpy as np

#N: nodes
#K: vehicles
#Q: max capacity
#q: demands
#d: distances

def split(N,K,Q,q,d,seq):
    v=[math.inf]*N
    v[0]=0
    w=[math.inf]*N
    w[0]=0
    p=[[0]*K]*N

    for k in range(K):
        for i in range(N-1):
            j=i
            load=q[seq[i]]
            dist=0
            cost=0
            while(j<N-1 and load<=Q):
                if(i==j):
                    dist=d[seq[0]][seq[j+1]]
                    cost=dist*q[seq[j+1]]
                else:
                    dist+=d[seq[j]][seq[j+1]]
                    cost+=dist*q[seq[j+1]]
                if(w[j-1]+cost<v[j]):
                    v[j]=w[i-1]+cost
                    p[j][k]=i-1
                j+=1
                load+=q[seq[j]]
                print("load:",load)
                print("dist:",dist)
                print("cost:",cost)

        for i in range(N):
            w[i]=v[i]