class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        visited = set()
        def dfs(node):
            nonlocal color, visited
            if node in visited:
                return True
            visited.add(node)
            temp = True
            for nb in graph[node]:
                if color[nb] == color[node]:
                    return False
                color[nb] = not color[node]
                temp = temp and dfs(nb)
            return temp
        
        
        for i in range(len(graph)):
            color[i] = 1
            if not dfs(i):
                return False
        return True