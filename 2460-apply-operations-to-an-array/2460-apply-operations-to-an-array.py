class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        res = []
        for n in nums:
            if n != 0:
                res.append(n)
        x = len(nums) - len(res)
        
        res.extend([0]*x)
        return res