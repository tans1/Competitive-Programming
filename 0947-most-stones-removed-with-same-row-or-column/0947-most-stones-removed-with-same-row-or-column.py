class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        par = [i for i in range(len(stones))]
        size = [1 for i in range(len(stones))]
        
        def find(x):
            root = x
            while root != par[root]:
                root = par[root]
            
            while x != root:
                temp = par[x]
                par[x] = root
                x = temp
            
            return root
        
        def union(x,y):
            par1, par2 = find(x), find(y)
            
            if par1 != par2:
                par[par2] = par1
                size[par1] += size[par2]
        
        for i in range(len(stones)-1):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
                    
        seen = set()
        ans = 0
        for i in range(len(size)):
            parent = find(i)
            if parent not in seen:
                ans += size[parent] - 1
                seen.add(parent)
        return ans
                
        
            