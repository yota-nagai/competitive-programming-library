from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]  # 各頂点の親番号(自身が根なら-1)を管理
        self.size = [1]*n  # 各頂点が属する根付き木の頂点数を管理
        # self.min_node=[i for i in range(n)]  # 各頂点が属する根付き木の頂点番号の最小値を管理

	# xを含む根付き木の根番号を返す
    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x]) #経路圧縮
            return self.parents[x]
	
	# xとyが同じグループに属すか判定
    def isSame(self, x, y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False
        
	# xを含む根付き木とyを含む根付き木を合併
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return
        # Union by Size(小さい方を大きい方に合併)
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parents[y] = x
        self.size[x] += self.size[y]
        # self.min_node[x]=min(self.min_node[x],self.min_node[y])
        
	# xが属する根付き木の要素数を返す
    def Size(self, x):
        return self.size[self.root(x)]
    
    # xが属す根付き木に属する要素をリストで返す
    def members(self, x):
        return [i for i in range(self.n) if self.root(i) == self.root(x)]
        
	# すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x == -1]
    
    # 根付き木の数（連結成分の個数）を返す
    # unite処理をすべて終えてから最後に1回連結成分の個数を出力する場合は group_count で良い（O(n)） だが,
    # uniteなどを行うごとに連結成分の個数を知りたい場合は, 現時点での連結成分の個数を記録する変数cntを isSame を用いて更新していく方法（isSame==False --> cnt-=1）をとる
    def group_count(self):
        return len(self.roots())
    
	# {根番号:[その根付き木に含まれる要素のリスト],...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    # # xが属する根付き木における頂点番号の最小値
    # def get_min_node(self,x):
    #     return self.min_node[self.root(x)]

    # all_group_membersの結果を文字列で返す
    def __str__(self):
	    return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
