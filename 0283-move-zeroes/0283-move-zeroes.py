class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                j = i
        
        
        
#         k = 0
#         for i in nums:
#             if i == 0: k += 1
#         i = 0
#         while i < len(nums) and k > 0:
#             if nums[i] == 0:
#                 nums.pop(i)
#                 k -= 1
#                 nums.append(0)
#             else:
#                 i += 1
        
        
        