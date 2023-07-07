class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [0 for _ in range(n+1)]
        roads = sorted(roads, key = lambda x:x[0])
        temp = {}
        
        def find(x):
            root = x
            while root != parent[root] and parent[root] != 0:
                root = parent[root]
            
            while x != root:
                ancestor = parent[x]
                parent[x] = root
                x = ancestor
            return root
        
        def union(l,m,val):
            par1 = find(l)
            par2 = find(m)
            
            if par1 not in temp and par2 not in temp:
                temp[par1] = val
                parent[par2] = par1
            elif par2 not in temp:
                temp[par1] = min(temp[par1],val)
                parent[par2] = par1
            elif par1 not in temp:
                temp[par2] = min(temp[par2],val)
                parent[par1] = par2
            else:
                parent[par2] = par1
                temp[par1] = min(temp[par1], temp[par2],val)

        for i,j,k in roads:
            union(i,j,k)
        return temp[find(1)]