class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) <= 1:
            return True
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        stack = [source]
        visited = set()
        
        while stack:
            nd = stack.pop()
            visited.add(nd)
            
            for neighbours in graph[nd]:
                if neighbours == destination:
                    return True
                
                if neighbours not in visited:
                    stack.append(neighbours)
                    
        return False