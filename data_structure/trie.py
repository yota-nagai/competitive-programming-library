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