class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0 for _ in range(n+1)]
        if n == 0:
            return 0
        memo[1] = 1
        
        def rec(i):
            nonlocal memo
            if memo[i] != 0:
                return memo[i]
            
            if i <= 1:
                # memo[i] = i
                return i
            
            ith = memo[i // 2]
            memo[i] = ith
            memo[i+1] = ith + memo[(i//2) + 1]
            return memo[i]
        
        for i in range(n):
            rec(i)
        return max(memo)
            