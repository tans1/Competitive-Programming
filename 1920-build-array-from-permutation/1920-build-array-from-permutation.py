class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] *len(nums)
        print(res)
        
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        return res