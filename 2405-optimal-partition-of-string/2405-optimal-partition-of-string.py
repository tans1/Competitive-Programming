class Solution:
    def partitionString(self, s: str) -> int:
        dct = {}
        ans = 0
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            
            else:
                ans += 1
                dct.clear()
                dct[s[i]] = 1
                
        if len(dct) > 0:
            ans += 1
        return ans