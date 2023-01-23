class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for j in range(len(nums)):
            counter =0
            for i in range(0, len(nums)):
                if nums[i] < nums[j]:
                    counter += 1
            output.append(counter)
            
        return output