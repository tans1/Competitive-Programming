class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        ans = 0
        i = 0
        j = len(nums) -1 
        
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += 2**(j-i)
                i += 1
            else:
                j -= 1
                
        return ans % mod