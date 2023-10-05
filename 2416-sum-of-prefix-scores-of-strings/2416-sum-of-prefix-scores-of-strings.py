class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.end = True

    def searchWord(self, word):
        node = self.root
        ans = 0
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
                ans += node.count
        
        return ans
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            Solution.insertWord(self,word)
        
        ans = []
        for word in words:
            ans.append(Solution.searchWord(self,word))
        return ans
        
            
        
        
        
        
        
        
        
        