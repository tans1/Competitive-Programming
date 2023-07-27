class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = values[0]
        ans = 0
        
        
        for j in range(1,len(values)):
            cur = (values[j] - j) + dp
            ans = max(ans, cur)
            
            dp = max(dp, values[j] + j)
        
        return ans