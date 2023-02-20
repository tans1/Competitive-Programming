class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dct1 = defaultdict(int)
        dct2 = defaultdict(int)
        
        for i in range(len(s)):
            dct1[s[i]] += 1
            dct2[t[i]] += 1
            
        cnt = 0
        for k,v in dct1.items():
            if v > dct2[k]:
                cnt += v - dct2[k]
        return cnt