class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = n
        r = 1
        ans = 0
        
        while l >= r:
            md = (l+r) // 2
            
            if citations[n - md] >= md:
                ans = max(ans,md)
                r = md + 1
            else:
                l = md - 1
        return ans