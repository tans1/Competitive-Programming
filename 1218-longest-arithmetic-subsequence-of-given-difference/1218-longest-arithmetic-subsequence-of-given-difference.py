class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        needdct = defaultdict(int)
        lengthdct = defaultdict(int)
        
        ans = 0
        for i,n in enumerate(arr):
            if (needdct[n] == 1):
                lengthdct[n] = lengthdct[n-difference] + 1
            else:
                lengthdct[n] = 1
            
            ans = max(ans, lengthdct[n])
            needdct[n + difference] = 1
        
        return ans
            
        