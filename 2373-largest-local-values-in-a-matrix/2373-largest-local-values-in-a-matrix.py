class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matLocal = [[0 for _ in range(len(grid[0]) - 2)] for _ in range(len(grid) - 2)]
        
        def helper(i,j):
            maxx = float('-inf')
            
            for k in range(3):
                for l in range(3):
                    maxx = max(maxx,grid[i+k][j+l])
            return maxx
            
        for i in range(len(matLocal)):
            for j in range(len(matLocal[0])):
                matLocal[i][j] = helper(i,j)
        
        return matLocal
                