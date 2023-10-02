class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insertWord(self,word):
        node = self.root
        res = ""
        flag = False
        prev = False
        for i  in range(len(word)):
            if word[i] in node.children:
                if not node.children[word[i]].end:
                    flag = True
                else:
                    res += word[i]
                    prev = True
            else:
                if i == 0 or (i + 1 == len(word) and prev == True):
                    res += word[i]
                else:
                    flag = True
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.end = True
        if not flag:
            return res
        else:
            return ""
    
    
    
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        temp = []
        for word in words:
            temp.append(Solution.insertWord(self,word))
        
        ans = sorted(temp, key = lambda x: (len(x),x))
        mx = len(ans[-1])
        i =  len(ans) - 1
        while i >= 0 and len(ans[i]) == mx:
            i -= 1
        return ans[i+1]
        
        