class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i):chr(i) for i in range(97,123)}


                
        def find(x):
            nonlocal parent
            
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != root:
                temp = parent[x]
                parent[x] = root
                x = temp   
            return root
        
        def union(x,y):
            nonlocal parent
            par1, par2 = find(x), find(y)

            if par1 == par2:
                return
            
            if par1 < par2:
                parent[par2] = par1
            if par1 > par2:
                parent[par1] = par2
        
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        
        ans = ""
        for i in range(len(baseStr)):
            ans += find(baseStr[i])
        return ans
        
