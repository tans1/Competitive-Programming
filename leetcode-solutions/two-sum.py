class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dct:
                return [dct[target - nums[i]], i]
            else:
                dct[nums[i]] = i
        return []
        