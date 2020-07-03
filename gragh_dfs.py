import sys
input=sys.stdin.readline

sys.setrecursionlimit(10**6)

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
