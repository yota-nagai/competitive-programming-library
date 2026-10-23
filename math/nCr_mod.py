# nCr（n>=r）をmodで割った余りを計算
def nCr_mod(n,r,mod):
    r=min(r,n-r)
    a=1  
    for i in range(n-r+1,n+1):
        a*=i
        a%=mod
    b=1  
    for i in range(1,r+1):
        b*=i
        b%=mod
    
    # a÷bをmodで割った余り = a*(b**(mod-2))をmodで割った余り
    return (a*pow(b,mod-2,mod))%mod