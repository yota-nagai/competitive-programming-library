## 1以上N以下の整数をすべて素因数分解  
# 全体としてO(NlogN)

def factorize_fast(n):
    is_prime=[True]*(n+1)
    min_factor=[-1]*(n+1)  # 各整数の最小素因数   
    is_prime[0],is_prime[1]=False,False
    min_factor[1]=1

    # エラトステネスの篩を用いた前処理 : O(NloglogN)
    i=2
    for i in range(2,n+1):
        if is_prime[i]:
            min_factor[i]=i
            for j in range(2*i,n+1,i):
                is_prime[j]=False
                if min_factor[j]==-1:
                    min_factor[j]=i

    # 2以上N以下の整数を各々 O(logN) で素因数分解
    res=[[] for _ in range(n+1)]
    for i in range(2,n+1):
        m=i
        while m>1:
            p=min_factor[m]
            c=0
            while min_factor[m]==p:
                m//=p
                c+=1
            res[i].append((p,c))

    return res
