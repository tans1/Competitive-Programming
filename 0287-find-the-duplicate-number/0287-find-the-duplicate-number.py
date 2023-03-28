class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = [0 for i in range(len(nums) + 2)]
        
        for n in nums:
            temp[n] += 1
        
        for i in range(len(temp)):
            if temp[i] > 1:
                return i