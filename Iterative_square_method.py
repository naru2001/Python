x,n,p=map(int,input().split())
ans=1
while n>0:
    if n&1:
        ans*=x
        ans%=p
    x*=x
    x%=p
    n>>=1
print(ans)