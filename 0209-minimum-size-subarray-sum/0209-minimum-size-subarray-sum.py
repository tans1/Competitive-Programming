class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = summ = 0
        minn = 1000000
        while j < len(nums):  #we use variable size window
            summ += nums[j]
            while summ >= target: #if the sum of the nums in the window is greator than target we reduce it continuosly
                minn = min(minn,j-i+1)  
                summ -= nums[i]
                i += 1
            j += 1
        
        return 0 if minn == 1000000 else minn