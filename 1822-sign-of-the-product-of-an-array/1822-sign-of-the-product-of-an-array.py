class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ng = len(list(filter(lambda x: x < 0, nums)))
        zr = 0 in nums
        
        if zr:
            return 0
        if ng % 2 == 0:
            return 1
        return -1