from random import randrange

# 多重集合の一致判定
# https://atcoder.jp/contests/abc367/tasks/abc367_f


"""
配列 A, B を受け取り,「先頭 i 個の要素からなる多重集合（重複を考慮）」のハッシュ値を格納した配列 hash_A, hash_B を返す
hash_A[r+1] - hash_A[l] == hash_B[R+1] - hash_B[L] ならば,
{A[l],A[l+1],...,A[r]} と {B[L],B[L+1],...,B[R]} は並び替えにより一致（多重集合として一致）させることができる    ※ l,r,L,R : 0-indexed
"""
def multiset_hashing(A,B):
    random_num={}
    for a in A:
        random_num[a]=randrange(1<<60)
    for b in B:
        random_num[b]=randrange(1<<60)
    
    hash_A=[0]
    for a in A:
        hash_A.append(hash_A[-1]+random_num[a])
    
    hash_B=[0]
    for b in B:
        hash_B.append(hash_B[-1]+random_num[b])

    return hash_A,hash_B