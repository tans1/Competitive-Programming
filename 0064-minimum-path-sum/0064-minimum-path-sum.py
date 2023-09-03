class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i - 1 < 0 or j - 1 < 0:
                    if i - 1 < 0 and j - 1 >= 0:
                        grid[i][j] += grid[i][j-1]
                        
                    elif i - 1 >= 0 and j - 1 < 0:
                        grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
                
        
        
        
        
        
#         self.ans = float('inf')

        
#         def backtracking(i,j,sm):
            
#             if i >= len(grid)-1 and j >= len(grid[0]):
#                 self.ans = min(self.ans, sm)
#                 return
            
#             if i >= len(grid) or j >= len(grid[0]):
#                 return
            
            
#             backtracking(i+1,j,sm + grid[i][j])
#             backtracking(i,j+1,sm + grid[i][j])
        
        
#         backtracking(0,0,0)
        
#         return self.ans
            
        
        
        
        
        
        
        
        
        
        
        
        