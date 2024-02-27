class Solution:
    def climbStairs(self, n: int) -> int:
        # top down
        memo = {}
        def dp(n):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return n
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        return dp(n)
        
#         Time complexity = O(N), and Space O(N)
    
        # bottum up
        if n <= 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
            