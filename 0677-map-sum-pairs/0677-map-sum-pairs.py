class Trie:
    def __init__(self):
        self.children = {}
        self.end = 0
class MapSum:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = Trie()
            
            node = node.children[char]
        node.end = val
        
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        ans = 0
        def dfs(nd):
            nonlocal ans
            ans += nd.end
            if not nd.children:
                return
            
            for nb in nd.children:
                dfs(nd.children[nb])
        
        dfs(node)
        return ans
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)