class TrieNode:
    def __init__(self):
        self.children = {}
        self.end =  False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
    def search(self, word: str) -> bool:
        node = self.root
        
        def helper(nd,i):
            if i >= len(word):
                return nd.end
            if not(word[i] in nd.children or word[i] == "."):
                return False
            if word[i] in nd.children:
                nd = nd.children[word[i]]
                return helper(nd,i+1)
            else:
                for nb in nd.children:
                    
                    if helper(nd.children[nb], i+1):
                        return True
                return False
                    
        return helper(node,0)
                



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)