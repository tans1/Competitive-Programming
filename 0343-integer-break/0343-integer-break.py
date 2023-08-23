class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        
        for i in range(2,n+1):
            temp = 0
            for j in range(i-1, -1,-1):
                pr = j * max(i-j, dp[i-j])
                temp = max(pr, temp)
            dp[i] = temp
        
        return dp[-1]