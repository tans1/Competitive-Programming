class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        sm = sum(nums[:k-1])
        maxx = float('-inf')
        
        while r < len(nums):
            sm += nums[r]
            maxx=max(maxx, sm)
            sm -= nums[l]
            
            l += 1
            r += 1
        return maxx / k
            
            