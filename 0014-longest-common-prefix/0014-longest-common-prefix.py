class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ''
        res = ''
        strs.sort()
        for j in range(len(strs[0])):
            if strs[0][j] == strs[-1][j]:
                res += strs[0][j]
            else: 
                break
        return res
