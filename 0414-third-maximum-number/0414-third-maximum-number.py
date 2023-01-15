class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dest = list(Counter(nums).keys())
        dest.sort()
        dest.reverse()
        
        return dest[2] if len(dest) > 2 else dest[0]
        