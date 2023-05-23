class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = []
        for k in indegree:
            if indegree[k] == 1:
                q.append(k)

        visited = set()
        ans = []
        while q:
            nd = q.pop()
            visited.add(nd)
            ans.append(nd)
            for nb in graph[nd]:
                indegree[nb] -= 1
                if nb not in visited and indegree[nb] == 1:
                    q.append(nb)

        return ans
                