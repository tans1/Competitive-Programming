class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = max(len(isConnected[0]), len(isConnected))
        graph = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i + 1 not in graph:
                    graph[i+1] = []
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1)
        
        def dfs(node,visited):
            visited.add(node)
            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb, visited)
            return 1

        ans = 0
        visited = set()
        for i in range(1,n + 1):
            if i not in visited:
                ans += dfs(i, visited)
        return ans