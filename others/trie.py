class TrieNode:
    """各頂点の情報をもつ"""
    def __init__(self):
        self.children={}         # {移動先の文字_1: 対応するTrieNode, 移動先の文字_2: 対応するTrieNode, ... }
        self.is_end=False        # この頂点で終わる単語が登録されているか


class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        """文字列を追加する"""
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end=True

    def search(self,word):
        """文字列を検索する（一致するものが登録されているかを判定）"""
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_end