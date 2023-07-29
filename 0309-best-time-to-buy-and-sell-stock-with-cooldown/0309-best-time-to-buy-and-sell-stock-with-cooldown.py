class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i,can_buy,dp):
            if i >= len(prices):
                return 0
            
            if dp[i][can_buy] != -1:
                return dp[i][can_buy]
            
            if can_buy:
                dp[i][can_buy] = max(-prices[i] + dfs(i+1,not can_buy,dp), dfs(i+1,can_buy,dp))
                return dp[i][can_buy]
            
            else:
                dp[i][can_buy] = max(prices[i] + dfs(i+2,not can_buy,dp), dfs(i+1,can_buy,dp))
                return dp[i][can_buy]
        
        
        return dfs(0,1,[[-1,-1] for _ in range(len(prices) + 2)])
        