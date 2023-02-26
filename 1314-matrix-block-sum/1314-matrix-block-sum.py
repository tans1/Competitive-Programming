class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(1,n):
                mat[i][j] += mat[i][j-1]
        
        for i in range(1,m):
            for j in range(n):
                mat[i][j] += mat[i-1][j]
        
        for i in range(m):
            for j in range(n):
                if i - k < 0:
                    t = 0
                else:
                    t = i - k
                    
                if i + k >= m:
                    b = m-1
                else:
                    b = i + k
                
                if j + k >= n:
                    r = n-1
                else:
                    r = j + k
                if j-k < 0:
                    l = 0
                else:
                    l = j - k
                
                
                
                bot = mat[b][r]
                if t - 1 >= 0 and l-1 >= 0:
                    tpl = mat[t-1][l-1]
                else:
                    tpl = 0
                
                if l -1 >= 0:
                    left = mat[b][l-1]
                else:
                    left = 0
                
                if t - 1 >= 0:
                    topr = mat[t-1][r]
                else:
                    topr = 0
                ans[i][j] = bot + tpl - left - topr
        return ans

