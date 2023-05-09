class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            return False
        return True