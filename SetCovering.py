from gurobipy import *
import numpy as np
import time
import math

# N: set of nodes 
# K: set of vehicles
# T: set of trips
# C_t: cost of trip t
# r_it: 1 if node i is visited by trip t, 0 otherwise
# x_t: 1 if trip t is selected, 0 otherwise

def setCovering(nN,K,nT,c,r,lim):
    model = Model('SetCovering')

    #Variables
    x=model.addVars(nT, vtype=GRB.BINARY, name='x')

    #Sets
    T=range(nT)
    N=range(nN)

    #Constraints
    model.addConstrs(quicksum(r[t][i]*x[t] for t in T) >= 1 for i in N)
    model.addConstr(quicksum(x[t] for t in T) == K)

    #Objective
    obj=quicksum(c[t]*x[t] for t in T)
    model.setObjective(obj, GRB.MINIMIZE)
    model.update()

    #Optimize
    model.setParam(GRB.Param.OutputFlag,0)
    model.setParam(GRB.Param.TimeLimit,lim)
    tiempo=time.time()
    model.optimize()
    tiempo=time.time()-tiempo

    #Results
    # print('-------------------------------------------')
    # print('My model')
    # print('Objective = \t', int(model.objVal))
    # print('Gap = \t\t', model.MIPGap*100)
    # print('time = \t\t',tiempo)
    # print('-------------------------------------------')

    ans=[]
    for i in T:
        if(x[i].x==1):
            ans.append(i)

    return ans