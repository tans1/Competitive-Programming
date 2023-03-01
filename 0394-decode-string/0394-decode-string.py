class Solution:
    def decodeString(self, s: str) -> str:
        ml = [] #to track the number of multiplier
        stack = [] # to store the letters 
        n = len(s)
        
        nm = "" #number
        for i in range(n):
            if s[i] == "]":
                
                temp = ""
                while stack and stack[-1] != "[":
                    temp += stack.pop()
                
                stack.pop()
                temp1 = temp[::-1]
                stack += list(temp1 * ml[-1])
                ml.pop()
                
            elif s[i] in "1234567890":
                nm += s[i]
            else:
                if s[i] == "[":
                    ml.append(int(nm))
                    nm = ""
                stack.append(s[i])
        
        return "".join(stack)