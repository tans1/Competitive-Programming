class Solution:
    def minSteps(self, n: int) -> int:
        i = 2
        temp = []
        while n >= i:
            if n % i == 0:
                temp.append(i)
                n = n // i
            else:
                i += 1
        return sum(temp)