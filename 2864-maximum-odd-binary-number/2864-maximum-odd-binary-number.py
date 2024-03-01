class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_one = 0
        num_zero = 0
        for i in range(len(s)):
            if s[i] == "1":
                num_one += 1
            else:
                num_zero += 1
        if num_one == 0:
            return s
        s = "1"*(num_one-1) + "0"*(num_zero) + "1"
        return s
    
        
