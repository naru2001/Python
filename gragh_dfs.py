import os,re,sys,operator
from collections import Counter,deque
from operator import itemgetter
from itertools import accumulate,combinations,groupby
from sys import stdin,setrecursionlimit
from copy import deepcopy
import heapq

setrecursionlimit(10**6)

def dfs(now,depth):
    global used
    global gragh
    global n
    ans=0

    if used[now]:
        return 0
    if depth==n:
        return 1
    used[now]=1
    for i in range(n):
        if gragh[now][i]:
            ans+=dfs(i,depth+1)
    used[now]=0
    return ans

n,m=map(int,stdin.readline().rstrip().split())
gragh=[[0]*n for _ in range(n)]

for i in range(m):
    a,b=map(int,stdin.readline().rstrip().split())
    gragh[a-1][b-1]=gragh[b-1][a-1]=1

used=[0]*n
print(dfs(0,1))