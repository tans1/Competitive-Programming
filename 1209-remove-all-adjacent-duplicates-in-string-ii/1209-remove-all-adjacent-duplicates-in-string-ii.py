class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char,1])
            else:
                if stack[-1][0] == char:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
        ans = ""
        for char,num in stack:
            ans += char*num
        return ans
                    
        