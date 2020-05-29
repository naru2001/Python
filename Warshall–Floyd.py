def warshall_floyd(G,n):
    r=range(n)
    for i in r:
        for j in r:
            for k in r:
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])
    