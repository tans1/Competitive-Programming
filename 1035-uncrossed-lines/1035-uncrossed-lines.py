class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        n , m = len(nums1) , len(nums2)
        def dfs(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = 0
            
            for k in range(j,m):
                if i < n and nums1[i] == nums2[k]:
                    memo[(i,j)] = max(memo[(i,j)], 1 + dfs(i+1,k+1))
                    
            memo[(i,j)] = max(memo[(i,j)], dfs(i+1, j))
            return memo[(i,j)]
        
        return dfs(0,0)
            
            