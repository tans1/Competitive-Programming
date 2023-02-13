class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        
        while i < len(s) and j < len(t):
            if t[j] != s[i]:
                i += 1
            else:
                i += 1
                j += 1
        return len(t) - j
        