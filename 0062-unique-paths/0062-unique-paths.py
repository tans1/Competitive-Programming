class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize=None)
        
        def bct(i,j):
            
            if i == m -1 and j == n-1:
                return 1
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            return bct(i,j+1) + bct(i+1,j)
        
        return bct(0,0)