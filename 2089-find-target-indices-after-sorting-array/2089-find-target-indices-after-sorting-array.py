class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                output.append(i)
            i +=1
        return output