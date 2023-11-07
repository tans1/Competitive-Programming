class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.hp = []
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insertWord(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]        
            heapq.heappush(node.hp, word)
                
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        for product in products:
            self.insertWord(product)
        ans = []
        node = self.root
        for char in searchWord:
            
            node = node.children[char]
            ans.append(heapq.nsmallest(3,node.hp))
        return ans
        
        