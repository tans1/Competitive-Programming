class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        total = int((n*(n+1)) / 2)
        for i in nums:
            summ += i
        return total - summ