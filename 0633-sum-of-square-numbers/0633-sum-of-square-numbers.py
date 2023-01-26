class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1 or c == 0 : return True
        ls = [i for i in range( int(c ** 0.5) + 1)]
        i = 0
        j = len(ls)-1
        
        while i <= j:
            if (ls[i] ** 2) + (ls[j] ** 2) == c:
                return True
            else:
                if (ls[i] ** 2) + (ls[j] ** 2) < c:
                    i += 1
                else:
                    j -= 1
        return False