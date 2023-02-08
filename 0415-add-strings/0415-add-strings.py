class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x , y = [] , []
        
        for i in range(len(num1)):
            x.append(ord(num1[i]) - 48)
        for i in range(len(num2)):
            y.append(ord(num2[i]) - 48)
        
        p1 , temp1 = 0 , 0
        for i in range(len(x)-1, -1,-1):
            temp1 += x[i] * (10 ** p1)
            p1 += 1
            
        p2 , temp2 = 0 , 0
        for i in range(len(y)-1, -1,-1):
            temp2 += y[i] * (10 ** p2)
            p2 += 1
        return str(temp1 + temp2)