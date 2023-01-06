class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dct = {nums[i]:i for i in range(len(nums))}
        
        for op in operations:
            j = dct[op[0]]
            nums[j] = op[1]
            
            del dct[op[0]]
            
            dct[op[1]] = j
        return nums