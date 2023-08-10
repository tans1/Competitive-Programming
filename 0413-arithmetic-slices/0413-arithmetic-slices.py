class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            for j in range(i+2,len(nums)):
                if (nums[j] - nums[j-1]) == (nums[j-1] - nums[j-2]):
                    ans += 1
                else:
                    break
        return ans
                    