class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        fact = 64
        temp = list(columnTitle)
        temp.reverse()
        
        ans = 0
        for i in range(len(temp)):
            ans += (26 ** i) * (ord(temp[i]) - fact)
        
        return ans