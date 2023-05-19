class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i):chr(i) for i in range(ord('a'),ord('z')+1)}

                
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
        
            

            
        for _  , eq in enumerate(equations):
            if eq[1] == "=":
                union(eq[0], eq[-1])
        # print(parent)
        
        for _  , eq in enumerate(equations):
            if eq[1] == "!":
                if find(eq[0]) == find(eq[-1]):
                    return False
        return True
        