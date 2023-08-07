class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = {nums[i] : set([nums[i]]) for i in range(len(nums))}
        
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i] % nums[j] == 0:
                    if len(ans[nums[i]]) < len(ans[nums[j]]) + 1:
                        
                        ans[nums[i]] = ans[nums[j]].copy()
                        
                        ans[nums[i]].add(nums[i])
        sortd = sorted(ans.items(), key=lambda x: -len(x[1]))
        
        return list(sortd[0][1])