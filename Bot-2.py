#!/bin/python
#https://www.hackerrank.com/challenges/saveprincess2
import numpy as np
import math
def nextMove(n,r,c,grid):
# print all the moves here
    x=0
    y=0

    for i in xrange(0,n):
        try:
            y= grid[i].split("-").index('p')
        except ValueError:
            x=0
        else:
            x=i
            break

    if(y<c):
        return "LEFT"
    elif(y>c):
        return "RIGHT"
    elif(y==c and r>x):
        return "UP"
    elif(y==c and r<x):

return "DOWN"

n = input()

r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input().strip())

    x=0
    y=0

for i in xrange(0,n):
    try:
        y= grid[i].split("-").index('p')
    except ValueError:
        x=0
    else:
        x=i
        break
while(x!=r or y!=c):
    out=nextMove(n,r,c,grid)
    if(out=="UP"):
        r=r-1
    if (out=="DOWN"):
        r=r+1
    if(out=="LEFT"):
        c=c-1
    if(out=="RIGHT"):
        c=c+1

    print "Next Position is",r,c
