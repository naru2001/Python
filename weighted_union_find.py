import sys
sys.setrecursionlimit(10**6)

class Weighted_Union_find:
    
    def __init__(self,n):
        self.n=n
        self.root=[i for i in range(n+1)]
        self.rank=[0]*(n+1)
        self.weight=[0]*(n+1)

    def find_root(self,x):# 頂点xのroot(根)頂点を見つける
        if self.root[x]==x:
            return x
        else:
            y=self.find_root(self.root[x])
            self.weight[x]+=self.weight[self.root[x]]
            self.root[x]=y
            return y

    def unite(self,x,y,w):#頂点xと頂点yを繋ぐ辺を追加
        rx=self.find_root(x)
        ry=self.find_root(y)
        if rx==ry:
            return 0
        if self.rank[rx]<self.rank[ry]:
            self.root[rx]=ry
            self.weight[rx]=w-self.weight[x]+self.weight[y]
        else:
            self.root[ry]=rx
            self.weight[ry]=-w-self.weight[y]+self.weight[x]
            if self.rank[rx]==self.rank[ry]:
                self.rank[rx]+=1

    def same(self,x,y):#頂点xと頂点yが連結であるか判定
        return self.find_root(x)==self.find_root(y)

    def count(self,x):#頂点xが属する木のサイズ
        return -self.root[self.find_root(x)]
    
    def diff(self,x,y):#頂点xから頂点yへのコスト
        return self.weight[x]-self.weight[y]

