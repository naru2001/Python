def gcd(a,b):
    if a<b:
        a,b=b,a
    r=a%b
    while r!=0:
        a,b=b,r
        r=a%b
    return b

def lcm(a,b):
    return (a*b)//gcd(a,b)
