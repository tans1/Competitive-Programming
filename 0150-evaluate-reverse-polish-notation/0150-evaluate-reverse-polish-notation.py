class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                if len(stack) >= 2:
                    a = int(stack.pop())
                    b = int(stack.pop())

                    if i == '+':
                        d = a + b
                    elif i == '-':
                        d = b - a
                    elif i == '*':
                        d = a * b
                    else:
                        d = int(b / a)
                    stack.append(d)
        return stack[0]
            