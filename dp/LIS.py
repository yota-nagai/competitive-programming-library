## 最長増加部分列（LIS）問題

N=int(input())
A=list(map(int,input().split()))

dp=[0]*N  # 最後の要素がA_iである部分列のうち, 最長のものの長さ
L=[10**20]*(N+1)  # 長さxの部分列の最後の要素として考えられる最小値（dp[k] = x を満たすkにおけるA_kの最小値）
L[0]=-1

for i in range(N):
    ok,ng=-1,N
    while ng-ok>1:
        m=(ok+ng)//2
        if L[m]<A[i]:
            ok=m
        else:
            ng=m
    dp[i]=ok+1
    L[dp[i]]=min(L[dp[i]],A[i])

print(max(dp))

