from collections import deque

N,M=map(int,input().split())
#mod=10**9+7
G=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)


def bfs(s):
    dq=deque()
    dq.append(s)
    dist[s]=0
    cnt[s]=1

    while len(dq)>0:
        i=dq.popleft()
        for j in G[i]:
            if dist[j]==-1:
                dist[j]=dist[i]+1
                cnt[j]=cnt[i]
                dq.append(j)
            else:
                if dist[j]==dist[i]+1:
                    cnt[j]+=cnt[i]
            #cnt[j]%=mod

dist=[-1]*N
cnt=[0]*N    #最短経路数のカウント
bfs(0)

print(cnt[N-1])