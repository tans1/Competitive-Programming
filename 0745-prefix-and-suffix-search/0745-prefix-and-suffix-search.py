class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for i in range(len(words)):
            currWord = words[i] + "#" + words[i]
            for j in range(len(currWord)):
                node = self.root
                for k in range(j,len(currWord)):
                    if currWord[k] not in node.children:
                        node.children[currWord[k]] = TrieNode()
                    
                    node = node.children[currWord[k]]
                    node.index = i
    def f(self, pref: str, suff: str) -> int:
        word = suff + "#" + pref
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return -1
            node = node.children[word[i]]
        return node.index
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)