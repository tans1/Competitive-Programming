class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # using buttom up knapsack
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 0
                else:
                    if coins[i] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
                        
                        
        if dp[-1][-1] != float("inf"):
            return dp[-1][-1]
        return -1