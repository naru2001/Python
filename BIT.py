class Binary_Indexed_Tree:

    def __init__(self,n):
        self.size=n
        self.graph=[0]*(n+1)

    def partially_sum(self,i):# [0,i]の和
        res=0
        while i>0:
            res+=self.graph[i]
            i-=i&-i
        return res

    def add_element(self,i,x):
        while self.size>=i:
            self.graph[i]+=x
            i+=i&-i
            
    def ret_sum(self,l,r):
        return self.partially_sum(r)-self.partially_sum(l+1)
