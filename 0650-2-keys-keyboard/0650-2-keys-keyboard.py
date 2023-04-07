class Solution:
    def minSteps(self, n: int) -> int:
        i = 2
        ans = 0
        while n >= i:
            if n % i == 0:
                ans += i
                n = n // i
            else:
                i += 1
        return ans