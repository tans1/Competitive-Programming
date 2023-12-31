class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if i == 0 and j == 0:
              continue
            
            top = float('inf')
            left = float('inf')

            if 0 <= i - 1 < len(grid):
              top = grid[i-1][j]
            if 0 <= j - 1 < len(grid[0]):
              left = grid[i][j-1]
            
            grid[i][j] = min(top,left) + grid[i][j]
          

        return grid[-1][-1]