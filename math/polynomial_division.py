# 多項式の除算（https://atcoder.jp/contests/abc245/tasks/abc245_d）
# ただし, 割り切れることが保証されているケース

N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))

ans_rev=[]
i=len(C)-1
for _ in range(M+1):
    a=C[i]//A[-1]
    ans_rev.append(a)
    for j in range(len(A)):
        C[i-j]-=A[-j-1]*a
    i-=1


ans=reversed(ans_rev)
print(*ans)