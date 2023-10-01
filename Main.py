from Function import *
from Split import *
from SetCovering import setCovering

path = "data/ins1.txt"
nodes,K,Q,q = readFile(path)
N=len(nodes)
d = distance(nodes)

iter=1000
c=[]
r=[]

for i in range(iter):
    seq=sequence(N)
    trips,delivs=split(N,K,Q,q,d,seq)
    
    for i in range(len(trips)):
        c.append(cost(trips[i],Q,d,delivs[i]))
        ri=[0]*(N+1)
        ri[0]=1
        for node in trips[i]:
            ri[node]=1
        r.append(ri)

T=len(c)
lim=1000
setCovering(N,K,T,c,r,lim)