class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles) + 1
        res = float('inf')
        
        while l <= r:
            k = (l+r) // 2
            
            temp = 0
            for n in piles:
                if n % k == 0:
                    temp += (n // k)
                else:
                    temp += (n //k) + 1

            if temp <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res