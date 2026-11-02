from random import randrange

# 集合の一致判定
# https://atcoder.jp/contests/abc250/tasks/abc250_e


"""
配列 A, B を受け取り,「先頭 i 個の要素からなる集合（重複は削除）」のハッシュ値を格納した配列 hash_A, hash_B を返す
hash_A[x] == hash_B[y] ならば, set(A[:x]) = set(B[:y])      ※ x,y: 1-indexed
"""
def zobrist_hashing(A,B):
    random_num={}
    for a in A:
        random_num[a]=randrange(1<<60)
    for b in B:
        random_num[b]=randrange(1<<60)
    
    hash_A=[0]
    set_A=set()
    for a in A:
        if a in set_A:
            hash_A.append(hash_A[-1])
        else:
            hash_A.append(hash_A[-1]^random_num[a])
            set_A.add(a)

    hash_B=[0]
    set_B=set()
    for b in B:
        if b in set_B:
            hash_B.append(hash_B[-1])
        else:
            hash_B.append(hash_B[-1]^random_num[b])
            set_B.add(b)

    return hash_A,hash_B