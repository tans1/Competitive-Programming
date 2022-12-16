class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        top = 0
        maxx = 0
        while top + 3 <= len(grid):
            left = 0
            while left + 3 <= len(grid[0]):
                hourSum = grid[top][left] + grid[top][left+1] + grid[top][left+2] + grid[top+1][left+1] + grid[top+2][left] + grid[top+2][left+1] + grid[top+2][left+2]
                maxx = max(maxx, hourSum)
                left += 1
            top += 1
        return maxx