import sys
import heapq
input=sys.stdin.readline
INF=1e18
def dijkstra(G,n,start,goal=None):#グラフ,初期頂点,頂点数,ゴール
    
    dist=[INF]*n;dist[start]=0
    q=[]
    prev=[-1]*n #最短経路の前の点を記録
    heapq.heappush(q,(0,start))
    
    while len(q):
        now_dist,v=heapq.heappop(q)
        if dist[v]<now_dist: continue

        for e1,e2 in G[v]:
            if dist[v]+e1<dist[e2]:
                dist[e2]=dist[v]+e1
                heapq.heappush(q,(dist[e2],e2))
                prev[e2]=v

    if goal!=None:#復元(return path,cost)
        if dist[goal]==INF: return [],dist
        else:
            Path=[goal]
            v=goal
            while v!=start:
                v=prev[v]
                Path.append(v)
            return Path[::-1],dist
    else: return prev,dist

