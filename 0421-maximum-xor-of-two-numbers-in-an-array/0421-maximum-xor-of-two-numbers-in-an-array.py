class TrieNode:
    def __init__(self):
        self.children = {}
        # self.end = 0
        
class Solution:
    def __init__(self):
        self.root = {}
    def insertBinary(self, number):
        node = self.root
        for n in number:
            if n not in node:
                node[n] = {}
            node = node[n]
        # node.end = int(number,2)
    def findMax(self,number):
        opp = {
            "0" : "1",
            "1" : "0"
        }
        temp = ""
        node = self.root
        for n in number:
            if opp[n] in node:
                temp += opp[n]
                node = node[opp[n]]
            else:
                temp += n
                node = node[n]
        return int(temp,2)
        # return node.end
        
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        for n in nums:
            binary_format = bin(n)[2:].zfill(32)
            Solution.insertBinary(self,binary_format)
        
        ans = 0
        for n in nums:
            binary_format = bin(n)[2:].zfill(32)
            ans = max(ans,Solution.findMax(self,binary_format)^n)
        return ans
