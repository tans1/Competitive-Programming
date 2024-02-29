class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, prices[i]-mn)
            mn = min(prices[i], mn)
            
        return ans