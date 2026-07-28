N,K=map(int,input().split())
A=list(map(int,input().split()))

# doubling[i][j] := jから2**i回移動してたどり着く位置（位置は1-indexed） 
doubling=[[-1]*(N+1) for _ in range(61)]
for j in range(1,N+1):
    doubling[0][j]=A[j-1]
for i in range(1,61):
    for j in range(1,N+1):
        # doubling[i-1][j] = jから2**(i-1)回移動した先
        # doubling[i-1][doubling[i-1][j]] = そこからさらに2**(i-1)回移動した先　<-- jから2**i回移動した先
        doubling[i][j]=doubling[i-1][doubling[i-1][j]]

def has_bit(n,i):
    return n&(1<<i)>0

now=1
# 移動回数Kの2進法表記でどのビットが立っているかをみてシミュレーション
for i in range(61):
    if has_bit(K,i):
        now=doubling[i][now]

print(now)