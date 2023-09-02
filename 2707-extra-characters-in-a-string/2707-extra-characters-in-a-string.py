class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {}
        def dfs(i):
            if i >= len(s):
                return 0
            if i in dp:
                return dp[i]
            
            temp = 1 + dfs(i+1)
            for j in range(len(s)):
                if s[i:j+1] in words:
                    temp = min(temp, dfs(j+1))
            dp[i] = temp
            return temp
        
        return dfs(0)