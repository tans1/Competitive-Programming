class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            dif = stones.pop()-stones.pop()
            if dif > 0: stones.append(dif)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            