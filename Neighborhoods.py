import math
from Function import *

def reverse_trip(tripi, delivsi, d):
    trip = tripi.copy()
    delivs = delivsi.copy()
    trip.reverse()
    delivs.reverse()
    cst = cost(trip, delivs, d)
    return trip, delivs, cst

def join_nodes(tripi, delivsi, d):
    trip = tripi.copy()
    delivs = delivsi.copy()
    for i in range(1,len(trip)-1):
        for j in range(i, len(trip)):
            if trip[i] == trip[j]:
                delivs[i] += delivs[j]
                delivs.pop(j)
                trip.pop(j)
                break
    cst = cost(trip, delivs, d) 
    return trip, delivs, cst

def merge_nodes(trip, delivs, pos1, pos2, d):
    new_trip1 = trip.copy()
    new_delivs1 = delivs.copy()
    new_trip2 = trip.copy()
    new_delivs2 = delivs.copy()
    new_delivs1[pos1]=0
    new_delivs2[pos2]=0
    cst1 = cost(new_trip1, new_delivs1, d)
    cst2 = cost(new_trip2, new_delivs2, d)
    if cst1 < cst2:
        return new_trip1, new_delivs1, cst1
    else:
        return new_trip2, new_delivs2, cst2
    
def move_nodes(trips, delivs, cst, rep, K, d):
    opc = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    best_trips = trips.copy()
    best_delivs = delivs.copy()
    best_cost = cst.copy()
    sum_cost = sum(best_cost)

    for i in range(len(rep)):
        trip1 = rep[i][0]
        pos1 = rep[i][1]
        for j in range(i+1,len(rep)):
            trip2 = rep[j][0]
            pos2 = rep[j][1]

            for k in range(len(opc)):
                new_trips = trips.copy()
                new_delivs = delivs.copy()
                new_cost = cst.copy()
                cant = math.floor(opc[k] * new_delivs[trip1][pos1])
                new_delivs[trip1][pos1] = cant
                new_delivs[trip2][pos2] -= cant

                for m in range(len(rep)):
                    if m != i and m!=j:
                        new_delivs[rep[m][0]][rep[m][1]] = 0

                for m in range(K):
                    new_cost[m] = cost(new_trips[m], new_delivs[m], d)

                if sum(new_cost) < sum_cost:
                    best_trips = new_trips.copy()
                    best_delivs = new_delivs.copy()
                    best_cost = new_cost.copy()
                    sum_cost = sum(new_cost)

    return best_trips, best_delivs, best_cost
