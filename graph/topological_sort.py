# トポロジカルソート
# サイクルが含まれるかの判定（DAGかどうか）としても機能：サイクルが含まれる場合はFalseを返す

def topological_sort(graph):
    N=len(graph)
    indegree=[0]*N
    for i in range(N):
        for j in graph[i]:
            indegree[j]+=1 

    stack=[]
    for i in range(N):
        if indegree[i]==0:
            stack.append(i)

    topological=[]
    cnt=0
    while len(stack)>0:
        i=stack.pop()
        cnt+=1
        topological.append(i)
        for j in graph[i]:
            indegree[j]-=1
            if indegree[j]==0:
                stack.append(j)

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

ans=topological_sort(graph)
if ans==False:
    print(-1)
else:
    print(*[i+1 for i in ans])


# 終点が頂点vである部分グラフのトポロジカルソートのみを得たい場合は, 
# 辺を逆に張ったグラフ上でBFS/DFSを行い, vから到達可能な頂点集合Sを求める --> topological_sort()の結果から, Sに含まれる頂点のみを抽出
