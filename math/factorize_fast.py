# エラトステネスの篩による前計算  O(n log log n)
def build_min_factor(n):
    is_prime=[True]*(n+1)
    is_prime[0],is_prime[1]=False,False
    min_factor=[-1]*(n+1)  # 各整数の最小素因数   

    for i in range(2,n+1):
        if is_prime[i]:
            min_factor[i]=i
            for j in range(2*i,n+1,i):
                is_prime[j]=False
                if min_factor[j]==-1:
                    min_factor[j]=i
    return min_factor


# 2以上n以下の整数mを O(log m) で素因数分解
def factorize_fast(m,min_factor):
    res=[]  # [(素因数,指数),...]
    k=m
    while k>1:
        p=min_factor[k]
        c=0
        while min_factor[k]==p:
            k//=p
            c+=1
        res.append((p,c))
    return res



N=int(input())
min_factor=build_min_factor(N)

# 2以上N以下の整数を各々素因数分解：全体でO(N log N)
for i in range(2,N+1):
    factorize_fast(i,min_factor)