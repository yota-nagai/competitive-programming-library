# Functional Graph : すべての頂点の出次数が 1 である有向グラフ
# 各連結成分は「ただ1つのサイクル」と「0個以上の, サイクルに接続する有向木」で構成される

class FunctionalGraph:
    def __init__(self,to):
        self.to=to
        self.n=len(to)
        self.in_cycle=[False]*self.n              # 各頂点がサイクル上にあるかどうか
        self.cycle_list=[]                        # 各サイクルのパスを格納
        self.leader=[-1]*self.n                   # 各頂点が属す連結成分における, サイクルの代表頂点（同じ連結成分に属す頂点同士は同じ値になる）
        self.cycle_size=[0]*self.n                # 各頂点が属す連結成分における, サイクルのサイズ     
        self.to_rev=[[] for _ in range(self.n)]   # 逆向きに辺を張ったグラフ
        for i in range(self.n):
            self.to_rev[to[i]].append(i)

        seen=[False]*self.n     
        finished=[False]*self.n
        for i in range(self.n):
            if finished[i]:
                continue
            pos=i
            history=[]
            while True:
                seen[pos]=True
                history.append(pos)
                pos=self.to[pos]
                if seen[pos] and not finished[pos]:
                    flag=True
                    break
                elif finished[pos]:
                    flag=False
                    break
            if flag:
                cycle=[]
                self.leader[pos]=pos
                v=pos
                while True:
                    cycle.append(v)
                    self.in_cycle[v]=True
                    v=self.to[v]
                    if v==pos:
                        break
                self.cycle_list.append(cycle)
                siz=len(cycle)
            else:
                siz=self.cycle_size[pos]
            for j in history:
                finished[j]=True
                self.leader[j]=self.leader[pos]
                self.cycle_size[j]=siz

    def cycles(self):
        """
        すべてのサイクルを列挙し, [[サイクル1のパス],[サイクル2のパス],...,[サイクルkのパス]] の形で返す     k : 連結成分の個数 
        ※ 終点（= 始点）は含めない
        """
        return self.cycle_list 

    def dist_to_cycle(self):
        """
        各頂点のサイクルまでの距離を計算し（多始点BFS）, リストで返す   
        """
        from collections import deque
        dist=[-1]*self.n
        dq=deque()
        for s in range(self.n):
            if self.in_cycle[s]:
                dist[s]=0
                dq.append(s)
        while len(dq)>0:
            i=dq.popleft()
            for j in self.to_rev[i]:
                if dist[j]==-1:
                    dist[j]=dist[i]+1
                    dq.append(j)
        return dist



            
N=int(input())
to=list(map(int,input().split()))  # 各頂点から出る辺がどの頂点に向かうか
to=[i-1 for i in to]               # 0-indexedに 

FG=FunctionalGraph(to)