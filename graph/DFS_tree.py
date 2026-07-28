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
    for nv in graph[v]:
        if nv==p:
            continue
        subtree_size[v]+=subtree_size[nv]


N=int(input())
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
subtree_size=[0]*N  # 各頂点を根とした部分木に含まれる頂点数 

dfs(0,-1,0)