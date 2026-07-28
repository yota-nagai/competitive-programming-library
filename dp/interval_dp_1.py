# https://atcoder.jp/contests/tessoku-book/submissions/73210558

N=int(input())
P,A=[],[]
for _ in range(N):
    p,a=map(int,input().split())
    p-=1
    P.append(p)
    A.append(a)

# dp[l][r]:= [l,r)のブロックが残っている状態になるまでに得られる得点のmax
# 区間長が大きい方から順にDPテーブルを更新

dp=[[0]*(N+1) for _ in range(N)]
dp[0][N]=0
for length in reversed(range(N)):
    for l in range(N):
        r=l+length
        if r>N:
            break

        # [l-1,r) --> [l,r) の遷移
        if l-1>=0:
            if l<=P[l-1]<r:
                dp[l][r]=max(dp[l][r],dp[l-1][r]+A[l-1])
            else:
                dp[l][r]=max(dp[l][r],dp[l-1][r])
        
        # [l,r+1) --> [l,r) の遷移
        if r+1<=N:
            if l<=P[r]<r:
                dp[l][r]=max(dp[l][r],dp[l][r+1]+A[r])
            else:
                dp[l][r]=max(dp[l][r],dp[l][r+1])
    

ans=0
for l in range(N):
    ans=max(ans,dp[l][l+1])

print(ans)
