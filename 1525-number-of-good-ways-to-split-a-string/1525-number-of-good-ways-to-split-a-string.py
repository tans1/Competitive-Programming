class Solution:
    def numSplits(self, s: str) -> int:
        frq = Counter(s)
        unq = set()
        ans = 0
        for i in range(len(s)):
            frq[s[i]] -= 1
            if frq[s[i]] == 0:
                del frq[s[i]]
            unq.add(s[i])
            ans += len(frq) == len(unq)
        return ans
            
        