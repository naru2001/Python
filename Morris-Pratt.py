from sys import stdin

input=stdin.readline

def morris_pratt(string,strlen,ans_array):
    j=-1
    for i in range(strlen):
        while j>=0 and string[i]!=string[j]:
            j=ans_array[j]
        j+=1
        ans_array[i+1]=j
    return ans_array

s=input().rstrip()
n=len(s)
ans=[-1]+[0]*n
print(*morris_pratt(s,n,ans))
