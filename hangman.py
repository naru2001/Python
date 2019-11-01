from random import randrange
import string

l=int(input("len: "))
now=list("_"*l)
body=["〇+<","〇+、","〇+","〇|","〇"]

def make_word(n):
    abc=list(string.ascii_lowercase)
    return "".join((abc[randrange(0,26)] for _ in range(n)))

ans=make_word(l)

def check(t):
    flag=False
    for i in range(l):
        if t==ans[i]:
            now[i]=t
            flag=True
    return flag

cnt=0
while(len(body)):
    s=input("alphabet: ")
    if not check(s):
        print(body[-1])
        del body[-1]
    else:
        print(" ".join(now))
        cnt+=1
    if cnt==l:
        print("Accepted!")
        exit()
else:
    print("Fuck")