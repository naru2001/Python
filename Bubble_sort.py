def Bs(n,a):

    cnt=0
    for i in range(n-1):
        id=i
        mini=a[i]
        ch=False
        for j in range(i,n):
            if mini>a[j]:
                mini=a[j]
                id=j
                ch=True
        if ch:
            a[i],a[id]=a[id],a[i]
            cnt+=1
    return a
