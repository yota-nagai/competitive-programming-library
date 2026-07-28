#巡回セールスマン問題

N=int(input())
A=[]
for _ in range(N):
    a=list(map(int,input().split()))
    A.append(a)

ALL=1<N

#cost[n][i] 訪れた場所の集合がnで、現在いる場所がiであるときのコスト最小値
cost=[[10**100]*N for _ in range(ALL)]

#最初にいる始点はnに含めずにゴールのときに含めるようにする
cost[0][0]=0

def has_bit(n,i):
    return (n&(1<<N)>0)

for n in range(ALL):
    for i in range(N):
        #iからjへ遷移
        for j in range(N):
            if has_bit(n,j) or i==j:
                continue
            cost[n|(1<<j)][j]=min(cost[n|(1<<j)][j],cost[n][i]+A[i][j])

print(cost[ALL-1][0])
