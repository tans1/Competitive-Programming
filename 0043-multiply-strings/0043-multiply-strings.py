class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        list_n1 = [ord(x)-ord('0') for x in num1]
        list_n2 = [ord(x)-ord('0') for x in num2]
        list_n1.reverse()
        list_n2.reverse()
        
        x = 0
        y = 0
        
        for i in range(len(list_n1)):
            x += (list_n1[i] * (10 ** i))
        
        for j in range(len(list_n2)):
            y += (list_n2[j] * (10 ** j))
        
        return str(x * y)
        