import sys
sys.setrecursionlimit(10**8)

# 木の直径：木の中で最も離れた2頂点間の距離 

def tree_diameter(graph,weighted):
    """ 
    (木の直径, それを構成するパス) を返す   ※ 辺の重みは非負が前提
    weighted = True : 重み付き木 
    weighted = False: 重みなし木
    """
    if weighted:
        def dfs(i):
            visited[i]=True
            for j,c in graph[i]:
                if not visited[j]:
                    dist[j]=dist[i]+c
                    previous_node[j]=i
                    dfs(j)
    else:
        def dfs(i):
            visited[i]=True
            for j in graph[i]:
                if not visited[j]:
                    dist[j]=dist[i]+1
                    previous_node[j]=i
                    dfs(j)     
     
    n=len(graph)
    visited,dist,previous_node=[False]*n,[-1]*n,[-1]*n
    dist[0]=0
    dfs(0)
    p1=dist.index(max(dist))
    visited,dist,previous_node=[False]*n,[-1]*n,[-1]*n
    dist[p1]=0
    dfs(p1)
    p2=dist.index(max(dist))

    path=[]
    i=p2
    while True:
        path.append(i)
        if i==p1:
            break
        i=previous_node[i]

    return dist[p2],path



# ------------------------------------------------------------
N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    # 重み付きケース
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,w))
    graph[v].append((u,w))

    # 重みなしケース
    # u,v=map(int,input().split())
    # u-=1
    # v-=1
    # graph[u].append(v)
    # graph[v].append(u)