class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for k,v in freq.items():
            comb = (v * (v-1)) // 2
            res += comb
        return res