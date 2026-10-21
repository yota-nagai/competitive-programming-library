# 正整数 n,m の公約数を列挙   O(log(min(n,m)) + √GCD(n,m))

from math import gcd

def common_divisors(n,m):
    g=gcd(n,m)
    res=[]
    i=1
    while i*i<=g:
        if g%i==0:
            res.append(i)
            if g//i!=i:
                res.append(g//i)
        i+=1
    res.sort()
    return res