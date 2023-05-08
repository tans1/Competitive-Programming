class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        self.cycle = False
        ans = []
        def dfs(nd): 
            color[nd] = 1
            
            for nb in graph[nd]:
                if color[nb] == 1:
                    self.cycle = True
                    return 
                
                if color[nb] == 0:
                    dfs(nb)
            ans.append(nd)
            color[nd] = 2
        
        for i in range(len(color)):
            if color[i] == 0:
                dfs(i)
                
        if len(ans) != numCourses or self.cycle == True:
            return []
        return ans[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = defaultdict(list)
#         incoming = [0] * numCourses
        
#         for a,b in prerequisites:
#             graph[b].append(a)
#             incoming[a] += 1
        
#         todo = deque([])
        
#         for i , count in enumerate(incoming):
#             if count == 0:
#                 todo.append(i)
        
#         ans = []
#         while todo:
#             nd = todo.popleft()
#             ans.append(nd)
#             for nb in graph[nd]:
#                 incoming[nb] -= 1
                
#                 if incoming[nb] == 0:
#                     todo.append(nb)
        
#         if len(ans) != numCourses:
#             return []
#         return ans