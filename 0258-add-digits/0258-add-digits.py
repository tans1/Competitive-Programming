class Solution:
    def addDigits(self, num: int) -> int:
        temp = str(num)
        while len(temp) > 1:
            x = 0
            for i in range(len(temp)):
                x += int(temp[i])
            temp = str(x)
        return int(temp)