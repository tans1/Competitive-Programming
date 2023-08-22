class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1 for _ in range(len(pairs))]
        pairs.sort()
        
        for i in range(len(pairs)):
            temp = 0
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    temp = dp[j]
            
            dp[i] = max(dp[i], temp+1)
        
        return max(dp)