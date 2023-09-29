class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end += 1

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            Solution.insertWord(self,word)
        
        curr = self.root
        count = 0
        
        def traverse(i,node):
            nonlocal count
            count += node.end
            
            if not node.children:
                return
            
            for child in node.children:
                for j in range(i,len(s)):
                    if s[j] == child:
                        traverse(j+1, node.children[child])
                        break
            return
        traverse(0,curr)
        return count
        
            
            
        
        