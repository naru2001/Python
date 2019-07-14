def prime(num):
    snum=int(num**0.5)+1
    pn=[True]*(snum+1)
    pn[0]=False
    pn[1]=False
    for i in range(2,snum):
        if pn[i]:
            for j in range(i*2,snum+1,i):
                pn[j]=False
    return pn

def factorization(n,l):
    ans=[]
    tmp=n
    for i in range(2,int(len(l)**0.5)+1):
        if l[i]==False:
            continue
        if tmp%l[i]==0:
            while tmp%i==0:
                ans.append(i)
                tmp//=i
    if ans==[]:
        ans.append(n)
    elif tmp!=1:
        ans.append(tmp)
    return ans


n=int(input())
p=prime(n)
s=factorization(n,p)
print(str(n)+":",end=' ')
print(*s)