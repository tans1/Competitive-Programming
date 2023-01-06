class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        res = [0] * len(nums)
        i = 0
        j = 1
        k = 0
        while i < len(nums) and j < len(nums):
            if k < len(pos):
                res[i] = pos[k]
                res[j] = neg[k]
                k += 1
            i += 2
            j += 2
        return res
        