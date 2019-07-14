from sys import setrecursionlimit

setrecursionlimit(10**9)

def f1(n):
    if a[n]!=0:
        return a[n]
    return n*f1(n-1)%(10**9+7)

a=[0]*1000000
a[0],a[1]=1,1
n=int(input())
for i in range(1,n+1):
    a[i]=f1(i)
print(a[n])
