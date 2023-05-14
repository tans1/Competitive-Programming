class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [0 for _ in range(n)]

        def dfs(nd, visited):
            nonlocal ans
            dct = defaultdict(int)
            dct[labels[nd]] += 1
            
            visited.add(nd)
            for nb in graph[nd]:
                if nb not in visited:
                    temp = dfs(nb, visited)
                
                    for k,v in temp.items():
                        dct[k] += v
            
            ans[nd] = dct[labels[nd]]
            return dct
        
        dfs(0, set())
        return ans