class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0 for _ in range(len(scores))]
        
        combined = []
        for i in range(len(scores)):
            combined.append((ages[i], scores[i]))
        
        combined = sorted(combined,key = lambda x: (x[0],x[1]))
        for i in range(len(combined)-1,-1,-1):
            for j in range(i,len(combined)):
                if combined[i][1] <= combined[j][1]:
                    dp[i] = max(dp[i],dp[j] + combined[i][1] )
        return max(dp)
            