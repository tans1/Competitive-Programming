class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        
        for a,b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i) 
        
        pre = defaultdict(set)
        while q:
            nd = q.popleft()
            for nb in graph[nd]:
                pre[nb].add(nd)
                pre[nb] = pre[nb].union(pre[nd])
                indegree[nb] -= 1
                
                if indegree[nb] == 0:
                    q.append(nb)

        ans = []
        for u,v in queries:
            st = set()
            st.add(u)
            if len(st.intersection(pre[v])) > 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            