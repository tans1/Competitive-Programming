class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        target = n // 3
        ans = []
        i = 0
        while i < n:
            j = i
            while j+1 < n and nums[j] == nums[j+1]:
                j += 1
            if (j-i+1) > target:
                ans.append(nums[i])
            i = j + 1
        return ans
            
        