def Bf(G,N,start):
    INF=2<<32
    cost=[INF]*N
    cost[start]=0
    for i in range(N):
        ch=True
        for f,t,c in G:
            if cost[t]>cost[f]+c:
                cost[t]=cost[f]+c
                ch=False
        if ch: break
        if i==N-1:return -1 #負閉路有り
    return cost