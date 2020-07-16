import heapq

INF=1e18
def dijkstra(G,n,start):#グラフ,初期頂点,頂点数
    
    dist=[INF]*n;dist[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    
    while len(q):
        now_dist,v=heapq.heappop(q)
        if dist[v]<now_dist: continue

        for e1,e2 in G[v]:
            if dist[v]+e1<dist[e2]:
                dist[e2]=dist[v]+e1
                heapq.heappush(q,(dist[e2],e2))
        
    return dist
