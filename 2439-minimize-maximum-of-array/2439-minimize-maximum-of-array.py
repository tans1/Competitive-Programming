class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        prefix_sum = nums[0]

        for i,v in enumerate(nums[1:]):
            prefix_sum += v
            result = max(result, math.ceil(prefix_sum / (i + 2)))
        return result