class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            md = (l + r) // 2
            if nums[md] == target:
                return md
            
            if nums[md] >= nums[l]: # left is ascending ?
                if nums[l] <= target <= nums[md]: # target at left side?
                    r = md - 1
                else:
                    l = md + 1
            else:
                if nums[md] <= target <= nums[r]:  # target at right side?
                    l = md + 1
                else:
                    r = md - 1

        return -1

