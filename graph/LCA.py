"""
最近共通祖先 (LCA: Lowest Common Ancestor)
根付き木において, 2頂点u,vの共通の祖先のうち最も近いところにあるもの
"""

class LCA:
    def __init__(self,graph,root):
        self.n=len(graph)
        self.root=root
        self.K=(self.n-1).bit_length()
        self.parent=[[-1]*self.n for _ in range(self.K)]
        self.depth=[-1]*self.n

        import sys
        sys.setrecursionlimit(10**8)
        def dfs(v,p,d):  
            self.depth[v]=d
            for nv in graph[v]:
                if nv==p:
                    continue
                self.parent[0][nv]=v
                dfs(nv,v,d+1)        
        dfs(self.root,-1,0)

        # ダブリングで parent[k][v]:=頂点vから2^k個上の祖先 を求める
        for k in range(1,self.K):
            for v in range(self.n):
                if self.parent[k-1][v]!=-1:
                    self.parent[k][v]=self.parent[k-1][self.parent[k-1][v]]


    def get_lca(self,u,v):
        """ 頂点uと頂点vのLCAを返す """
        if self.depth[u]<self.depth[v]:
            u,v=v,u
        # uとvの深さを揃える
        diff=self.depth[u]-self.depth[v]
        for k in range(self.K):         
            if diff&(1<<k)>0:
                u=self.parent[k][u]
        if u==v:
            return u
        # 合流点の1つ手前までu,vを動かす
        for k in reversed(range(self.K)):
            if self.parent[k][u]!=self.parent[k][v]:
                u=self.parent[k][u]
                v=self.parent[k][v]
        return self.parent[0][u]

    def get_dist(self,u,v):
        """ 頂点uと頂点vの距離を返す """
        lca=self.get_lca(u,v)
        return self.depth[u]+self.depth[v]-2*self.depth[lca]

    def is_on_path(self,u,v,a):
        """ 頂点uと頂点vを結ぶパス上に頂点aが存在するか（True/False）を返す """
        return self.get_dist(u,a)+self.get_dist(a,v)==self.get_dist(u,v) 

# ------------------------------------------------------------
N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)

lca=LCA(graph,0)   # 頂点0を根とする