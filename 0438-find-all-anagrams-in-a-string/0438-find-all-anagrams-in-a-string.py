class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:      
        res = []
        fr = Counter(p)
        for i in range(len(s)-len(p) + 1):
            wnd = s[i:i+len(p)]
        
            if Counter(wnd) == fr:
                res.append(i)
        return res