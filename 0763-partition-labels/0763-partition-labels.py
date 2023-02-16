class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dct = {}
        for i in range(len(s)):
            dct[s[i]] = i
        
        i = 0
        j = 0
        temp = 0
        res = []
        
        while i < len(s) and j < len(s):
            if dct[s[j]] > temp:
                temp = dct[s[j]]
            if j == temp:
                res.append(j-i+1)
                i = j+1
                temp = 0
            j += 1
        return res