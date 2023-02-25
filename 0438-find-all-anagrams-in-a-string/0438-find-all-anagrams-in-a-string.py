class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        n = len(p)
        cp = Counter(p)
        res = []
        sp = Counter(s[:n-1])
        for i in range(len(s)-n+1):
            if s[i+n-1] not in sp:
                sp[s[i+n-1]] = 0
            sp[s[i+n-1]] += 1
            
            if sp == cp:
                res.append(i)
            sp[s[i]] -= 1
            if sp[s[i]] == 0:
                del sp[s[i]]
        return res