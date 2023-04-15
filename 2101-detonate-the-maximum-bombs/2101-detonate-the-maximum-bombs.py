class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            x,y,r1 = bombs[i]
            for j in range(len(bombs)):
                if i != j:
                    a,b,r2 = bombs[j]
                    if (a-x)**2 + (b-y)**2 <= r1**2:
                        graph[(x,y)].append((a,b))
                        
        
        def dfs(node, visited):
            visited.add(node)
            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb, visited)
            
            return len(visited)
        
        ans = 0
        for i in range(len(bombs)):
            node = (bombs[i][0],bombs[i][1])
            ans = max(ans, dfs(node, set()))
        
        bombs.sort()
        for i in range(1, len(bombs)):
            if bombs[i] == bombs[i-1]:
                ans += 1
        return ans