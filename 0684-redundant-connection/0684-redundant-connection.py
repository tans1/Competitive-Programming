class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1 for _ in range(n+1)]
        parent = [i for i in range(n+1)]
        
        def find(x):
            nonlocal parent
            root = x
            while root != parent[root]:
                root = parent[root]

            while x != root:
                par = parent[x]
                parent[x] = root
                x = par
            return root
        
        def union(x,y):
            par1,par2 = find(x), find(y)
            
            if par1 == par2:
                return [x,y]
            
            if rank[par1] == rank[par2]:
                rank[par1] += 1
                

            if rank[par1] < rank[par2]:
                parent[par1] = par2
                
            else:
                parent[par2] = par1
        
        for u,v in edges:
            temp = union(u,v)
            
            if temp:
                return temp
        return []