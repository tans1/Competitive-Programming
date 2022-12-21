class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i + 2] > nums[i+1] and  nums[i+1] + nums[i+2] > nums[i] :
                maxx = max(maxx, sum(nums[i:i+3]))
        return maxx
        