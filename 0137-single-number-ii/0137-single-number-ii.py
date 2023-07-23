class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for k,v in freq.items():
            if v == 1:
                return k