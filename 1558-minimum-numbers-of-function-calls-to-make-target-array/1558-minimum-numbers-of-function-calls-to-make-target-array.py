class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    ans += 1
                    nums[i] -= 1
            if any(nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                ans += 1
        
        return ans