from itertools import groupby

def prime_factorization(n):
    if n==1:
        return [1]
    m=n
    i=2
    res=[]
    while i*i<=n:
        if m%i==0:
            m//=i
            res.append(i)
        else:
            i+=1
    if m!=1:
        res.append(m)
    
    return res

N=int(input())
#N=1のときは別に処理

#同じ素因数をまとめる
N_factorization=[(key,len(list(group))) for key,group in groupby(prime_factorization(N))]
print(N_factorization)

"""
素数判定 O(√N)
2以上√N以下のいずれの整数iでも割り切れなければ、Nは素数
"""

"""
Nの約数列挙 O(√N) 
1. 1以上√N以下のiについて、Nがiで割り切れるかどうか調べる
2. 割り切れる場合、iとN//iを約数に追加する
"""

