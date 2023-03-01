class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # easily find the most maximum and its next maximum, 3  & 2
        temp = []
        stack = []
        n = len(nums)
        for i in range(n-1,-1,-1):
            if temp and nums[i] < temp[-1]:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    temp.append(stack.pop())
            stack.append(nums[i])
        return False