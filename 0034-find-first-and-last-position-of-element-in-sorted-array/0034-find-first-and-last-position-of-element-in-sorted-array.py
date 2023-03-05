class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1: return [-1, -1]
        l = 0
        r = len(nums)-1
        ans = [-1,-1]
        
        while l <= r:
            md = (l+r) // 2
            
            if nums[md] == target:
                break
            elif nums[md] > target:
                r = md - 1
            else:
                l = md + 1
        if nums[md] == target:
            i = md
            while i >= 0 and nums[i] == target:
                i -= 1
            j = md
            while j < len(nums) and nums[j] == target:
                j += 1
            
            ans =  [i +1, j-1]
        return ans