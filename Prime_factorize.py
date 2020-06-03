def Pf(n,prime=None):#nの素因数分解(prime:素数リスト)

    if prime==None: prime=[True]*(n+1)

    ret=[]
    tmp=n

    for i in range(2,int(n**0.5)+1):
        if not prime[i]: continue
        if tmp%i==0:
            while tmp%i==0:
                ret.append(i)
                tmp//=i
    if ret==[] or tmp!=1: ret.append(tmp)

    return ret
