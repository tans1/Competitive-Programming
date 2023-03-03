# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def helper(l,r,bad):
            md = (l+r) // 2
            if l > r:
                return bad
            
            if isBadVersion(md):
                bad = md
                r = md-1
            else:
                l = md + 1
            
            return helper(l,r,bad)
        
        return helper(0,n,1)
                

