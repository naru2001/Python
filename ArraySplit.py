from collections import Counter,deque
from sys import stdin,setrecursionlimit

def array_split(array): #なんか
    array_len=len(array)
    res=[];ans=[]
    s=0 # 0:傾き不明 1:広義単調増加 2:広義単調減少
    roop=0
    while roop!=array_len:
        if ans==[]:
            ans.append(array[roop])
            roop+=1
        elif s==0 and ans[-1]>array[roop]:
            ans.append(array[roop])
            s=2
            roop+=1
        elif s==0 and ans[-1]<array[roop]:
            ans.append(array[roop])
            s=1
            roop+=1
        elif s==0 and ans[-1]==array[roop]:
            ans.append(array[roop])
            roop+=1
        elif s==1:
            if ans[-1]<=array[roop]:
                ans.append(array[roop])
                roop+=1
            else:
                res.append(ans)
                s=0
                ans=[]
        elif s==2:
            if ans[-1]>=array[roop]:
                ans.append(array[roop])
                roop+=1
            else:
                res.append(ans)
                s=0
                ans=[]
    res.append(ans)
    return res
