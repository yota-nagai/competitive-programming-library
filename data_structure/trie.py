class TrieNode:
    """各頂点の情報をもつ"""
    def __init__(self):
        self.children={}        # {移動先の文字_1: 対応するTrieNode, 移動先の文字_2: 対応するTrieNode, ... }
        self.pass_cnt=0         # この頂点を通過する文字列の数
        self.end_cnt=0          # この頂点で終わる文字列の数


class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        """文字列を追加する"""
        node=self.root
        node.pass_cnt+=1
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
            node.pass_cnt+=1
        node.end_cnt+=1

    def count_word(self,word):
        """指定した文字列の登録数を返す"""
        node=self.root
        for char in word:
            if char not in node.children:
                return 0
            node=node.children[char]
        return node.end_cnt

    def count_prefix(self,prefix):
        """指定した接頭辞をもつ文字列の登録数を返す"""
        node=self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node=node.children[char]
        return node.pass_cnt

    def get_path(self,word):
        """
        ・単語 word をTrie上で辿ったときに通る経路を, [word[0]に対応するTrieNode, word[1]に対応するTrieNode, ...] で返す
        ・word の最後まで辿れた（len(返したリスト) = len(word) となる）場合, それ以降の頂点までを辿って得られる文字列は word を接頭辞としてもつ
        """
        node=self.root
        res=[]
        for char in word:
            if char not in node.children:
                return res
            node=node.children[char]
            res.append(node)
        return res

    def delete_word(self,word,k):
        """単語 word を k 個 削除する   ※その操作が可能であることをcount_word()により確認してから使用する"""
        node=self.root
        node.pass_cnt-=k
        for char in word:
            node=node.children[char]
            node.pass_cnt-=k
        node.end_cnt-=k

    def delete_prefix(self,prefix):
        """prefixを接頭辞としてもつ単語をすべて削除して, 削除した数を返す"""
        if len(prefix)==0:
            return 0
        path=self.get_path(prefix)
        if len(path)!=len(prefix):
            return 0
        prefix_last=path[-1]
        remove_cnt=prefix_last.pass_cnt
        # 根から "prefixの終点の1つ前の頂点" までのpass_cntを更新
        self.root.pass_cnt-=remove_cnt
        for node in path[:-1]:
            node.pass_cnt-=remove_cnt
        # "prefixの終点の1つ前の頂点" と "prefixの終点" を結ぶ辺を切断
        char=prefix[-1]
        if len(prefix)==1:
            del self.root.children[char]
        else:
            del path[-2].children[char]
        return remove_cnt

    def get_max_lcp(self,word,case): 
        """
        ・単語 word に対して, 「Trieが保持する単語との最長共通接頭辞（LCP）」のうち最長のものを返す
        ・単語群 S_1,...,S_n （重複ok）が Trie に保持されているときに,
            case = 1 : 与えられた単語 T（任意の文字列）について, 単語 S_1,...,S_n とのLCPのうち最長のものを探すケース   
            case = 2 : 各 S_i について, 他の単語 S_j (i≠j) とのLCPのうち最長のものを探すケース
        """
        node=self.root
        res=[]
        for char in word:
            if (char in node.children) and (node.children[char].pass_cnt>=case):
                node=node.children[char]
                res.append(char)
            else:
                break
        return "".join(res)

    def get_lcp_sum(self,word,case):
        """
        ・単語 word に対して, 「Trieが保持する単語との最長共通接頭辞（LCP）」の長さの総和を返す
        ・単語群 S_1,...,S_n （重複ok）が Trie に保持されているときに,
            case = 1 : 与えられた単語 T（任意の文字列）について, 単語 S_1,...,S_n とのLCPの長さの総和を得るケース   
            case = 2 : 各 S_i について, 他の単語 S_j (i≠j) とのLCPの長さの総和を得るケース
        """
        node=self.root
        depth=0
        res=0
        for i in range(len(word)):
            char=word[i]
            if (char in node.children) and (node.children[char].pass_cnt>0):
                res+=(node.pass_cnt-node.children[char].pass_cnt-node.end_cnt)*depth   # 進まない分岐先の分
                node=node.children[char]
                depth+=1
                if i==len(word)-1:
                    res+=(node.end_cnt-(case-1))*depth
                else:
                    res+=node.end_cnt*depth
            else:
                break
        res+=(node.pass_cnt-node.end_cnt)*depth
        return res