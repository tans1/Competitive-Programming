class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            ml = helper(x,n//2)
            
            if n % 2 == 0:
                return ml * ml
            else:
                return x * ml * ml


            
        
        
        if n % 2 == 0:
            if n >= 0:
                return helper(x,n//2) * helper(x,n//2)
            else:
                return 1 / (helper(x,abs(n)//2) * helper(x,abs(n)//2))
        else:
            if n >= 0:
                return x * helper(x,n//2) * helper(x,n//2)
            else:
                return 1 / (x * helper(x,abs(n)//2) * helper(x,abs(n)//2))
