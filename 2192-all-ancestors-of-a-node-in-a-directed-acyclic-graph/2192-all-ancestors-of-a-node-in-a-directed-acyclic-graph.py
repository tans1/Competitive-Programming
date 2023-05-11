class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestor = defaultdict(set)
        indegree = [0 for _ in range(n)]
        graph = defaultdict(list)
        
        for f,t in edges:
            graph[f].append(t)
            indegree[t] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
            
        while q:
            nd = q.popleft()
            for nb in graph[nd]:
                
                # temp = ancestor[nd]
                ancestor[nb].add(nd)
                ancestor[nb] = ancestor[nb].union(ancestor[nd])
#                 if temp:
#                     ancestor[nb] += temp + [nd]
#                 else:
#                     ancestor[nb].append(nd)
                    
                indegree[nb] -= 1
                
                if indegree[nb] == 0:
                    q.append(nb)
        

        ans = []
        for i in range(n):
            if not ancestor[i]:
                ans.append([])
            else:
                temp = list(ancestor[i])
                temp.sort()
                ans.append(temp)
        
        return ans