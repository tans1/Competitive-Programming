class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        res = []
        for i in range(len(nums)):
            cnt = 0
            while stack and stack[-1][0] <= nums[i]:                
                cnt = max(cnt, stack[-1][1])
                stack.pop()
                
            if stack:
                cnt += 1
            else:
                cnt = 0
                
            res.append(cnt)
            stack.append((nums[i], cnt ))
        return max(res)        


        