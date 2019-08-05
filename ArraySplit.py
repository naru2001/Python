import os,re
from collections import Counter,deque
from operator import itemgetter
from itertools import accumulate,combinations,groupby
from sys import stdin,setrecursionlimit
from copy import deepcopy
setrecursionlimit(10**6)

def array_split(array):
    array_len=len(array)
    res=[];ans=[]
    s=0 # 0:傾き不明 1:単調非減少 2:単調非増加
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
n=int(input())
a=list(map(int,input().split()))
print(array_split(a))