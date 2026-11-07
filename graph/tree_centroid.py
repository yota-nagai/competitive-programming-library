import sys
sys.setrecursionlimit(10**8)

"""
木の重心
定義：その頂点を削除したときに残るすべての部分木の頂点数が N/2 以下（残る部分木のうち最大サイズのものの頂点数が最小）となる頂点
性質：すべての頂点からの距離の総和が最小となる
"""

# 木の重心を求める     ※ 1つ or 2つ（その場合は隣接）存在するのでリストで返す
def tree_centroid(graph):
    def dfs(v,parent):  
        for nv in graph[v]:
            if nv==parent:
                continue
            dfs(nv,v)
        
        subtree_size[v]=1
        flag=True
        for nv in graph[v]:
            if nv==parent:
                continue
            subtree_size[v]+=subtree_size[nv]
            if subtree_size[nv]>N//2:
                flag=False
        if N-subtree_size[v]>N//2:
            flag=False
        if flag:
            centroid.append(v)

    N=len(graph)
    subtree_size=[0]*(len(graph))
    centroid=[]
    dfs(0,-1)
    return centroid



# 木の構築
N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)