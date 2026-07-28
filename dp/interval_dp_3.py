# https://atcoder.jp/contests/dp/submissions/73221612

N=int(input())
A=list(map(int,input().split()))

cum_A=[0]  # 区間のスライムの大きさをO(1)で求める用
for a in A:
    cum_A.append(cum_A[-1]+a)


# dp[l][r]:= [l,r)を, 全てバラバラにするのに必要なコストのmin
# 区間長が小さい方からDPを回していく

dp=[[10**20]*(N+1) for _ in range(N)]
for l in range(N):
    dp[l][l+1]=0

for length in range(1,N+1):
    for l in range(N):
        r=l+length
        if r>N:
            break

        ## [l+1,r) --> [l,r) の遷移
        # if l+1<N:
        #     dp[l][r]=min(dp[l][r],dp[l+1][r]+cum_A[r]-cum_A[l])
        
        ## [l,r-1) --> [l,r) の遷移
        # if r-1>=0:
        #     dp[l][r]=min(dp[l][r],dp[l][r-1]+cum_A[r]-cum_A[l])


        # 今回は上の2通りだけでなく, 境界を全探索
        # [l,pos) と [pos,r) に分ける
        for pos in range(l+1,r):
            dp[l][r]=min(dp[l][r],dp[l][pos]+dp[pos][r]+cum_A[r]-cum_A[l])

print(dp[0][N])