class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 != 0:
                j += 1
            if i < len(nums) and j < len(nums) and i < j and nums[i] % 2 != 0 and nums[j] % 2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            else:
                j += 1
        return nums