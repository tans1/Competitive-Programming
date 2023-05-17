class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        
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




            # if x != parent[x]:
            #     temp = find(parent[x])
            #     parent[x] = temp 
            #     return temp
            # return x
        
        
        def union(x,y):
            par1,par2 = find(x), find(y)
            
            if par1 == par2:
                return 
            
            if rank[par1] == rank[par2]:
                # parent[par2] = par1
                rank[par1] += 1
                

            if rank[par1] < rank[par2]:
                parent[par1] = par2
                
            else:
                parent[par2] = par1
                            
        
        for u,v in edges:
            union(u,v)
        

        return find(source) == find(destination)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(edges) <= 1:
#             return True
#         graph = defaultdict(list)
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        

#         stack = [source]
#         visited = set()
        
#         while stack:
#             nd = stack.pop()
#             visited.add(nd)
            
#             for neighbours in graph[nd]:
#                 if neighbours == destination:
#                     return True
                
#                 if neighbours not in visited:
#                     stack.append(neighbours)
                    
#         return False