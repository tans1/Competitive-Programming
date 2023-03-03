class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0]
        for i in range(n):
            p.append(p[-1] + nums[i])
        
        mnq = []
        ans = n + 1
        for r in range(len(p)):
            while mnq and p[mnq[-1]] >= p[r]:
                mnq.pop()
            
            while mnq and p[r] - p[mnq[0]] >= k:
                ans = min(ans, r - mnq[0])
                mnq.pop(0)
            
            mnq.append(r)
        
        if ans != n+1:
            return ans
        
        return -1