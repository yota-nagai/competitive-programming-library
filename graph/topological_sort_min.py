# 辞書順最小のトポロジカルソートを求める
# サイクルが含まれるかの判定（DAGかどうか）としても機能：サイクルが含まれる場合はFalseを返す

import heapq

def topological_sort_min(graph):
    N=len(graph)
    indegree=[0]*N
    for i in range(N):
        for j in graph[i]:
            indegree[j]+=1 
    hq=[]
    for i in range(N):
        if indegree[i]==0:
            heapq.heappush(hq,i)

    topological=[]
    cnt=0
    while len(hq)>0:
        i=heapq.heappop(hq)
        cnt+=1
        topological.append(i)
        for j in graph[i]:
            indegree[j]-=1
            if indegree[j]==0:
                heapq.heappush(hq,j)

    if cnt<N:
        return False  # 有向サイクルあり
    else:
        return topological


N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)

ans=topological_sort_min(graph)
if ans==False:
    print(-1)
else:
    print(*[i+1 for i in ans])