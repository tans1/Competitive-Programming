class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        def fib(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            temp = fib(n-1) + fib(n-2) + fib(n-3)
            memo[n] = temp
            return temp
        
        return fib(n)