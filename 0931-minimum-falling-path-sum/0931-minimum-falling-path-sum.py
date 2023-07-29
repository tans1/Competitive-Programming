class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        n,m = len(matrix), len(matrix[0])
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if (0<=i+1<n and 0<=j<m) or (0<=i+1<n and 0<=j-1<m) or (0<=i+1<n and 0<=j+1<m):
                mn = float('inf')
                if (0<=i+1<n and 0<=j<m):
                    mn = min(mn,matrix[i][j] + dfs(i+1,j))
                    
                if (0<=i+1<n and 0<=j-1<m):
                    mn = min(mn,matrix[i][j] + dfs(i+1,j-1))
                    
                if (0<=i+1<n and 0<=j+1<m):
                    mn = min(mn,matrix[i][j] + dfs(i+1,j+1))
                
                memo[(i,j)] = mn
            else:
                memo[(i,j)] = matrix[i][j]
            return memo[(i,j)]
                
            
        ans = float('inf')
        for j in range(len(matrix[0])):
            ans = min(ans,dfs(0,j))
        return ans
            # print(memo)