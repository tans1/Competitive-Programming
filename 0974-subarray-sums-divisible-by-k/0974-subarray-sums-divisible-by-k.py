class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        
        pre = 0 # prefix sum
        ans = 0
        for i in range(len(nums)):
            pre += nums[i]
            rmd = pre % k 
            
            ans += dct.get(rmd,0) #had we already seen the remainder ? 
            dct[rmd] = dct.get(rmd, 0) + 1
        return ans

            