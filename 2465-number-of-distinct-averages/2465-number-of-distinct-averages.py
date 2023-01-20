class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        dstnict = set()
        nums.sort()
        i , j = 0, len(nums)-1
        
        while i < j:
            dstnict.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return len(dstnict)