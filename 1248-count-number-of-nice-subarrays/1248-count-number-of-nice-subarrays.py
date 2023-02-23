class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        ans = 0
        psb = 0
        while i < len(nums) and j < len(nums):
            if nums[j] % 2 == 1:
                k -= 1
                psb = 0
            if k == 0:
                while k == 0:
                    if nums[i] % 2 == 1:
                        k += 1
                    psb += 1
                    i += 1
            j += 1
            ans += psb
        return ans
    
    
    

            
    

            
                