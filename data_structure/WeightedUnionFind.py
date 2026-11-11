from collections import defaultdict

class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n                     # 各頂点の親番号（自身が根なら-1）を管理
        self.size = [1]*n                         # 各頂点が属する根付き木の要素数を管理  ※ 根の頂点のみ
        self.diff_weight = [0]*n                  # 親からの重みを管理  ※ 取得時は weight() を呼び出す
        self.group_cnt=n                          # 根付き木（連結成分）の数
        self.next_node=[i for i in range(n)]      # 同一根付き木の頂点を巡回する際の, 次の頂点を管理

	# xが属する根付き木の根番号を返す
    def root(self, x):
        if self.parents[x]==-1:
            return x
        else:
            # 経路圧縮＆差分重みの更新
            r=self.root(self.parents[x])
            self.diff_weight[x]+=self.diff_weight[self.parents[x]]
            self.parents[x]=r
            return r

	# xとyが同じ根付き木に属すか判定
    def isSame(self,x,y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False

	# weight(y)-weight(x)=w となるように, xが属する根付き木とyが属する根付き木を合併   
    def unite(self,x,y,w):
        w+=self.weight(x)
        w-=self.weight(y)
        x=self.root(x)
        y=self.root(y)
        if x==y:
            return
        # Union by Size (頂点数が小さい方を大きい方に合併)
        if self.size[x]<self.size[y]:
            x,y=y,x
            w=-w
        self.parents[y]=x
        self.diff_weight[y]=w
        self.size[x]+=self.size[y]
        self.group_cnt-=1
        self.next_node[x],self.next_node[y]=self.next_node[y],self.next_node[x]

    # 根を基準（重み0）としたxの重みを返す
    def weight(self,x):
        self.root(x)  # 経路圧縮  
        return self.diff_weight[x]

    # xとyの重みの差 weight(y)-weight(x) を返す    ※ xとyは同じ根付き木に含まれる前提
    def diff(self,x,y):
        return self.weight(y)-self.weight(x) 

	# xが属する根付き木の頂点数を返す
    def Size(self,x):
        return self.size[self.root(x)]
    
    # xが属する根付き木に属する全頂点をリストで返す
    def members(self, x):
        res=[x]
        i=self.next_node[x]
        while i!=x:
            res.append(i)
            i=self.next_node[i]
        return res
        
	# すべての根をリストで返す
    def roots(self):
        res=[]
        for i,p in enumerate(self.parents):
            if p==-1:
                res.append(i)
        return res
    
    # 根付き木（連結成分）の個数を返す
    def group_count(self):
        return self.group_cnt

	# {根番号:[その根付き木に含まれる頂点のリスト],...}のdefaultdictを返す
    def all_group_members(self):
        res=defaultdict(list)
        for i in range(self.n):
            res[self.root(i)].append(i)
        return res