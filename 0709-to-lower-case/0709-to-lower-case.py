class Solution:
    def toLowerCase(self, s: str) -> str:
        temp = list(s)
        for i in range(len(temp)):
            if 65 <= ord(temp[i]) <= 90:
                temp[i] = chr(ord(temp[i]) + 32)
        return ''.join(temp)