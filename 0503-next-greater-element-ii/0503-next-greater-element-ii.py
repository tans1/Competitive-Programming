class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        n = len(nums)
        
        mono_stack = []
        for i in range(2 * n - 1):
            v = nums[i % n]
            while mono_stack and mono_stack[-1][1] < v:
                j,nm = mono_stack.pop()
                
                res[j % len(res) ] = v
            mono_stack.append([i,v])
        return res
            