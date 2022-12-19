class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            pal = 0
            n = x
            while x > 0:
                end = x % 10  # to get the number at the end of x
                pal = pal * 10 + end
                x = x // 10  # reduce x by removing the last degit
            return n == pal
        else:
            return False

	