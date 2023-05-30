class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt = 0
        
        @lru_cache(maxsize=None)
        def bct(i,sm):
            if i == len(nums) and sm == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            return bct(i+1,sm + nums[i]) + bct(i+1,sm - nums[i])
        
        return bct(0,0)
