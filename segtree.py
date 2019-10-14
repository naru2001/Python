import sys

sys.setrecursionlimit(10**6)

INT_MAX=2**31-1
MAX_N=10**5
array=[INT_MAX]*(MAX_N*4)
n,q=map(int,input().split())

def update(i,x):
    i+=n-1
    array[i]=x
    while i>0:
        i=(i-1)//2
        array[i]=min(array[i*2-1],array[i*2+2])
    print(array[i])

def rec(a,b,k=0,left=0,right=n):
    if right<=a or b<=left:
        return INT_MAX
    if a<=left and right<=b:
        return array[k]
    else:
        value_left=rec(a,b,k*2+1,left,(left+right)//2)
        value_right=rec(a,b,k*2+2,(left+right)//2,right)
        return min(value_left,value_right)

for _ in range(q):
    c,_x,_y=map(int,input().split())
    if c==0:
        update(_x,_y)
    else:
        print(rec(_x,_y))