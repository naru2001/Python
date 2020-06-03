def FF(n,p=10**9+7): #1~nまでの階乗 mod p
    ret=[1]+[i for i in range(1,n+1)]
    for i in range(3,n+1):
        ret[i]*=ret[i-1]
        ret[i]%=p
    return ret
