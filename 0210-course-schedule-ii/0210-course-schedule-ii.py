class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
        
        todo = deque([])
        
        for i , count in enumerate(incoming):
            if count == 0:
                todo.append(i)
        
        ans = []
        while todo:
            nd = todo.popleft()
            ans.append(nd)
            for nb in graph[nd]:
                incoming[nb] -= 1
                
                if incoming[nb] == 0:
                    todo.append(nb)
        
        if len(ans) != numCourses:
            return []
        return ans