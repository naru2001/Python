def compression(A):
    B=sorted(set(A))
    res={key:value for value,key in enumerate(B)}
    return [res[i] for i in A]