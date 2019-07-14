n=1000000
num=[True]*(n+1)
num[0]=num[1]=False

for i in range(2,int(n**0.5)+1):
    if num[i]:
        for j in range(i*2,n+1,i):
            num[j]=False
# 0 1 2 2 3 3 4
# 1 2 3 4 5 6 7
ans=[0]*(n)
for i in range(1,n):
    if num[i]:
        ans[i]=ans[i-1]+1
    else:
        ans[i]=ans[i-1]
while True:
    try:
        s=int(input())
    except:
        break
    print(ans[s])