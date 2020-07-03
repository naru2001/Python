import sys
input=sys.stdin.readline

def morris_pratt(st,stlen,ans_array):
    j=-1
    for i in range(stlen):
        while j>=0 and st[i]!=st[j]:
            j=ans_array[j]
        j+=1
        ans_array[i+1]=j
    return ans_array
