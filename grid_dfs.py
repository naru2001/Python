from sys import setrecursionlimit as rec
import sys
rec(10**9)

def dfs(x,y):
    if x<0 or y<0 or w<=y or h<=x or s[x][y]=='#':
        return 
    if s[x][y]=='g':
        print("Yes")
        sys.exit()

    s[x][y]='#'

    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='s':
            dfs(i,j)
            break
print("No")