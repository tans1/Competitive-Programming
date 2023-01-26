class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = '_'
        i = 0
        while i < len(nums):
            if nums[i] == '_':
                del nums[i]
            else:
                i += 1
        return len(nums)