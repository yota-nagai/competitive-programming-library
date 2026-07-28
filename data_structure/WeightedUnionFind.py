from collections import defaultdict

class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]  # 各頂点の親番号(自身が根なら-1)を管理
        self.size = [1]*n  # 各頂点が属する根付き木の要素数を管理
        self.diff_weight = [0]*n  # 親からの重みを管理
	
	# xを含む根付き木の根番号を返す
    def root(self, x):
        if self.parents[x]==-1:
            return x
        else:
            # 経路圧縮＆差分重みの更新
            r=self.root(self.parents[x])
            self.diff_weight[x]+=self.diff_weight[self.parents[x]]
            self.parents[x]=r
            return r
	
    # 各ノードの重みを返す
    def weight(self,x):
        self.root(x)  # 経路圧縮  
        return self.diff_weight[x]

    # xとyの重みの差を出力
    def diff(self,x,y):
        return self.weight(y)-self.weight(x) 

	# xとyが同じグループに属すか判定
    def isSame(self,x,y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False

	# xを含む根付き木とyを含む根付き木を合併（weight(y)-weight(x)=wを満たすように）
    def unite(self,x,y,w):
        w+=self.weight(x)
        w-=self.weight(y)

        x=self.root(x)
        y=self.root(y)
        if x==y:
            return
        
        # Union by Size(要素数が小さい方を大きい方に合併)
        if self.size[x]<self.size[y]:
            x,y=y,x
            w=-w

        self.parents[y]=x
        self.diff_weight[y]=w
        self.size[x]+=self.size[y]
        
	# xが属する根付き木の要素数を返す
    def Size(self,x):
        return self.size[self.root(x)]
    
    # xが属す根付き木に属する要素をリストで返す
    def members(self,x):
        res=[]
        for i in range(self.n):
            if self.root(i)==self.root(x):
                res.append(i)
        return res
        
	# すべての根の要素をリストで返す
    def roots(self):
        res=[]
        for i,p in enumerate(self.parents):
            if p==-1:
                res.append(i)
        return res
    
    # 根付き木の数（連結成分の個数）を返す
    # unite処理をすべて終えてから最後に1回連結成分の個数を出力する場合は group_count で良い（O(n)） が,
    # uniteなどを行うごとに連結成分の個数を知りたい場合は, 現時点での連結成分の個数を記録する変数cntを isSame を用いて更新していく方法（isSame==False --> cnt-=1）をとる
    def group_count(self):
        return len(self.roots())
    
	# {根番号:[その根付き木に含まれる要素のリスト],...}のdefaultdictを返す
    def all_group_members(self):
        res=defaultdict(list)
        for i in range(self.n):
            res[self.root(i)].append(i)
        return res



# unite()では子グループの根の重みしか更新されず, それより下流の頂点の重みは次にroot()などが呼び出されるまで放置される（遅延評価）ことに注意
# 必要に応じてroot()など（内部でroot()を呼び出すメソッドならok)を呼び出して更新する

# それをせずとも,
# 重み取得時に「diff_weightを参照」ではなく「weight()を呼び出す」とすることで, 最新の重みの値であることが保証される！




N,M=map(int,input().split())
wuf=WeightedUnionFind(N)
for _ in range(M):
    L,R,D=map(int,input().split())
    L-=1
    R-=1
    if wuf.isSame(L,R)==False:
        wuf.unite(L,R,D)
    else:
        if wuf.diff(L,R)!=D:
            print("No")
            exit()

print("Yes")