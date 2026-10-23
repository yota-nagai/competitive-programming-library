def has_bit(n,i):
    return (n&(1<<i)>0)

#a**bをmodで割った余り
def Power(a,b,mod):
    ans=1
    p=a  #a**(2**i)
    for i in range(100):
        if 1<<i>b:
            break
        if has_bit(b,i):
            ans*=p
            ans%=mod
        p*=p
        p%=mod
    return ans

#a÷bをmodで割った余り = a*(b**(mod-2))をmodで割った余り
def Division(a,b,mod):
    return (a*Power(b,mod-2,mod))%mod

#nCrをmodで割った余り（n>=r）
def ncr(n,r,mod):
    r=min(r,n-r)
    a=1  # n(n-1)...(n-r+1) をmodで割った余り
    for i in range(n-r+1,n+1):
        a*=i
        a%=mod

    b=1  # r! をmodで割った余り
    for i in range(1,r+1):
        b*=i
        b%=mod
    
    return Division(a,b,mod)


n,r=map(int,input().split())
mod=10**9+7

print(ncr(n,r,mod))