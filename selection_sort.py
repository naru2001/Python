n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    id=i
    mini=a[i]
    ch=False
    for j in range(i,n):
        if a[j]<mini:
            id=j
            mini=a[j]
            ch=True
    if ch:
        a[id],a[i]=a[i],a[id]
print(*a)