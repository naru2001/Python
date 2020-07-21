def Pf(n):#nの素因数分解
    ret=[]
    tmp=n

    for i in range(2,int(n**0.5)+1):
        if tmp%i==0:
            while tmp%i==0:
                ret.append(i)
                tmp//=i
    if ret==[] or tmp!=1: ret.append(tmp)

    return ret
