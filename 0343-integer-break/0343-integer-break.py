class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,i):
                x = max(dp[i - j], i-j)
                y = max(j, dp[j])
                # x + y = i
                dp[i] = max(dp[i],x*y)
        
        return dp[-1]