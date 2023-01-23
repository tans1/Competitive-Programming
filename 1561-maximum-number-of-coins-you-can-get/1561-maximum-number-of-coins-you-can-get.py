class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i = 0
        j = len(piles)-1
        me = 0
        piles.sort()
        while i < j-1:
            me += piles[j-1]
            i += 1
            j -= 2
        return me