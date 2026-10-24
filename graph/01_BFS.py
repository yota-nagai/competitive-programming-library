# 全ての辺の重みが0か1であるグラフに対するBFS

from collections import deque

def bfs01(s):
    dist[s]=0
    dq=deque()
    dq.append(s)
    done=[False]*len(dist)
    while len(dq)>0:
        i=dq.popleft()
        if done[i]:
            continue
        for j,c in graph[i]:
            if c==0 and dist[j]>dist[i]:
                dq.appendleft(j)
                dist[j]=dist[i]
            elif c==1 and dist[j]>dist[i]+1:
                dq.append(j)
                dist[j]=dist[i]+1
        done[i]=True


N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append((b,c))
    graph[b].append((a,c))  #無向グラフの場合

inf=10**18
dist=[inf]*N