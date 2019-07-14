n=int(input())
a=list(map(int,input().split()))
print(*a)
for i in range(1,n):
    num=a[i]
    j=i-1
    while j>=0 and a[j]>num:
        a[j+1]=a[j]
        j-=1
    a[j+1]=num
    print(*a)