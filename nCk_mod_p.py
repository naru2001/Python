class nCk:
    def __init__(self,n,m):
        self.fact=[False]*n
        self.finv=[False]*n
        self.inv=[False]*n
        self.fact[0],self.fact[1]=1,1
        self.finv[0],self.finv[1]=1,1
        self.inv[1]=1
        self.mod=m
        self.n=n

        for i in range(2,self.n):
            self.fact[i]=self.fact[i-1]*i%self.mod
            self.inv[i]=self.mod-self.inv[self.mod%i]*(self.mod//i)%self.mod
            self.finv[i]=self.finv[i-1]%self.mod

    def calc(self,n,k):
        if n<k : return 0
        if n<0 or k<0 :return 0
        return self.fact[n]*(self.finv[k]*self.finv[n-k]%self.mod)%self.mod
        