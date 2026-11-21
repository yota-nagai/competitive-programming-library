## 木上のDFS ##

import sys
sys.setrecursionlimit(10**8)

# dfs(頂点v, vの親, vの根からの距離)
def dfs(v,p,d):  
    depth[v]=d
    for nv in graph[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)
    
    subtree_size[v]=1
    subtree_large[v].append(X[v])
    subtree_small[v].append(X[v])
    for nv in graph[v]:
        if nv==p:
            continue
        subtree_size[v]+=subtree_size[nv]
        subtree_large[v]+=subtree_large[nv]
        subtree_large[v]=sorted(subtree_large[v],reverse=True)[:K]
        subtree_small[v]+=subtree_small[nv]
        subtree_small[v]=sorted(subtree_small[v])[:K]


N=int(input())
X=list(map(int,input().split()))  # 各頂点に書かれている数字
K=20                              # subtree_large/small で管理する数字の個数上限
graph=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
    
# 行きがけ処理（根から下へ）
depth=[0]*N  # 各頂点の根からの距離（深さ）

# 帰りがけ処理（葉から上へ）  木DPのときコッチの配列
subtree_size=[0]*N                    # 各頂点を根とする部分木に含まれる頂点数 
subtree_large=[[] for _ in range(N)]  # 各頂点を根とする部分木に属す頂点に書かれた数のうち, 大きい方から順に K 個を格納
subtree_small=[[] for _ in range(N)]  # 各頂点を根とする部分木に属す頂点に書かれた数のうち, 小さい方から順に K 個を格納

dfs(0,-1,0)    #頂点 0 を根としてDFS