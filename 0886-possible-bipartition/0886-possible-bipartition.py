class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1 for _ in range(n+1)]
        
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        ans = True

        def dfs(nd, cl,cur):
            visited.add(nd)
            nonlocal ans
            if color[nd] == -1:
                color[nd] = cl
            cur.add(nd)
            for nb in graph[nd]:
                if color[nb] == cl:
                    ans = False
                    return
                if nb not in cur:
                    dfs(nb,not cl, cur)
        
        for i in range(1,n+1):
            if i not in visited:
                dfs(i,0,set())
        return ans
            