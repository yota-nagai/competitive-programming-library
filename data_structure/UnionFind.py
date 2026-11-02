from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]  # 各頂点の親番号(自身が根なら-1)を管理
        self.size = [1]*n  # 各頂点が属する根付き木の頂点数を管理
        self.next_node=[i for i in range(n)]  # 同一グループ（根付き木）の頂点を巡回する際の, 次の頂点を管理
        self.group_cnt=n  # グループの数（根付き木の数）
        self.min_node=[i for i in range(n)]  # 各頂点が属する根付き木における, 頂点番号の最小値を管理
        self.max_node=[i for i in range(n)]  # 各頂点が属する根付き木における, 頂点番号の最大値を管理

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
        self.next_node[x],self.next_node[y]=self.next_node[y],self.next_node[x]
        self.group_cnt-=1
        self.min_node[x]=min(self.min_node[x],self.min_node[y])
        self.max_node[x]=max(self.max_node[x],self.max_node[y])
        
	# xが属する根付き木の要素数を返す
    def Size(self, x):
        return self.size[self.root(x)]
    
    # xが属す根付き木に属する要素をリストで返す
    def members(self, x):
        res=[x]
        i=self.next_node[x]
        while i!=x:
            res.append(i)
            i=self.next_node[i]
        return res
        
	# すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x == -1]
    
    # グループの数（根付き木の数）を返す
    def group_count(self):
        return self.group_cnt
    
	# {根番号:[その根付き木に含まれる要素のリスト],...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    # xが属する根付き木における頂点番号の最小値を返す
    def get_min_node(self,x):
        return self.min_node[self.root(x)]

    # xが属する根付き木における頂点番号の最大値を返す
    def get_max_node(self,x):
        return self.max_node[self.root(x)]

    # all_group_membersの結果を文字列で返す
    def __str__(self):
	    return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())