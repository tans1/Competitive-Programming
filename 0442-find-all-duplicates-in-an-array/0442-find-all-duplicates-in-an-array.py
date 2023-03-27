class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dublicate = [0 for i in range(len(nums) + 1)]
        
        for n in nums:
            dublicate[n] += 1
        ans = []
        
        for i in range(len(dublicate)):
            if dublicate[i] > 1:
                ans.append(i)
        
        return ans