class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        dct = defaultdict(int)
        i = 0
        
        for j in range(len(s)):    
            dct[s[j]] += 1
            
            while len(dct) == 3:
                res += (len(s) - j)       
                dct[s[i]] -= 1
                if dct[s[i]] == 0:
                    del dct[s[i]]
                i += 1
        return res