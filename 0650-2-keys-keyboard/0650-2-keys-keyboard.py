class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        primeFactorization = []
        p = 2
        while p <= n:
            if n % p == 0:
                n =  n // p
                primeFactorization.append(p)
            else:
                p += 1
        return sum(primeFactorization)