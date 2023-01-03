class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = len(strs[0])
        wrd_col = list(zip(*strs))
        
        cnt = 0
        for i in range(l):
            wrd = list(wrd_col[i])
            
            sorted_char = sorted(wrd)
            
            cnt += sorted_char != wrd
        
        return cnt