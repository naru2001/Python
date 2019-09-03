#import pysnooper
#import os,re,sys,operator,math,heapq,string
from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy

setrecursionlimit(10**6)
input=stdin.readline

h,w=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
sy,sx,gy,gx=sy-1,sx-1,gy-1,gx-1
c=[list(input().rstrip()) for _ in range(h)]
#print(c)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dis=[[-1]*w for _ in range(h)]
dis[sy][sx]=0
q=deque([(sy,sx)])
rootx=[[-1]*w for _ in range(h)]
rooty=[[-1]*w for _ in range(h)]

while len(q)!=0:
    y,x=q.popleft()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ny<=0 or nx<=0 or ny+1==h or nx+1==w:
            continue
        if c[ny][nx]=="#":
            continue
        if dis[ny][nx]==-1:
            q.append((ny,nx))
            dis[ny][nx]=dis[y][x]+1
            rootx[ny][nx]=x
            rooty[ny][nx]=y

x,y=gx,gy
while x!=-1 and y!=-1:
    c[y][x]="o"
    x,y=rootx[y][x],rooty[y][x]
for i in c:
    print(*i)