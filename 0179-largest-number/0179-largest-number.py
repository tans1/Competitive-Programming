class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0 : return '0'
        nums = [str(i) for i in nums]
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[i] , nums[j] = nums[j], nums[i]
        return ''.join(nums)