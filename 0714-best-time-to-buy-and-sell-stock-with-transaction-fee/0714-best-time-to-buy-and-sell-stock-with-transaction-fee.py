class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        buyProfit = -prices[0]
        sellProfit = 0
        
        for i in range(1, n):
            tmp = buyProfit
            
            buyProfit = max(buyProfit, sellProfit - prices[i])
            sellProfit = max(sellProfit, tmp + prices[i] - fee)
        
        return sellProfit