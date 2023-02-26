class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        temp = []
        for i in range(len(s)):
            temp.append(abs(ord(s[i]) - ord(t[i])))
        res = 0
        i = 0
        pr = 0
        for j in range(len(temp)):  #simply it is about finding longest sub array with sum <= maxCost
            pr += temp[j]
            while pr > maxCost and i <= j:
                pr -= temp[i]
                i += 1
            
            res = max(res, j - i + 1)
        return res
            