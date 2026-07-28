def has_bit(n,i):
    return (n&(1<<i)>0)

#a**bをmodで割ったあまり
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


a,b=map(int,input().split())

print(Power(a,b,10**9+7))


#pow(a,b,mod)がある