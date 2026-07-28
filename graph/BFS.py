from collections import deque

def bfs(s):
    dist[s]=0
    dq=deque()
    dq.append(s)
    while len(dq)>0:
        i=dq.popleft()
        for j in graph[i]:
            if dist[j]==-1:
                dist[j]=dist[i]+1
                previous_node[j]=i  #経路復元用
                dq.append(j)

#経路復元（到達不可能なら復元不可）
def restore_path(start,goal):
    path=[]
    i=goal
    while True:
        path.append(i+1)
        if i==start:
            break
        i=previous_node[i]
    return list(reversed(path))



N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)  #無向グラフの場合のみ
    
dist=[-1]*N
previous_node=[-1]*N

#dist[i]=-1ならばiへの到達不可能