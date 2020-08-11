#!/usr/bin/env python3 
from array import *

# global starting perfect square
p_sq = [[2,9,4],[7,5,3],[6,1,8]]
def formingMagicSquare(s):
    # create local copy of perfect sq to be modified, will be passed by reference
    local_sq = p_sq
    # list to contain the cost to swap to obtain a certain magic square, will return
    # minimum value in this list
    costs = []
    # calculate cost to create this perfect square and append to costs
    costs.append(calcCost(local_sq, s))
    
    # generate first perfect square and then calc cost
    print(local_sq[0][0],local_sq[0][2])
    # swap 
    local_sq[0][0], local_sq[0][2] = local_sq[0][2], local_sq[0][0]
    local_sq[2][0], local_sq[1][2] = local_sq[1][2], local_sq[2][0]
    print(local_sq[0][0],local_sq[0][2])
    costs.append(calcCost(local_sq, s))
    
    return min(costs)

def calcCost(sq,s):
    # keeps track of cost to swap to make perfect square
    finalCost = 0
    for i in range(3):
        for j in range(3):
            finalCost = finalCost + abs(sq[i][j] - s[i][j])
    return finalCost

def swap(a, b):
    store = a
    a = b
    b = store
    return a, b

if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s) 
    print(result)
