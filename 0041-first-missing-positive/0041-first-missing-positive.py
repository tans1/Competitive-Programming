class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] != ans:
                    return ans
                if i < len(nums)-1 and nums[i] != nums[i+1]:
                    ans += 1
                elif i == len(nums) - 1:
                    ans += 1
                    
                    
        return ans
        
                