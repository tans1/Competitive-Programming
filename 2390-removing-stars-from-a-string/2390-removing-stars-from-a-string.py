class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            
            elif s[i] == '*':
                if stack[-1] != '*':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return ''.join(stack)
            