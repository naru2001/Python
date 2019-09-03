#import pysnooper
#import os,re,sys,operator,math,heapq,string
from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy
setrecursionlimit(10**6)
input=stdin.readline

n=int(input().rstrip())
gragh=[[] for _ in range(n)]
q=deque()
for i in range(n):
    u=list(map(int,input().rstrip().split()))
    for j in u[2:]:
        gragh[u[0]-1].append(j-1)
#print(gragh)
dis=[-1]*n
dis[0]=0
q.append(0)
while len(q)!=0:
    v=q.popleft()
    for i in gragh[v]:
        if dis[i]!=-1:
            continue
        dis[i]=dis[v]+1
        q.append(i)
for i,j in enumerate(dis,1):
    print(i,j)
