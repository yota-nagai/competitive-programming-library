# 個数制限なしナップサック問題  https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja

N,W=map(int,input().split())
vs,ws=[],[]  # 価値リスト, 重さリスト
for _ in range(N):
    v,w=map(int,input().split())
    vs.append(v)
    ws.append(w)

dp=[[0]*(W+1) for _ in range(N+1)]
dp[0][0]=0
for i in range(1,N+1):
    for j in range(W+1):
        dp[i][j]=dp[i-1][j]
        if j-ws[i-1]>=0:
            dp[i][j]=max(dp[i][j],dp[i][j-ws[i-1]]+vs[i-1])

print(max(dp[-1]))