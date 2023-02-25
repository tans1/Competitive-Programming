class Solution:
    def minimumSum(self, num: int) -> int:
        ls = list(str(num))
        ls.sort()
        num1 = int(ls[0] + ls[-1])
        num2 = int(ls[1] + ls[2])
        
        return num1 + num2