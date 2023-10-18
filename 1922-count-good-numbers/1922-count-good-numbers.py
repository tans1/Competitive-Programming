class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 5
        odd = n // 2
        even = odd + (n- odd*2)
        return ((pow(4,odd,mod))*(pow(5,even, mod))) % mod