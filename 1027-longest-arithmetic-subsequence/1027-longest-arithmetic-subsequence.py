class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                diff = nums[j] - nums[i]
                
                if (i,diff) not in dp:
                    dp[(j,diff)] = 2
                else:
                    dp[(j,diff)] = dp[(i,diff)] + 1
    
        return max(dp.values())