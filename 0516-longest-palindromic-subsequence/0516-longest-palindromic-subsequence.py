class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i,j):
            nonlocal memo
            if (i,j) in memo:
                return memo[(i,j)]
            if i > j:
                return ""
            if i == j:
                memo[(i,j)] = s[i]
                return memo[(i,j)]
            if s[i] == s[j]:
                memo[(i,j)] = s[i] + dfs(i+1,j-1) + s[j]
                return memo[(i,j)]
            else:
                option1 = dfs(i,j-1)
                option2 = dfs(i+1,j)
                
                if len(option1) > len(option2):
                    memo[(i,j)] = option1
                else:
                    memo[(i,j)] = option2
                
                return memo[(i,j)]
        
        return len(dfs(0,len(s)-1))
            