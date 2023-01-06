class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dct = {nums[i]:i for i in range(len(nums))}
        
        for operation in operations:
            j = dct[operation[0]]
            nums[j] = operation[1]
            
            del dct[operation[0]]
            
            dct[operation[1]] = j
        return nums