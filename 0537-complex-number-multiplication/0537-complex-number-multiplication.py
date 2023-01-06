class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x,y = num1.split('+')
        a,b = num2.split('+')
        # num1 = x + yi
        x = int(x[1:]) * -1 if x[0] == '-' else int(x[0:])
        y = int(y[1:-1]) * -1 if y[0] == '-' else int(y[0:-1])

        # num2 = a + bi
        a = int(a[1:]) * -1 if a[0] == '-' else int(a[0:])
        b = int(b[1:-1]) * -1 if b[0] == '-' else int(b[0:-1])
        
        return f"{(a*x) - (b*y)}+{(b*x)+(a*y)}i"
        