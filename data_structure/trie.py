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