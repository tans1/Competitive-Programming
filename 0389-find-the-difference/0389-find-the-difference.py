class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        i = j = 0
        res = []
        while i < len(s) and j < len(t):
            if a[i] != b[j]:
                res.append(b[j])
                j += 1
            else:
                i += 1
                j += 1     
        if j != len(t):
            res.extend(b[j])
        return ''.join(res)
        
        
        #a = set()
        #b = set()
        #res = ''
        #for i in range(len(s)):
        #   a.add(s[i])
        #for j in range(len(t)):
         #   b.add(t[j])
        #for i in b.difference(a):
         #   res += i
        #return res
        