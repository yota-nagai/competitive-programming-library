# https://atcoder.jp/contests/dp/submissions/73205201

N=int(input())
A=list(map(int,input().split()))

# dp[i][j]:= 区間a_i, a_(i+1),..., a_(j-1)の状態の局面から出発して, 双方最善を尽くしたときの X-Y 
dp=[[None]*(N+1) for _ in range(N)]

# length: [i,j)の区間長j-i 
# length = 0,1,2,...から順にdpテーブル更新処理

for length in range(N+1):
    for i in range(N):
        j=i+length
        if j>N:
            break
        if length==0:
            dp[i][i]=0
            continue

        # N-length = 0,2,4,...なら先手番 X-Yを最大化
        #          = 1,3,5,...なら後手番 X-Yを最小化
        if (N-length)%2==0:
            dp[i][j]=-10**20
            if i+1<N:
                dp[i][j]=max(dp[i][j],dp[i+1][j]+A[i])
            if j-1>=0:
                dp[i][j]=max(dp[i][j],dp[i][j-1]+A[j-1])
        else:
            dp[i][j]=10**20
            if i+1<N:
                dp[i][j]=min(dp[i][j],dp[i+1][j]-A[i])
            if j-1>=0:
                dp[i][j]=min(dp[i][j],dp[i][j-1]-A[j-1])

print(dp[0][N])