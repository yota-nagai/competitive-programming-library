import sys
sys.setrecursionlimit(10**8)

N,M=map(int,input().split())
G=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

visited=[False]*N

def dfs(i):
    visited[i]=True
    for j in G[i]:
        if not visited[j]:
            dfs(j)
            #この深さに書くと、1つの頂点jを訪れる度、そののちに処理が行われる
    #この深さに書くと、全ての頂点jを訪れたのちに処理が行われる

dfs(0)



"""
無向グラフの頂点(vertex)と辺(edge)の数のカウント
"""
def dfs(i):
    global vertex,edge
    visited[i]=True
    vertex+=1
    for j in G[i]:
        edge+=1
        if not visited[j]:
            dfs(j)

visited=[False]*N
for i in range(N):
    if not visited[i]:
        vertex,edge=0,0
        dfs(i)
        edge//=2


# グラフに含まれるサイクルの数＝edge-vertex+1


"""
次数：degree 
入次数：indegree
出次数：outdegree
"""


"""
パスグラフである必要十分条件
グラフが連結(N頂点) and 辺がN-1本 and 全頂点の次数が2以下
"""


"""
木のオイラーツアー：根からDFSで全ての辺を2回ずつ通って根に帰ってくるパス
https://ikatakos.com/pot/programming_algorithm/graph_theory/eular_tour
"""

# ex) 訪問頂点を順にansに入れる
ans=[]
def dfs(i):
    ans.append(i)
    visited[i]=True
    for j in G[i]:
        if not visited[j]:
            dfs(j)
            ans.append(i)