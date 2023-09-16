class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if len(heights) == len(heights[0]) == 1:
            return 0
        efforts = []
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                for l,k in directions:
                    if 0 <= i+l < len(heights) and 0 <= j+k < len(heights[0]):
                        effort = abs(heights[i+l][j+k] - heights[i][j])
                        efforts.append(effort)
        efforts.sort()
        def dfs(i,j,cur,visited):
            if i == len(heights)-1 and j == len(heights[0])-1:
                return True
            
            visited.add((i,j))
            for l,k in directions:
                if 0 <= i+l < len(heights) and 0 <= j+k < len(heights[0]) and (i+l,j+k) not in visited:
                    effort = abs(heights[i+l][j+k] - heights[i][j])
                    if effort <= cur:
                        if dfs(i+l,j+k,cur,visited):
                            return True
            return False
        
        i = 0
        j = len(efforts) - 1

        while i < j:
            mid = (i + j) // 2
            temp = dfs(0, 0, efforts[mid], set())

            if temp:
                j = mid
            else:
                i = mid + 1

        return efforts[i]
            
            
            