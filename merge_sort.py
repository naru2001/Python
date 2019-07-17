inf=10**10
def merge(a,left,cen,right):
    n1=cen-left
    n2=right-cen
    L=[a[left+i] for i in range(n1)]+[inf]
    R=[a[cen+i] for i in range(n2)]+[inf]
    i,j=0,0
    for k in range(left,right):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
    return a

def sorting(a,left,right):
    if left+1<right:
        m=(left+right)//2
        sorting(a,left,m)
        sorting(a,m,right)
        merge(a,left,m,right)
    return a

n=int(input())
a=list(map(int,input().split()))
ans=sorting(a,0,n)
print(*ans)