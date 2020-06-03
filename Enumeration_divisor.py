def Ed(num):
    ret=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            ret.append(i)
            if num//i!=i:
                ret.append(num//i)
    ret.sort()
    return ret
