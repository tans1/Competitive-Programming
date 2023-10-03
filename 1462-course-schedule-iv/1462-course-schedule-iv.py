class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # USING FROYD-WARSHALL ALGORITHM
        dist = [[float("inf")] * numCourses for _ in range(numCourses)]
        for u,v in prerequisites:
            dist[u][v] = 1
        
        
        for i in range(numCourses):
            dist[i][i] = 0
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = []
        for u,v in queries:
            ans.append(dist[u][v] != float("inf"))
        return ans
            
            