class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i - 1 >= 0 :
                        dp[i][j] += dp[i-1][j]
                    if j-1 >= 0 :
                        dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]