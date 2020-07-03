def Ism(x,n,p=2<<32): #x^n mod p
    ret=1
    while n>0:
        if n&1:
            ret*=x
            ret%=p
        x*=x
        x%=p
        n>>=1
    return ret
