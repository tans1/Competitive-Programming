class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        @lru_cache(maxsize = None)
        def backtracking(i,cur):
            nonlocal ans
            if i >= len(nums):
                ans = max(ans,cur)
            
            for j in range(i,len(nums)):
                backtracking(j+2,cur + nums[j])
        
        backtracking(0,0)
        return ans
        
        
        # dp = [0,0]
        # i = 0
        # while i < len(nums):
        #     dp[0] += nums[i]
        #     if i + 1 < len(nums):
        #         dp[1] += nums[i+1]
        #     i += 2
        # return max(dp)