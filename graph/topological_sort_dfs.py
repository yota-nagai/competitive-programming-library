import sys
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())

graph=[[] for _ in range(N)]
indegree=[0]*N
for _ in range(M):
    x,y=map(int,input().split())
    x-=1
    y-=1
    graph[x].append(y)
    indegree[y]+=1

# root=set() 
# for v in range(N):
#     if indegree[v]==0:
#         root.add(v)


def dfs(i):
    visited[i]=True
    for j in graph[i]:
        if visited[j]:
            continue
        dfs(j)
    topological_sort.append(i)

topological_sort=[]
visited=[False]*N
for i in range(N):
    if not visited[i]:
        dfs(i)
topological_sort.reverse()


# トポロジカルソートの結果を, 各連結グループごとに
# group=[]
# g=[topological_sort[0]]
# for i in range(1,N):
#     v=topological_sort[i]
#     if v not in root:
#         g.append(v)
#     else:
#         group.append(g)
#         g=[v]
# group.append(g)

