class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        
        def dfs(i,j):
            if i == j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            if s[i] == s[j] and i + 1 == j:
                return 2
            if s[i] == s[j] and i + 1 != j:
                return dfs(i+1,j-1) + 2
            
            else:
                temp1 = dfs(i+1,j)
                temp2 = dfs(i,j-1)

            memo[(i,j)] = max(temp1,temp2)
            return memo[(i,j)]
        
        return len(s) - dfs(0,len(s)-1)