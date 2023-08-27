class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(i,j):
            if i == j:
                return s[i]
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == s[j] and i + 1 == j:
                return s[i:j+1]
            
            if s[i] == s[j] and i + 1 != j:
                return s[i] + dfs(i+1,j-1) + s[j]
            else:
                temp1 = dfs(i,j-1)
                temp2 = dfs(i+1,j)
                
                if len(temp1) > len(temp2):
                    memo[(i,j)] = temp1
                else:
                    memo[(i,j)] = temp2
                
                return memo[(i,j)]
        
        return len(dfs(0,len(s)-1))
                