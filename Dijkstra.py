import heapq

INF=2<<28

def dijkstra(G,start,n):#グラフ,初期頂点,頂点数

    dist=[INF]*n;dist[start]=0
    used=[False]*n;used[0]=True
    q=[]

    for v in G[start]:
        heapq.heappush(q,v)
    
    while len(q)>0:
        now=heapq.heappop(q)
        if used[now[1]]:
            continue
        v=now[1]
        dist[v]=now[0]
        used[v]=True

        for e in G[v]:
            if not used[e[1]]:
                heapq.heappush(q,(e[0]+dist[v],e[1]))

    return dist
