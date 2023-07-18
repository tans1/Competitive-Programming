class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [i for i in range(len(quiet))]
        indegree = [0 for _ in range(len(quiet))]
        graph = defaultdict(list)
        
        for u,v in richer:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur_node = q.popleft()
            for nb in graph[cur_node]:
                indegree[nb] -= 1
                
                if indegree[nb] == 0:
                    q.append(nb)
                
                if quiet[ans[cur_node]] < quiet[ans[nb]]:
                    ans[nb] = ans[cur_node]
        return ans