from gurobipy import *
import numpy as np
import time
import math

# k: set of vehicles
# T: set of trips
# C_t: cost of trip t
# r_it: 1 if node i is visited by trip t, 0 otherwise
# x_t: 1 if trip t is selected, 0 otherwise

def setCovering(n,k,t,c,r,lim):
    model = Model('SetCovering')

    #Variables
    x=model.addVars(T, vtype=GRB.binary, name='x')

    #Sets
    K=range(k)
    T=range(t)
    N=range(n)

    #Constraints
    model.addConstrs(quicksum(r[i][t]*x[t] for k in K) >= 1 for i in N)
    model.addConstr(quicksum(x[t] for t in T) == k)

    #Objective
    obj=quicksum(c[t]*x[t] for t in T)
    model.setObjective(obj, GRB.MINIMIZE)
    model.update()

    #Optimize
    model.setParam(GRB.Param.OutputFlag,1)
    model.setParam(GRB.Param.TimeLimit,lim)
    tiempo=time.time()
    model.optimize()
    tiempo=time.time()-tiempo

    #Results
    print('-------------------------------------------')
    print('My model')
    print('Objective = \t', int(model.objVal))
    print('Gap = \t\t', model.MIPGap*100)
    print('time = \t\t',tiempo)
    print('-------------------------------------------')
