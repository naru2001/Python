def Es(num): #2~numまでの素数列挙
    isPrime=[True]*(num+1)
    isPrime[0]=isPrime[1]=False
    for i in range(2,int(num**0.5)+1):
        if isPrime[i]:
            for j in range(i*2,num+1,i):
                isPrime[j]=False
    return isPrime
