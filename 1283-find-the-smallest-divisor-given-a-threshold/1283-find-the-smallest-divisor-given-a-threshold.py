class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        possible = [i for i in range(1, max(nums) + 1)]
        res = float('inf')
        
        l , r = 0, len(possible)-1
        
        while l <= r:
            md = (l + r) // 2
        
            x= possible[md]
            temp = 0
            for n in nums:
                if n % x == 0:
                    temp += (n // x)
                else:
                    temp += (n // x) + 1
            
            if temp <= threshold:
                res = min(res,x)
                r = md - 1
            else:
                l = md + 1
        
        return res