class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        
        def helper(l,r):
            md = (l+r) // 2
            
            if l > r:
                return l-1
            else:
                if md ** 2 == x:
                    return md
                elif md **2 < x:
                    l = md + 1
                else:
                    r = md - 1

                return helper(l,r)
        
        return helper(1,x)
                
