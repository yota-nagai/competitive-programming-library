# 正整数 n,m の公約数を列挙   O(√min(n,m))

def common_divisors(n,m):
    if n>m:
        n,m=m,n
    res=[]
    i=1
    while i*i<=n:
        if n%i==0:
            if m%i==0:
                res.append(i)
            if n//i!=i and m%(n//i)==0:
                res.append(n//i)
        i+=1
    res.sort()
    return res  