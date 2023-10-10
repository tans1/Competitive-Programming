class Solution:
    def longestPrefix(self, s: str) -> str:
        lsp = [0 for _ in range(len(s))]
        i , j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                lsp[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lsp[i-1]
        ans = ""
        for i in range(lsp[-1]):
            ans += s[i]
        
        return ans
        