class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1 
                l += 1
            res = max(res, r - l + 1)
        return res