class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        
        # db bottom-up
        def dp(i,j):
            arr = [nums[i], max(nums[i], nums[i+1])]
            for l in range(i+2,j):
                arr.append( max(arr[-2] + nums[l],arr[-1]) )
            return arr[-1]
        
        return max(dp(0,n-1), dp(1,n))